from crew import FIICrew

def run_fiis_assistant(pergunta: str):
    # Initialize the FIICrew
    crew_instance = FIICrew()

    # Run the AI FII Assistant
    result = crew_instance.crew().kickoff(inputs={"pergunta": pergunta})

    return result
