from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import xml.etree.ElementTree as ET

app = FastAPI(title="Knowledge Brain API", version="1.0")

SITEMAP_URL = "https://support.brilliantdirectories.com/support/sitemap.xml"

class QueryRequest(BaseModel):
    question: str

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "Knowledge Brain"}

@app.post("/query")
async def query_knowledge_base(request: QueryRequest):
    return {
        "answer": f"Received your question: '{request.question}'. (Connected to Knowledge Brain API)",
        "status": "answered",
        "sources": [
            {
                "title": "Brilliant Directories Solution Center",
                "url": "https://support.brilliantdirectories.com/support/home",
                "relevance": 0.95
            }
        ],
        "confidence": 0.90,
        "needs_human": False
    }

@app.post("/ingestion/run")
async def run_ingestion():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(SITEMAP_URL)
            if response.status_code != 200:
                raise HTTPException(status_code=500, detail="Failed to fetch sitemap")
            
            root = ET.fromstring(response.text)
            namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            urls = [elem.text for elem in root.findall('.//ns:loc', namespaces)]
            
            return {
                "status": "success",
                "total_urls_found": len(urls),
                "message": "Sitemap successfully crawled and parsed."
            }
        except Exception as e:
          return {"status": "error", "message": str(e)}