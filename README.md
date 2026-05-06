## 💬 Simple Chat CLI with Memory (OpenAI SDK)

A beginner-friendly yet practical AI chatbot built using OpenAI SDK and Python.

This project demonstrates how to build a **context-aware conversational system** using:
- Continuous chat loop
- Short-term memory (message history)
- Persistent memory (saved to file)
- Jupyter Notebook for step-by-step learning

---

## 🚀 Features

✅ Interactive CLI chatbot  
✅ Maintains conversation context  
✅ Persistent memory (stored in `memory.json`)  
✅ Automatic memory trimming (to avoid overload)  
✅ Clean and minimal project structure  
✅ Jupyter Notebook version for learning  

---

## 🧠 How It Works

The chatbot maintains a list of messages like this:

```python
messages = [
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": "Hello"},
  {"role": "assistant", "content": "Hi!"}
]

---

## 🔁 Chat Flow
User Input → Append to Memory → Send to OpenAI → Get Response → Store Response → Repeat

---

## 📦 Project Structure
simple-chat-cli/
│── chat.py                 # Main CLI chatbot
│── chat_notebook.ipynb     # Step-by-step notebook version
│── memory.json             # Stored conversation memory (auto-created)
│── requirements.txt
│── README.md
│── .env.example
│── .gitignore

---

## ⚙️ Setup Instructions

1️⃣ Clone Repository


2️⃣ Create Virtual Environment
🪟 Windows
python -m venv venv
venv\Scripts\activate
🍎 Mac / 🐧 Linux
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add API Key

Create a .env file:
OPENAI_API_KEY=your_api_key_here

5️⃣ Run Chatbot
python chat.py

📓 Jupyter Notebook Version

For step-by-step understanding:

jupyter notebook

Open: chat.ipynb

---

🧠 Memory System
🔹 Short-Term Memory
Stored in Python list
Maintains conversation context
🔹 Persistent Memory
Saved to memory.json
Automatically loaded on restart
