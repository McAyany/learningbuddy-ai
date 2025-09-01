# 📚 LearningBuddy AI
An offline-first AI-powered revision app for students aged 10–18. Built with Supabase, HuggingFace, Cursor, and Paystack/Flutterwave.

## Quick features
- Grade-specific AI explanations & quizzes
- Offline mode (cached Q&A)
- Save notes & track progress (Supabase)
- Payments via Paystack or Flutterwave

## Tech stack
Frontend: HTML, CSS, JavaScript
Backend: Python (FastAPI) or Supabase Edge Functions
DB/Auth: Supabase
AI: HuggingFace Inference API
Payments: Paystack / Flutterwave

## Getting started
1. Set up Supabase project and enable Auth.
2. Create HuggingFace API token and set HF_TOKEN.
3. Create Paystack/Flutterwave test keys.
4. Copy `.env.example` to `.env` and fill values.
5. Run backend: `python backend/app.py`
6. Open `frontend/index.html`.

## Folder structure
See repo root for `frontend/`, `backend/`, `prompts/`, `docs/`.

## Security
- Secrets stored server-side in environment variables.
- Supabase Row Level Security (RLS) protects user data.

## Demo
See `docs/demo-script.md` or the embedded video link in the repo.
