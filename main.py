from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/keywords")
async def get_keywords(query: str):
    url = "https://suggestqueries.google.com/complete/search"
    params = {"client": "firefox", "q": query}
    async with httpx.AsyncClient() as client:
        r = await client.get(url, params=params)
        return r.json()[1]

