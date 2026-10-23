import os

def generate_scope_from_transcripts():
    transcript_folder = "transcripts"
    transcripts = []
    
    if os.path.exists(transcript_folder):
        for file in os.listdir(transcript_folder):
            if file.endswith(".txt"):
                with open(os.path.join(transcript_folder, file), "r") as f:
                    transcripts.append(f.read())
                    
    print(f"Loaded {len(transcripts)} meeting transcripts.")
    
    # Synthetic Multi-Agent Scope Synthesis
    scope_document = """
# Scope of Work (SOW)

## 1. Project Objectives
- Implement automated AI Tech Consultant workflows.
- Integrate Knowledge Brain API with Inbox Agent and Scope Generator.

## 2. Deliverables
- Knowledge Brain RAG API
- Inbox Email Categorization Agent
- Meeting-to-Scope Generator

## 3. Timeline & Execution
- Phase 1: Setup & Ingestion
- Phase 2: Agent Workflows
- Phase 3: Testing & Submission
"""
    return scope_document

if __name__ == "__main__":
    sow = generate_scope_from_transcripts()
    print("\n--- Generated Scope of Work ---")
    print(sow)