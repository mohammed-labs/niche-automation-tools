import openai

def generate_resume(prompt):
    openai.api_key = "your-api-key"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    prompt = "Create a resume summary for a Python developer with 5 years of experience."
    print(generate_resume(prompt))
