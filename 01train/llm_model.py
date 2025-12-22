from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os 
load_dotenv()

def model():
    '''
    Using HuggingFace API for open-source model without local download.
    '''
    try:
    
        force_text = os.getenv("HUGGINGFACE_FORCE_TEXT", "0") == "1"
        provider = os.getenv("HUGGINGFACE_PROVIDER", "").lower()
        task = "text-generation"
        if not force_text and ("groq" in provider or os.getenv("HUGGINGFACE_FORCE_CONVERSATIONAL", "0") == "1"):
            task = "conversational"

        model = HuggingFaceEndpoint(
            repo_id="openai/gpt-oss-20b",
            task=task,
            temperature=0,
            max_new_tokens=1024,
            huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY")
        )
    except Exception as e:
        print(f"Error loading model: {e}")
        model = None    
    return model