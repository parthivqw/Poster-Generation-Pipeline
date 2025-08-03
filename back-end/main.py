from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.schema import PosterRequest, PosterImageRequest
from utils.llama_generate_fields import call_llama_generate_fields
from utils.prompt_builder import build_image_generation_prompt
from utils.image_generator import generate_poster_image
from dotenv import load_dotenv
import json
import os

load_dotenv()

app = FastAPI()

# ✅ Allow frontend (Angular) to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ For dev only. Use specific domain in prod.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🧠 Step 1: Generate Poster Fields using Groq LLaMA
@app.post("/generate-fields")
async def generate_fields(data: PosterRequest):
    try:
        print("📥 Received POST with data:", data)

        # 🔁 Call Groq (LLaMA)
        raw_response = call_llama_generate_fields(data)
        print("🧠 Raw response from LLaMA:\n", raw_response)

        # 🧪 Parse JSON string safely
        parsed_json = json.loads(raw_response)

        # ✅ Return clean object to frontend
        return {
            "status": "success",
            "data": parsed_json,
            "message": "Poster fields generated using LLaMA."
        }

    except json.JSONDecodeError as e:
        print("❌ JSON parsing error:", str(e))
        raise HTTPException(status_code=500, detail="Failed to parse LLaMA response as JSON.")

    except Exception as e:
        print("❌ General error:", str(e))
        raise HTTPException(status_code=500, detail=str(e))

# 🖼️ Step 2: Generate Final Poster Image using Imagen API
@app.post("/generate-poster")
async def generate_poster(data: PosterImageRequest):
    try:
        print("🎨 Generating poster from fields:", data.fields)

        # ✍️ Use LLaMA-suggested theme if available, else fallback to user-supplied
        theme = data.fields.get("suggested_theme") or data.theme

        # 🧠 Build full image generation prompt
        prompt = build_image_generation_prompt(data.fields, theme)
        print("🧾 Final crafted prompt:\n", prompt)

        # 🎨 Generate base64 image from prompt
        base64_img = generate_poster_image(prompt)

        return {
            "status": "success",
            "image_base64": base64_img,
            "message": "Poster image generated successfully."
        }

    except Exception as e:
        print("❌ Image generation error:", str(e))
        raise HTTPException(status_code=500, detail="Poster image generation failed.")
