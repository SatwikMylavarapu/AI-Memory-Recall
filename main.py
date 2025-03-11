import os
import google.generativeai as genai
from fastapi import FastAPI, HTTPException, UploadFile, File
from pymongo import MongoClient
from pydantic import BaseModel
from dotenv import load_dotenv
import shutil
from transformers import pipeline

# ✅ Load environment variables
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ✅ Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# ✅ Initialize FastAPI
app = FastAPI()

# ✅ MongoDB Connection
client = MongoClient(MONGO_URI)
db = client["memoryRecallDB"]
notes_collection = db["notes"]

# ✅ Request Models    
class MemoryQuery(BaseModel):
    query: str

# 🎯 1️⃣ AI-Powered Recall (Gemini)
@app.post("/ai-recall")
def ai_recall(memory_query: MemoryQuery):
    query = memory_query.query

    # 🔍 Fetch stored memories
    memories = [note["memory"] for note in notes_collection.find({}, {"_id": 0, "memory": 1})]

    if not memories:
        return {"recalled_memory": "No memories found in the database."}

    # 📜 Format prompt
    prompt = f"I have the following memories stored: {memories}. Based on the query '{query}', retrieve the most relevant memory."

    model = genai.GenerativeModel("gemini-1.5-pro-latest")  # 🔥 Use Gemini API
    response = model.generate_content(prompt)

    return {"recalled_memory": response.text}

# 🎤 2️⃣ Convert Speech-to-Text (Whisper)
from datetime import datetime

@app.post("/transcribe-audio")
async def transcribe_audio(file: UploadFile = File(...)):
    file_path = f"./audio_{file.filename}"
    
    # 🔹 Save audio file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 🔥 Load Whisper Model
    pipe = pipeline("automatic-speech-recognition", model="openai/whisper-small")
    
    # 🎙️ Transcribe
    result = pipe(file_path)
    transcription = result["text"]

    # 📝 Store in MongoDB with timestamp
    notes_collection.insert_one({
        "memory": transcription,
        "timestamp": datetime.utcnow()
    })

    return {"message": "✅ Transcription completed!", "transcription": transcription}


# 🗣️ 3️⃣ Convert Text to Speech (TTS - Future Integration)
import pyttsx3

@app.post("/text-to-speech")
def text_to_speech(memory_query: MemoryQuery):
    text = memory_query.query

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

    return {"message": "🔊 Speaking:", "text": text}


@app.get("/")
def read_root():
    return {"message": "Welcome to AI Memory Recall API! Use /docs to test endpoints."}

@app.post("/store-memory")
def store_memory(memory_query: MemoryQuery):
    new_memory = {"memory": memory_query.query}
    notes_collection.insert_one(new_memory)
    return {"message": "✅ Memory stored successfully!", "stored_memory": memory_query.query}


from mangum import Mangum

handler = Mangum(app)
