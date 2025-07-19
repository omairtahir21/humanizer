import requests

API_KEY = "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"  # Put your OpenRouter key directly here
API_URL = "https://openrouter.ai/api/v1/chat/completions"

def humanize_text(input_text):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
Please humanize the following text. Make it more natural and conversational, but keep the original meaning.

Text:
\"\"\"{input_text}\"\"\"
    """

    payload = {
        "model": "meta-llama/llama-3-70b-instruct",  # ✅ changed
        "messages": [
            {"role": "system", "content": "You are an expert at rewriting AI-generated content to sound more human."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"OpenRouter API Error: {response.text}")

    return response.json()['choices'][0]['message']['content'].strip()