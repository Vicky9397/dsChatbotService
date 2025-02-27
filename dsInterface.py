import ollama

def generate_response(prompt):
    # Using Ollama's streaming response
    for chunk in ollama.chat(model="deepseek-r1:8b", messages=[{"role": "user", "content": prompt}], stream=True):
        #print (f"{chunk['message']['content']}")  # SSE format
        yield f"data: {chunk['message']['content']}\n\n"

#generate_response("Explain quantum physics in simple terms")