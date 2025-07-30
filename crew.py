from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.excel_knowledge_source import ExcelKnowledgeSource
from crewai.knowledge.source.crew_docling_source import CrewDoclingSource
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource

pdf_source = PDFKnowledgeSource(
    file_paths=["HABT11.pdf"]
)


# excel_tool = ExcelKnowledgeSource(
#     file_paths=[r"PLANILHA ORIGINAL FUNDOS IMOBILIÁRIOS.xlsx"]
# )

# # Create a knowledge source from web content
# content_source = CrewDoclingSource(
#     file_paths=[
#         "https://www.fundsexplorer.com.br/ranking",
#     ],
# )

# Create an LLM with a temperature of 0 to ensure deterministic outputs
llm = LLM(model="gpt-4o-mini", temperature=0.3)

@CrewBase
class FIICrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def especialista_fiis(self) -> Agent:
        return Agent(
            config=self.agents_config["especialista_fiis"],
            verbose=True,
            llm=llm,
        )

    @task
    def responder_recomendacao_fiis(self) -> Task:
        return Task(
            config=self.tasks_config["responder_recomendacao_fiis"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MQuestKnowledge crew"""

        return Crew(
            agents=[self.especialista_fiis()],
            tasks=[
                self.responder_recomendacao_fiis(),
            ],
            process=Process.sequential,
            verbose=True,
            knowledge_sources=[pdf_source],
        )