from serpapi import GoogleSearch
from dotenv import load_dotenv
import os

load_dotenv()


def run_researcher_agent(topic):
    params = {
        "engine": "google",
        "q": topic,
        "api_key": os.getenv("SERPAPI_API_KEY"),
        "num": 5
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    organic_results = results.get("organic_results", [])
    output = []

    for result in organic_results:
        title = result.get("title")
        snippet = result.get("snippet")
        link = result.get("link")
        output.append(f"**{title}**\n{snippet}\n{link}")

    return "\n\n".join(output)
