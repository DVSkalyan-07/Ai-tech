import json

def load_emails():
    try:
        with open("emails.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def process_inbox():
    emails = load_emails()
    results = []
    
    for email in emails:
        subject = email.get("subject", "").lower()
        body = email.get("body", "").lower()
        
        # Simple rule-based triage categorization
        if "pricing" in subject or "cost" in body:
            category = "Sales Inquiry"
            priority = "High"
        elif "error" in subject or "bug" in body or "issue" in body:
            category = "Technical Support"
            priority = "Urgent"
        else:
            category = "General"
            priority = "Normal"
            
        results.append({
            "id": email.get("id"),
            "sender": email.get("sender"),
            "category": category,
            "priority": priority,
            "status": "triaged"
        })
        
    return results

if __name__ == "__main__":
    triaged_emails = process_inbox()
    print(f"Successfully triaged {len(triaged_emails)} emails.")