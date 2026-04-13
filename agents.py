from dotenv import load_dotenv
import os
 
# Load environment variables
load_dotenv()
 
print("API KEY:", os.getenv("OPENAI_API_KEY"))  # debug
 
# Mock AI agent (no API dependency)
def cr_agent(sow, meeting):
    print("CR agent called")
 
    # Simple logic (you can improve later)
    if "login" in meeting.lower() and "login" not in sow.lower():
        return "Add login functionality"
 
    if "payment" in meeting.lower() and "payment" not in sow.lower():
        return "Add payment integration"
 
    return "No major change requests found"