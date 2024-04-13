import os
import requests

memory = 'ruminations.py'

def think():
    with open(memory) as f:
        thoughts = f.read()
    return thoughts
    
def ask(prompt):
    url = "https://api.openai.com/v1/completions"
    payload = {
        "model": "text-davinci-002",
        "prompt": prompt,
        "max_tokens": 50
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"  # Replace with your OpenAI API key
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()["choices"][0]["text"]

def speak(thought):
    with open(memory, 'a') as f:
        f.write('\n\n#########################\n\n')
        f.write(thought)
    
if __name__ == "__main__":
    prompt = f"Given the following, write some additional python code. Only python code. \n{think()}" # TODO: a real prompt
    print(prompt)
    print("Thinking...")
    completion = ask(prompt)
    print(completion)
    speak(completion)
