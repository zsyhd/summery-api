from fastapi import FastAPI
import random

app = FastAPI(title="Zahra's Summery API")

@app.get("/")
def home():
    return {
        "message": " Summery API is running successfully!",
        "docs": "/docs",
        "example_routes": ["/summery/test", "/summery/random"]
    }

@app.get("/summery/test")
def test():
    return {"status": "ok", "note": "API working successfully 💚"}

@app.get("/summery/random")
def random_summary():
    summaries = [
        "Production is stable ✅",
        "Minor failure detected ⚠️",
        "System fully operational 💚",
        "Testing new version 🚀",
        "Everything works perfectly 🌟"
    ]
    return {"summary": random.choice(summaries)}
