Build a mobile-first LearningBuddy web app using plain HTML, CSS, JavaScript (frontend) and Python FastAPI (backend). Requirements:
- Pages: signup (with grade selection), login, subject list, chat UI, saved notes, payment.
- Frontend: vanilla JS for Supabase Auth integration and fetch calls to backend endpoints: /api/hf-infer, /api/save-message, /api/create-payment.
- Chat UI: messages show user vs AI; input box; save note button saves to backend.
- Offline: include a simple service worker and IndexedDB caching for recent 50 Q&As (use localForage).
- Backend: FastAPI endpoints as above, use environment variables for HF_TOKEN, SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, PAYSTACK_SECRET. The /hf-infer endpoint calls HuggingFace Inference API and prepends "Explain to a {grade} student" to prompts.
- Provide minimal CSS for a clean mobile-first layout.
Return a zip-structure with files and short comments on where to paste env vars.
