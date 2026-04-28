# Smart Marketing Assistant using Crew AI

## Overview

The Smart Marketing Planning Agent is an AI-powered solution designed to help marketers build smarter campaigns and launch marketing strategies with confidence. It combines research, trend analysis, campaign planning, and briefing creation to support every step of marketing preparation.

## Workflow

## Features

- **Campaign Research**: Collect market insights, competitor information, and audience context.
- **Marketing Analysis**: Identify trends, opportunities, risks, and positioning strategies.
- **Strategy Planning**: Create high-impact campaign ideas, messaging frameworks, and activation plans.
- **Briefing & Execution**: Produce a polished marketing brief that guides creative, media, and launch decisions.
- **Collaborative Planning**: Coordinate AI agents to build a unified marketing plan across research, strategy, and execution.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Smart-Marketing-Assistant-using-Ai-Agents.git
   cd Smart-Marketing-Assistant-using-Ai-Agents
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add the following variables:
     ```
     LANGCHAIN_TRACING_V2=true
     LANGCHAIN_API_KEY=your langchain api key
     OPENROUTER_API_KEY=your openrouter api key
     OPENROUTER_MODEL=openrouter/openai/gpt-3.5-turbo
     EXA_API_KEY=your-exa-api-key
     ```

## Usage

1. **Run the Assistant**:

   ```bash
   python main.py
   ```

2. **Use the Web Interface**:
   Open your web browser and navigate to `http://localhost:3000` once the frontend is running.

## Configuration

- **Customization**:
  You can customize the assistant's behavior and settings by modifying the `config.py` file.

- **AI Models**:
  The project uses OpenRouter-compatible LLMs. You can replace the model by updating `OPENROUTER_MODEL` in the `.env` file.

## Project Structure

- `requirements.txt:` Lists required Python dependencies.
- `main.py:` Main script to run the AI agents.
- `src/agents.py:` Defines AI agents for research, marketing analysis, strategy, and briefing.
- `src/tasks.py:` Defines the marketing planning tasks that each agent executes.
- `src/tools.py:` Contains search and data tools used by the agents.

## Contributing

We welcome contributions to enhance the functionality of the Smart Marketing Assistant. To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch
   ```
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please open an issue in the repository or contact the project maintainers.

---

Thank you for using the Smart Marketing Assistant! We hope it helps you succeed with your marketing and meeting preparation.
