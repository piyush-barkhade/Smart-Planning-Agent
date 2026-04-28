# Smart Marketing Planning Agent - Frontend

A modern React frontend for the Smart Marketing Planning Agent application.

## Setup Instructions

### Prerequisites
- Node.js 16+ installed
- Backend API running on `http://localhost:8000`

### Installation

1. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

### Running the Frontend

**Development mode:**
```bash
npm run dev
```
The application will be available at `http://localhost:3000`

**Production build:**
```bash
npm run build
```

**Preview production build:**
```bash
npm run preview
```

## Features

- **Clean, modern UI** with gradient background
- **Real-time form input** for campaign stakeholders, context, and objectives
- **Loading indicator** while AI marketing planning agents process
- **Results display** for marketing plan outputs and strategy summaries
- **Download results** as a text file
- **Responsive design** works on all screen sizes
- **Error handling** with user-friendly messages

## Architecture

The frontend communicates with the FastAPI backend via REST API:

- **POST /api/prepare-meeting** - Initiates marketing plan creation
- **GET /api/health** - Health check endpoint

## Tech Stack

- **React 18** - UI library
- **Vite** - Build tool
- **Axios** - HTTP client
- **CSS3** - Styling with responsive design

## Notes

- Make sure the backend API is running before starting the frontend
- The frontend proxies API requests to `http://localhost:8000`
- All environment variables are loaded from the backend .env file
