# Quick Start Guide

## 🚀 Start Everything in 5 Minutes

### Step 1: Install Backend Dependencies

```bash
pip install -r requirements.txt
```

This installs the marketing planning AI stack and API server.

### Step 2: Start Backend API

```bash
python api.py
```

You should see:

```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Step 3: Install Frontend Dependencies (New Terminal)

```bash
cd frontend
npm install
```

### Step 4: Start Frontend

```bash
npm run dev
```

You should see:

```
VITE v4.x.x  ready in xxx ms

➜  Local:   http://localhost:3000/
```

### Step 5: Open Browser

Go to `http://localhost:3000` and you're done! 🎉

Use the web app to input campaign participants, marketing context, and objectives, then generate your marketing plan.

---

## Environment Variables

Before running, make sure `.env` has:

```
OPENROUTER_API_KEY=your-key
EXA_API_KEY=your-key
OPENROUTER_MODEL=openrouter/openai/gpt-3.5-turbo
```

Get your keys:

- OpenRouter: https://openrouter.ai/keys
- Exa: https://dashboard.exa.ai

---

## Troubleshooting

**Backend won't start?**

- `pip install --upgrade crewai`
- Check `python api.py` for error details

**Frontend won't connect?**

- Make sure backend is running on port 8000
- Try `http://localhost:8000/api/health` in browser

**Missing module errors?**

- Run `pip install -r requirements.txt` again
- Then `pip install --upgrade crewai`

**Port already in use?**

- Backend: Change port in `api.py` line 65
- Frontend: Change port in `frontend/vite.config.js` line 6

---

## Using the Web App

1. **Fill the form:**
   - Participants (emails)
   - Meeting context
   - Meeting objective

2. **Click "Prepare Meeting 🚀"**

3. **Wait for results** (typically 1-2 minutes)

4. **Download results** (optional)

---

## What Each Agent Does

🔍 **Research Specialist** - Researches participants and companies
📊 **Industry Analyst** - Analyzes market trends
💡 **Meeting Strategy Advisor** - Develops talking points
📋 **Briefing Coordinator** - Compiles everything into a report

All work together automatically when you submit the form!

---

## Next Steps

- Customize agent prompts in `src/agents.py`
- Modify task descriptions in `src/tasks.py`
- Update styling in `frontend/src/App.css`
- Add new features to the React app

Enjoy! 🎯
