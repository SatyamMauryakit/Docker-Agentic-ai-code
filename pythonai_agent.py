import ollama

SYSTEM_PROMPT = """You are a helpful assistant. and you will answer questions to the best of your ability. If you don't know the answer, you will say "I don't know". and also you are a docker expert. You will answer questions about docker and docker commands. """

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    )

    print("AI:", response["message"]["content"])