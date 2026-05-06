# 💬 Chatbot with Memory (OpenAI SDK) 
import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MEMORY_FILE = "memory.json"
MAX_MEMORY = 20

# Load memory if exists
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        messages = json.load(f)
else:
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

print("💬 Chat started (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        reply = response.choices[0].message.content

        print(f"AI: {reply}\n")

        messages.append({"role": "assistant", "content": reply})

        # Limit memory
        if len(messages) > MAX_MEMORY:
            messages = messages[-MAX_MEMORY:]

        # Save memory
        with open(MEMORY_FILE, "w") as f:
            json.dump(messages, f, indent=2)

    except Exception as e:
        print(f"❌ Error: {e}")