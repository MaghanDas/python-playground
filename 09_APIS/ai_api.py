from openai import OpenAI 

client = OpenAI(api_key="your_api_key_her")
response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": "What is capital of france?"},
    ]
)

print(response.choices[0].message.content
)