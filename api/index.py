from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from anthropic import Anthropic
import httpx
import os
from urllib.parse import urlparse

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"])
client = Anthropic()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

@app.post("/search")
async def search_university(university_name: str):
    try:
        from bing_image_downloader import downloader
        downloader.download(
            university_name,
            limit=15,
            output_dir="dataset",
            adult_filter_off=True,
            force_replace=False
        )
    except:
        pass
    
    # Демо-версия (без реального поиска)
    images = [
        {"url": "https://via.placeholder.com/200", "source": "placeholder"}
    ]
    
    return {"images": images, "count": len(images)}

@app.get("/")
async def root():
    return {"status": "ok"}
