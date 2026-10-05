import os, requests
from dotenv import load_dotenv
load_dotenv()
key = os.environ.get("GEMINI_API_KEY", "").strip('"')
r = requests.get(
    "https://generativelanguage.googleapis.com/v1beta/models",
    params={"key": key},
)
data = r.json()
if "error" in data:
    print("Error:", data["error"])
else:
    models = [
        m["name"].replace("models/", "")
        for m in data.get("models", [])
        if "generateContent" in m.get("supportedGenerationMethods", [])
    ]
    for m in sorted(models):
        print(m)
