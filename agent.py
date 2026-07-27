from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain.agents import create_agent
import subprocess

SYSTEM_PROMPT = """
You are a helpful assistant. You answer questions to the best of your ability.
If you don't know the answer, say "I don't know".

You are also a Docker expert. You can answer Docker questions and use the
available tools when needed.
"""

@tool
def show_running_containers() -> str:
    """Show all running Docker containers."""
    result = subprocess.run(
        ["docker", "ps"],
        capture_output=True,
        text=True,
    )
    return result.stdout


@tool
def show_container_logs(container_id: str) -> str:
    """Show logs of a Docker container using its container ID."""
    result = subprocess.run(
        ["docker", "logs", container_id],
        capture_output=True,
        text=True,
    )
    return result.stdout


llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0.7,
)

tools = [show_running_containers, show_container_logs]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=SYSTEM_PROMPT,
)

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_input,
                }
            ]
        }
    )

    print("AI:", response["messages"][-1].content)