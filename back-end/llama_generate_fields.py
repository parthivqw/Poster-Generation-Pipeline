from openai import OpenAI
import os

def call_llama_generate_fields(data):
    client = OpenAI(
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1"
    )

    # 🛠️ Coerce all checkbox fields to boolean
    def to_bool(val):
        return str(val).lower() == "true" or val is True

    # ✅ 1. Build selected fields list safely
    selected_fields = []
    if to_bool(data.include_hero_headline):
        selected_fields.append("hero_headline")
    if to_bool(data.include_hero_subline):
        selected_fields.append("hero_subline")
    if to_bool(data.include_description):
        selected_fields.append("description")
    if to_bool(data.include_cta):
        selected_fields.append("cta")
    if to_bool(data.include_testimonial):
        selected_fields.append("testimonial")
    if to_bool(data.include_success_metrics):
        selected_fields.append("success_metrics")
    if to_bool(data.include_target_audience):
        selected_fields.append("target_audience")
    if to_bool(data.include_cta_link):
        selected_fields.append("cta_link")

    # 2. Handle theme logic
    if data.theme:
        theme_msg = (
            f"The user provided a rough theme: '{data.theme}'. "
            "Your job is to expand it into a visually detailed, layout-aware prompt suitable for an image generation model. "
            "Include lighting, color palette, background scene, layout structure, mood, and visual motifs. "
            "Avoid vague terms like 'modern' or 'futuristic'."
        )
    else:
        theme_msg = (
            "The user did not provide a theme. "
            "Based on the main intent, suggest a complete and vivid visual background prompt for image generation. "
            "Include scene composition, mood, lighting, colors, and layout motifs. "
            "Avoid overused styles like 'futuristic neon city' unless truly relevant."
        )

    # 3. Compose system prompt
    system_prompt = f"""
You are a professional poster content generation AI specializing in educational and marketing visuals.

The user wants a poster with the following fields: {', '.join(selected_fields)}.
Main intent: "{data.main_prompt}"
{theme_msg}

🧠 STRICT INSTRUCTIONS:
- Respond with a clean JSON object only — no explanations, no markdown, no headers.
- Output only the selected keys.
- If the theme was not provided, add a key called 'suggested_theme' with the generated description.
- If theme was provided, you must expand and regulate it — replace the original version.

✂️ TOKEN LIMITS (DO NOT EXCEED):
- "hero_headline": max 12 tokens
- "hero_subline": max 15 tokens
- "description": max 25 tokens
- "testimonial": max 25 tokens (short single-quote quote)
- "success_metrics": max 20 tokens (pipe-separated stats)
- "target_audience": max 15 tokens
- "cta" and "cta_link": very short and clean

✅ FORMAT EXAMPLE:
{{
  "hero_headline": "Master AI with Python!",
  "hero_subline": "Your journey to a tech career begins here",
  "cta": "Enroll Now",
  "cta_link": "https://pythonbootcamp.io",
  "suggested_theme": "A high-energy tech workspace with students coding on laptops, surrounded by glowing circuit overlays, ambient lighting, and vibrant color gradients in blue and teal."
}}
"""

    # 4. Call LLaMA model
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": system_prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
