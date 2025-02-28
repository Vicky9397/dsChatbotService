import ollama

def generate_response(prompt):
    # Using Ollama's streaming response
    for chunk in ollama.chat(model="deepseek-r1:8b", messages=[{"role": "user", "content": prompt}], stream=True):
        print (chunk['message']['content'], end='', flush=True)  # SSE format
        # yield f"data: {chunk['message']['content']}\n\n"
        #yield (chunk['message']['content'], end='', flush=True)

generate_response("Explain AI in simple terms.")