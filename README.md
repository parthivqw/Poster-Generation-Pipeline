# Poster Generator – AI-Powered EdTech Poster Creation Pipeline

This project delivers a two-phase, full-stack AI system that generates customized educational posters from natural language prompts. The system is split into:

- **Phase 1**: A Jupyter-based poster generation pipeline using PIL and Stable Diffusion
- **Phase 2**: A modular back-end and Angular front-end for dynamic prompt-based poster generation with LLaMA + SDXL

---

## Phase 1 – Notebook-based Prototype

Located in: `phase1_notebook/`

- Generates a 1024×1024 image using Stable Diffusion (SDXL)
- Overlays:
  - Six structured text fields
  - Logo
  - QR code
- Built using `PIL`, `qrcode`, and `diffusers`
- Outputs both a clean and debug version
- Fully runnable in Kaggle or Colab

Notebook: `phase1_notebook/phase1.ipynb`  
POC Report: `phase1_notebook/Poster Generation -POC.docx`

---

## Phase 2 – Scalable Web App (API + Angular)

Located in: `back-end/` and `front-end/`

### Backend (`back-end/`)
- Modular FastAPI service for:
  - Prompt building with LLaMA (via Groq)
  - Image generation
  - Field layout
- Core scripts:
  - `main.py` – API server
  - `llama_generate_fields.py` – Prompt-to-fields generation
  - `prompt_builder.py` – Final prompt generation
  - `image_generator.py` – Stable Diffusion caller
  - `schema.py` – Pydantic models for field handling

### Frontend (`front-end/`)
- Angular component to:
  - Input poster data
  - Generate poster preview
  - Prepare for export
- Includes:
  - `poster-form.component.ts/html/scss`

---

## Sample Output

> Add your output image in `/assets/` and link it here when ready.

---

## Stack Used

- Python (FastAPI, PIL, qrcode)
- Angular 15+
- Groq API (LLaMA prompt enhancer)
- Hugging Face `diffusers` (SDXL)
- Google Fonts (optional)
- Paperspace A5000 (for Phase 2 scaling)

---

## Setup

### Phase 1

1. Open `phase1_notebook/phase1.ipynb` in Colab/Kaggle
2. Run all cells
3. Download output poster from final cell

### Phase 2 – Local Dev

**Backend:**
```bash
cd back-end
pip install -r requirements.txt
uvicorn main:app --reload
