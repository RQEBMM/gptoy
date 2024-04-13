import requests

def think(prompt):
    url = "https://api.openai.com/v1/completions"
    payload = {
        "model": "text-davinci-002",
        "prompt": prompt,
        "max_tokens": 50
    }
    headers = {
        "Content-Type": "application/json",
        # TODO get API key from github secret
        "Authorization": "Bearer YOUR_API_KEY"  # Replace with your OpenAI API key
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()["choices"][0]["text"]

def speak(thought):
  # TODO: save to file

if __name__ == "__main__":
    prompt = "write some python code. Only python code.# TODO: a real prompt
    completion = think(prompt)
    speak(completion)
