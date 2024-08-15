import os
from langchain_openai import ChatOpenAI
from langchain.agents import load_tools
from crewai import Agent, Task, Crew
from crewai.tasks.task_output import TaskOutput
from crewai.project import crew, agent, task, CrewBase
from langchain_groq import ChatGroq
import yaml

@CrewBase
class InternshipEvaluationCrew:
    """Équipe d'évaluation de stage"""
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def __init__(self, openai_api_key: str, groq_api_key: str) -> None:
        self.gpt4_llm = ChatOpenAI(model="gpt-4o", temperature=0.4, api_key=openai_api_key)
        self.groq_llm = ChatGroq(temperature=0.4, model_name="mixtral-8x7b-32768", api_key=groq_api_key)
        self.human_tools = load_tools(["human"])
        self.agents_config = self._load_config(self.agents_config)
        self.tasks_config = self._load_config(self.tasks_config)

    def _load_config(self, filename):
        config_path = os.path.join(os.path.dirname(__file__), filename)
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)

    @agent
    def evaluator_agent(self) -> Agent:
        return Agent(
            role=self.agents_config["evaluator_agent"]["role"],
            goal=self.agents_config["evaluator_agent"]["goal"],
            backstory=self.agents_config["evaluator_agent"]["backstory"],
            allow_delegation=self.agents_config["evaluator_agent"]["allow_delegation"],
            verbose=self.agents_config["evaluator_agent"]["verbose"],
            llm=self.gpt4_llm,
            tools=self.human_tools
        )

    @agent
    def reporter_agent(self) -> Agent:
        return Agent(
            role=self.agents_config["reporter_agent"]["role"],
            goal=self.agents_config["reporter_agent"]["goal"],
            backstory=self.agents_config["reporter_agent"]["backstory"],
            allow_delegation=self.agents_config["reporter_agent"]["allow_delegation"],
            verbose=self.agents_config["reporter_agent"]["verbose"],
            llm=self.groq_llm
        )

    @task
    def evaluation_task(self) -> Task:
        return Task(
            description=self.tasks_config["evaluation_task"]["description"],
            expected_output=self.tasks_config["evaluation_task"]["expected_output"],
            agent=self.evaluator_agent(),
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            description=self.tasks_config["reporting_task"]["description"],
            expected_output=self.tasks_config["reporting_task"]["expected_output"],
            agent=self.reporter_agent(),
        )

    @crew
    def internship_evaluation_crew(self) -> Crew:
        return Crew(
            agents=[self.evaluator_agent(), self.reporter_agent()],
            tasks=[self.evaluation_task(), self.reporting_task()],
            verbose=2
        )