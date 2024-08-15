# AI-Powered Internship Evaluation System

## Overview

This project implements an innovative approach to internship evaluation using multiple Large Language Models (LLMs) and the CrewAI framework. It features two AI agents working in tandem to streamline and enhance the internship evaluation process:

1. **Evaluator Agent (GPT-4)**: Conducts the evaluation by asking questions and gathering information about the internship.
2. **Reporter Agent (Groq's Mixtral 8x7B)**: Synthesizes the collected data to generate a comprehensive evaluation report.

## Features

- Automated internship evaluation process
- Integration of multiple LLMs for specialized tasks
- Markdown report generation
- Configurable evaluation criteria and question sets
- Error handling and smooth inter-agent communication
- Built with Python, leveraging CrewAI for agent orchestration and LangChain for LLM interactions

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Set up a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   GROQ_API_KEY=your_groq_api_key
   ```

## Usage

To run the internship evaluation system:

1. Navigate to the `src/evaluation` directory:
   ```
   cd src/evaluation
   ```

2. Run the main script:
   ```
   python main.py
   ```

3. Follow the prompts to input information about the internship.

4. Once complete, find the generated report in `rapport_evaluation_stage.md`.

## Configuration

You can customize the evaluation process by modifying the following files:

- `src/evaluation/config/agents.yaml`: Configure agent roles and behaviors
- `src/evaluation/config/tasks.yaml`: Define evaluation questions and reporting structure

Example of modifying an agent in `agents.yaml`:
```yaml
evaluator_agent:
  role: Évaluateur de stage
  goal: Évaluer le stage d'un étudiant en posant des questions spécifiques et en notant les réponses
  backstory: >
    Un professionnel expérimenté dans l'évaluation des stages étudiants...
```

## Project Structure

```
evaluation/
│
├── src/
│   └── evaluation/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       ├── tools/
│       │   └── custom_tool.py
│       ├── __init__.py
│       ├── crew.py
│       └── main.py
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

- `src/evaluation/`: Contains the main project code
- `config/`: YAML files for configuring agents and tasks
- `tools/`: Custom tools and utilities
- `crew.py`: Defines the CrewAI setup and agent interactions
- `main.py`: Entry point of the application

## Contributing

Contributions to improve the AI-Powered Internship Evaluation System are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

Please make sure to update tests as appropriate and adhere to the project's coding standards.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [CrewAI](https://github.com/joaomdmoura/crewAI) for the AI agent orchestration framework
- [LangChain](https://github.com/hwchase17/langchain) for LLM interactions
- OpenAI and Groq for providing the LLM models used in this project