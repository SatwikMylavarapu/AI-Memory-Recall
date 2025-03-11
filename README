# 🧠 AI Memory Recall System
Seamlessly store and recall thoughts using AI-powered memory retrieval with AI & NLP.

🚀 **Built with:** FastAPI, MongoDB, AWS EC2, Docker, Streamlit  

---

## 📜 Project Overview
This project enables users to **store and recall memories** using AI-powered **Natural Language Processing (NLP)**. Users can store thoughts, retrieve them based on context, and even convert text to speech.

### 🚀 Tech Stack
- **Backend**: FastAPI, MongoDB, Docker, AWS EC2  
- **Frontend**: Streamlit  
- **AI & NLP**: OpenAI Whisper, Google Gemini AI  
- **Storage**: MongoDB Atlas (Free Tier)  
- **Deployment**: AWS EC2 (Free Tier), Docker, Streamlit Cloud  

---

## 1️⃣ Setting Up MongoDB (Free Tier)
We use **MongoDB Atlas** to store memory data.  

### 🔹 Step 1: Create a Free MongoDB Atlas Account
1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)  
2. Click **Get Started** → Select **Shared (Free Tier)**  
3. Choose **AWS (us-east-1)** and click **Create Cluster**  
4. **Network Access** → Allow `0.0.0.0/0` (For Development)  
5. **Create Database User** → Add a username & password  

### 🔹 Step 2: Get Connection String
1. Go to **Database > Connect**  
2. Choose **Python** and copy the connection string  
3. Replace `<username>` and `<password>` with your credentials  
4. Store it in `.env` file (Never commit this!)

```env
MONGO_URI = "mongodb+srv://<username>:<password>@cluster.mongodb.net/memoryRecallDB"
