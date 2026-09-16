from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from anthropic import Anthropic
import os

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"])
client = Anthropic()

@app.get("/")
async def root():
    return {"status": "ok", "message": "API работает"}

@app.post("/search")
async def search_university(university_name: str):
    # Демо-версия
    demo_images = [
        {
            "url": f"https://via.placeholder.com/300?text={university_name}+1",
            "source": "placeholder"
        },
        {
            "url": f"https://via.placeholder.com/300?text={university_name}+2",
            "source": "placeholder"
        },
    ]
    
    return {
        "university": university_name,
        "images": demo_images,
        "count": len(demo_images)
    }
