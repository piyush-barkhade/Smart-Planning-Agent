# Smart Marketing Planning Agent - Complete Setup Guide

## Project Structure

```
Smart-Marketing-Assistant-Crew-AI/
├── src/                    # Backend Python code
│   ├── main.py            # CLI version
│   ├── agents.py          # Marketing planning AI agents
│   ├── tasks.py           # Marketing planning tasks
│   └── tools.py           # Search tool integrations
├── frontend/              # React frontend
│   ├── src/
│   │   ├── main.jsx
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── index.css
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── api.py                 # FastAPI server
├── requirements.txt       # Python dependencies
└── .env                   # Environment variables
```

## Prerequisites

- Python 3.10+
- Node.js 16+
- OpenRouter API key (for LLM)
- Exa API key (for search)

## Backend Setup

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

Make sure these are included:
- crewai
- fastapi
- uvicorn
- python-dotenv
- exa-py

### 2. Configure Environment Variables

Create or update `.env` file:

```
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your-langchain-api-key
OPENROUTER_API_KEY=your-openrouter-api-key
OPENROUTER_MODEL=openrouter/openai/gpt-3.5-turbo
EXA_API_KEY=your-exa-api-key
```

These variables power the marketing planning AI and search tools.

### 3. Run the Backend API

```bash
python api.py
```

The API will be available at `http://localhost:8000`

Test it: `http://localhost:8000/api/health`

## Frontend Setup

### 1. Install Node Dependencies

```bash
cd frontend
npm install
```

### 2. Run Development Server

```bash
npm run dev
```

Access the frontend at `http://localhost:3000`

### 3. Build for Production

```bash
npm run build
```

## Usage

### Option 1: Command Line (CLI)

```bash
python src/main.py
```

### Option 2: Web Interface

1. Start the backend: `python api.py`
2. Start the frontend: `cd frontend && npm run dev`
3. Open `http://localhost:3000`

## API Endpoints

### Health Check
```bash
GET http://localhost:8000/api/health
```

### Prepare Meeting
```bash
POST http://localhost:8000/api/prepare-meeting
Content-Type: application/json

{
  "participants": "email@example.com",
  "context": "AI Marketing discussion",
  "objective": "Find marketing strategies using AI"
}
```

## Troubleshooting

### Backend API fails to start
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Check .env file has valid API keys
- Ensure port 8000 is not in use

### Frontend can't connect to backend
- Verify backend is running on port 8000
- Check CORS settings in api.py (should allow all origins)
- Clear browser cache and refresh

### OpenRouter quota exceeded
- Check your OpenRouter account: https://openrouter.ai/account
- Add payment method or upgrade plan
- You can test with free models on OpenRouter

### Missing Exa API key
- Get your Exa API key from https://dashboard.exa.ai
- Add to .env file as `EXA_API_KEY=your-key`

## Performance Tips

- The first request may take longer (model loading)
- Results are displayed as they complete
- For large participant lists, expect longer processing times
- Download results while viewing to ensure you don't lose data

## Development Notes

### Adding New Agents
Edit `src/agents.py` to add new agent types

### Modifying Tasks
Edit `src/tasks.py` to customize task prompts

### Frontend Customization
- Modify `frontend/src/App.jsx` for layout changes
- Edit `frontend/src/App.css` for styling
- Update `frontend/vite.config.js` for build settings

## Production Deployment

### Backend (Using Gunicorn + Uvicorn)
```bash
pip install gunicorn
gunicorn api:app -w 4 -k uvicorn.workers.UvicornWorker
```

### Frontend (Using Nginx)
1. Build: `npm run build`
2. Serve the `dist/` directory with Nginx
3. Configure Nginx to proxy `/api` requests to backend

## Support

For issues:
1. Check API health: `curl http://localhost:8000/api/health`
2. Verify environment variables are set
3. Check browser console for frontend errors
4. Review backend logs for API errors
