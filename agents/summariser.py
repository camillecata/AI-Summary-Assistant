from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def run_summariser_agent(research_output):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key= os.getenv("OPENAI_API_KEY"),
    )

    completion = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct:free",
        messages=[
            {
                "role": "user",
                "content": f"""You are a summarising AI agent. Please return a summary in this format:

    ## TL;DR
    (2 sentences)

    ## Pros
    - ...

    ## Cons
    - ...

    Content:
    {research_output}
    """
            }
    ],
    )

    summary = completion.choices[0].message.content
    return summary
   

