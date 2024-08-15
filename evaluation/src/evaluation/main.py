import os
from dotenv import load_dotenv
from crew import InternshipEvaluationCrew

# Load environment variables
load_dotenv()

def main():
    # Initialize API keys
    openai_api_key = os.getenv("OPENAI_API_KEY")
    groq_api_key = os.getenv("GROQ_API_KEY")

    # Pass API keys to InternshipEvaluationCrew
    evaluation_crew = InternshipEvaluationCrew(openai_api_key=openai_api_key, groq_api_key=groq_api_key)
    crew = evaluation_crew.internship_evaluation_crew()
    result = crew.kickoff()
    
    print("\nRésultat final de l'évaluation de stage:")
    for task_output in result.task_outputs:
        print(f"Tâche: {task_output.task.description}")
        print(f"Sortie: {task_output.output}")
        print("---")

    # Sauvegarder le rapport dans un fichier Markdown
    with open("rapport_evaluation_stage.md", "w", encoding="utf-8") as f:
        f.write("# Rapport d'Évaluation de Stage\n\n")
        for task_output in result.tasks_output:
            if task_output.task.description.startswith("Rédiger un rapport"):
                # This is the reporting task, write its output directly
                f.write(task_output.output)
            else:
                # For other tasks, add them as separate sections
                f.write(f"## {task_output.task.description}\n\n")
                f.write(f"{task_output.output}\n\n")
            f.write("---\n\n")
    
    print("\nLe rapport d'évaluation de stage a été sauvegardé dans 'rapport_evaluation_stage.md'")

if __name__ == "__main__":
    main()