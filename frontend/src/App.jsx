import { useState } from 'react'
import axios from 'axios'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import './App.css'

function App() {
  const [participants, setParticipants] = useState('')
  const [context, setContext] = useState('')
  const [objective, setObjective] = useState('')
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState('')
  const [error, setError] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError('')
    setResult('')

    try {
      const response = await axios.post('/api/prepare-meeting', {
        participants,
        context,
        objective
      })

      setResult(response.data.result)
    } catch (err) {
      setError(err.response?.data?.detail || 'An error occurred. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  const handleClear = () => {
    setParticipants('')
    setContext('')
    setObjective('')
    setResult('')
    setError('')
  }

  return (
    <div className="app-container">
      <header className="header">
        <h1>🎯 Smart Marketing Planning Agent</h1>
        <p>AI-powered campaign planning, research, and briefing in one workflow.</p>
      </header>

      <div className="main-content">
        <div className="form-section">
          <form onSubmit={handleSubmit} className="meeting-form">
            <div className="form-group">
              <label htmlFor="participants">Campaign Stakeholders</label>
              <textarea
                id="participants"
                value={participants}
                onChange={(e) => setParticipants(e.target.value)}
                placeholder="List key stakeholders, team members, or target personas"
                required
                disabled={loading}
              />
            </div>

            <div className="form-group">
              <label htmlFor="context">Marketing Context</label>
              <textarea
                id="context"
                value={context}
                onChange={(e) => setContext(e.target.value)}
                placeholder="Describe the campaign context, product, audience, or market situation"
                required
                disabled={loading}
              />
            </div>

            <div className="form-group">
              <label htmlFor="objective">Campaign Objective</label>
              <textarea
                id="objective"
                value={objective}
                onChange={(e) => setObjective(e.target.value)}
                placeholder="What are the goals for this marketing campaign?"
                required
                disabled={loading}
              />
            </div>

            <div className="button-group">
              <button
                type="submit"
                className="btn btn-primary"
                disabled={loading}
              >
                {loading ? 'Building Marketing Plan... ⏳' : 'Build Marketing Plan 🚀'}
              </button>
              <button
                type="button"
                className="btn btn-secondary"
                onClick={handleClear}
                disabled={loading}
              >
                Reset
              </button>
            </div>
          </form>
        </div>

        <div className="results-section">
          {error && (
            <div className="error-message">
              <strong>Error:</strong> {error}
            </div>
          )}

          {loading && (
            <div className="loading-message">
              <div className="spinner"></div>
              <p>Your AI agents are working on your meeting preparation...</p>
              <p className="loading-hint">This may take a minute or two</p>
            </div>
          )}

          {result && !loading && (
            <div className="result-box">
              <h2>📋 Marketing Plan Results</h2>
              <div className="result-content">
                <ReactMarkdown remarkPlugins={[remarkGfm]}>{result}</ReactMarkdown>
              </div>
              <button
                onClick={() => {
                  const element = document.createElement('a')
                  const file = new Blob([result], { type: 'text/plain' })
                  element.href = URL.createObjectURL(file)
                  element.download = 'marketing-plan.txt'
                  document.body.appendChild(element)
                  element.click()
                  document.body.removeChild(element)
                }}
                className="btn btn-download"
              >
                📥 Download Results
              </button>
            </div>
          )}

          {!result && !loading && !error && (
            <div className="empty-state">
              <p>Fill out the form and click "Build Marketing Plan" to get started.</p>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

export default App
