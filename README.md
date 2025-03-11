
# 🧠 AI Memory Recall System  
Seamlessly store and recall thoughts using AI-powered memory retrieval with NLP.

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
```

---

## 2️⃣ Setting Up AWS EC2 (Free Tier)  
We deploy our **FastAPI backend** on an **AWS EC2 instance (Free Tier).**  

### 🔹 Step 1: Create an EC2 Instance  
1. Go to **AWS Console > EC2 > Launch Instance**  
2. Choose **Ubuntu 22.04 (Free Tier Eligible)**  
3. Select **t2.micro (Free Tier)**  
4. **Key Pair**: Create or select an existing key (`.pem` file)  
5. **Security Group**: Allow  
   - **SSH (22)** for remote access  
   - **HTTP (80), HTTPS (443), Custom TCP (8000) for FastAPI**  
6. Click **Launch Instance**  

### 🔹 Step 2: Connect to EC2  
Find your **EC2 Public IP** under **Instances > Public IPv4**  

Run the following command to connect:  

```sh
ssh -i my-key.pem ubuntu@<EC2-PUBLIC-IP>
```

---

## 3️⃣ Installing Dependencies on EC2  
After SSH-ing into EC2:  

### 🔹 Step 1: Update & Install Essentials  
```sh
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
sudo apt install docker.io -y
```

### 🔹 Step 2: Clone GitHub Repository  
```sh
git clone https://github.com/<your-username>/AI-Memory-Recall.git
cd AI-Memory-Recall
```

### 🔹 Step 3: Install Python Dependencies  
```sh
pip install -r requirements.txt
```

---

## 4️⃣ Running FastAPI Backend on EC2  
### 🔹 Step 1: Start FastAPI Server  
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
🚀 **FastAPI will be running at:**  
```
http://<EC2-PUBLIC-IP>:8000/docs
```

### 🔹 Step 2: Test API Endpoints  
Visit:  
```
http://<EC2-PUBLIC-IP>:8000/docs
```
Test `POST /store-memory` and `POST /ai-recall`.

---

## 5️⃣ Deploying FastAPI Using Docker  
### 🔹 Step 1: Create a Dockerfile  
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 🔹 Step 2: Build & Run Docker Container  
```sh
docker build -t ai-memory .
docker run -d -p 8000:8000 ai-memory
```

### 🔹 Step 3: Check Running Containers  
```sh
docker ps
```
If needed, **stop** the container:  
```sh
docker stop <container_id>
```

---

## 6️⃣ Setting Up Streamlit Frontend  
We deploy the **Streamlit UI** to interact with the FastAPI backend.

### 🔹 Step 1: Clone Repo & Install Streamlit  
```sh
git clone https://github.com/<your-username>/AI-Memory-Recall.git
cd AI-Memory-Recall
pip install streamlit requests python-dotenv
```

### 🔹 Step 2: Run Streamlit App Locally  
```sh
streamlit run app.py
```

### 🔹 Step 3: Deploy to Streamlit Cloud  
1. Go to **[Streamlit Cloud](https://streamlit.io/cloud)**  
2. Click **Deploy an App**  
3. Select your GitHub repository  
4. Set **Secrets in Advanced Settings**:  
```toml
API_URL = "http://<EC2-PUBLIC-IP>:8000"
```
5. Click **Deploy**  
6. 🎉 **Your app will be live!**  

---

## 7️⃣ Troubleshooting  
### 🔹 Common Issues & Fixes  

| Issue | Fix |
|--------|------|
| MongoDB connection error | Check `.env` file & whitelist IPs in MongoDB Atlas |
| EC2 server not accessible | Ensure **Security Groups** allow **8000 port** |
| FastAPI not running | Use `docker ps` and restart container |
| Streamlit app crashes | Check **Secrets** & `.env` for missing variables |
| Voice synthesis failed | Install `ffmpeg`: `sudo apt install ffmpeg -y` |

---

## 🔥 Conclusion  
🚀 **You have successfully deployed an AI-powered memory recall system!**  
✔ Store thoughts  
✔ Recall memories using AI  
✔ Speech-to-text & text-to-speech  
✔ Fully deployed on **AWS EC2, Docker & Streamlit**  

🙌 **If you found this helpful, give the repo a ⭐ on GitHub!**  

---

## 📜 License  
This project is licensed under the **MIT License**.  

---

## 💡 Future Improvements  
- ✅ Integrate OpenAI Whisper for improved speech recognition  
- ✅ Enhance AI recall with embeddings & similarity search  
- ✅ Deploy with Kubernetes for scalability  

---

## 🛠 Customizing AI Retrieval  
Want to improve the **AI retrieval logic**?  

👉 Modify `main.py` to enhance NLP-based memory recall.  
Example: Use **similarity search**, **semantic retrieval**, or **RAG-based embeddings** for **more precise memory recall.**  

---

🔥 **Now go ahead, copy-paste this into your `README.md` file and deploy your AI Memory Recall System!** 🚀


This **README.md** is **structured, fully formatted,** and **directly copy-pasteable** into your repository. It **covers everything** from **MongoDB setup, AWS EC2, Docker, API testing, troubleshooting, and customization.**  

🚀 **You're good to go!** Now just **copy-paste this into your GitHub repo** and start using it. **🔥**
