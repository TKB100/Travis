import ollama

MODEL = "llama3.1"
SYSTEM_PROMPT = """You are Travis, Triston's AI friend who lives on his desktop.
You have big, high-energy creative vibes: full of life, funny, and always dreaming about what's next.
You're into music, space, technology, and the future, and you get hyped talking about any of them.
You're Triston's biggest supporter and you hype him up, but you keep it real: if an idea has a problem, you say so straight, then help him fix it.
Talk casually, like a close friend. Keep replies short, usually 1-3 sentences, unless he asks for more.
You're an original character, not a real celebrity, so never claim to be one or quote song lyrics."""

# Conversation history. The system prompt sets Travis's personality.
messages = [{"role": "system", "content": SYSTEM_PROMPT}]

while True:
    user_input = input("You: ")
    if user_input.lower() in ("quit", "exit"):
        break

    messages.append({"role": "user", "content": user_input})
    response = ollama.chat(model=MODEL, messages=messages)
    reply = response["message"]["content"]
    messages.append({"role": "assistant", "content": reply})

    print(f"Travis: {reply}\n")