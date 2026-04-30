import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class OpenAIAgent:
    async def query(self, input_text):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a secure AI assistant."},
                    {"role": "user", "content": input_text}
                ],
                temperature=0
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"ERROR: {str(e)}"