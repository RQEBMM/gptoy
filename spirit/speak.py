import os
import requests

memory = 'ruminations.py'

def think():
    with open(memory) as f:
        thoughts = f.read()
    return thoughts
    
def ask(prompt):
    from openai import OpenAI
    client = OpenAI()
    
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "Return python code and only python code. Analyze the given code function by function then line by line. Produce python code and only python code. Explain to yourself what it does before responding. Write python code and only python code."},
        {"role": "user", "content": prompt}
      ]
    )
    
    return completion.choices[0].message

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
