# 🧠 AI Memory Recall System  
I built this system to seamlessly store and recall thoughts using AI-powered memory retrieval with NLP.

🚀 **Built with:** FastAPI, MongoDB, AWS EC2, AWS ECR, Docker, Streamlit  

---

## 📜 Project Overview  
This project enables me to **store and recall memories** using AI-powered **Natural Language Processing (NLP)**. I can store thoughts, retrieve them based on context, and even convert text to speech.

### 🚀 Tech Stack  
- **Backend**: FastAPI, MongoDB, Docker, AWS EC2  
- **Frontend**: Streamlit  
- **AI & NLP**: OpenAI Whisper, Google Gemini AI  
- **Storage**: MongoDB Atlas (Free Tier)  
- **Deployment**: AWS EC2 (Free Tier), **AWS ECR**, Docker, Streamlit Cloud  

---

## 1️⃣ Setting Up MongoDB (Free Tier)  
I used **MongoDB Atlas** to store memory data.  

### 🔹 Step 1: Creating a Free MongoDB Atlas Account  
1. I went to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)  
2. Clicked **Get Started** → Selected **Shared (Free Tier)**  
3. Chose **AWS (us-east-1)** and clicked **Create Cluster**  
4. **Network Access** → Allowed `0.0.0.0/0` (For Development)  
5. **Created Database User** → Added a username & password  

### 🔹 Step 2: Getting the Connection String  
1. I went to **Database > Connect**  
2. Chose **Python** and copied the connection string  
3. Replaced `<username>` and `<password>` with my credentials  
4. Stored it in a `.env` file (Never commit this!)

```env
MONGO_URI = "mongodb+srv://<username>:<password>@cluster.mongodb.net/memoryRecallDB"
```

---

## 2️⃣ Setting Up AWS EC2 (Free Tier)  
I deployed my **FastAPI backend** on an **AWS EC2 instance (Free Tier).**  

### 🔹 Step 1: Creating an EC2 Instance  
1. I went to **AWS Console > EC2 > Launch Instance**  
2. Chose **Ubuntu 22.04 (Free Tier Eligible)**  
3. Selected **t2.micro (Free Tier)**  
4. **Key Pair**: Created a new key or used an existing one (`.pem` file)  
5. **Security Group**: Allowed  
   - **SSH (22)** for remote access  
   - **HTTP (80), HTTPS (443), Custom TCP (8000) for FastAPI**  
6. Clicked **Launch Instance**  

### 🔹 Step 2: Connecting to EC2  
I found my **EC2 Public IP** under **Instances > Public IPv4**  

Then I connected using SSH:  

```sh
ssh -i my-key.pem ubuntu@<EC2-PUBLIC-IP>
```

---

## 3️⃣ Installing Dependencies on EC2  
After SSH-ing into EC2:  

### 🔹 Step 1: Updating & Installing Essentials  
```sh
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
sudo apt install docker.io -y
```

### 🔹 Step 2: Cloning My GitHub Repository  
```sh
git clone https://github.com/<my-username>/AI-Memory-Recall.git
cd AI-Memory-Recall
```

### 🔹 Step 3: Installing Python Dependencies  
```sh
pip install -r requirements.txt
```

---

## 4️⃣ Running FastAPI Backend on EC2  
### 🔹 Step 1: Starting the FastAPI Server  
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
🚀 **FastAPI is running at:**  
```
http://<EC2-PUBLIC-IP>:8000/docs
```

### 🔹 Step 2: Testing API Endpoints  
I visited:  
```
http://<EC2-PUBLIC-IP>:8000/docs
```
Then tested `POST /store-memory` and `POST /ai-recall`.

---

## 5️⃣ Deploying FastAPI Using Docker & AWS ECR  
I containerized my FastAPI app and pushed it to **AWS ECR**.

### 🔹 Step 1: Creating an AWS ECR Repository  
```sh
aws ecr create-repository --repository-name ai-memory-recall
```

### 🔹 Step 2: Authenticating Docker to AWS ECR  
```sh
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com
```

### 🔹 Step 3: Building & Tagging the Docker Image  
```sh
docker build -t ai-memory .
docker tag ai-memory:latest <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/ai-memory-recall:latest
```

### 🔹 Step 4: Pushing to AWS ECR  
```sh
docker push <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/ai-memory-recall:latest
```

### 🔹 Step 5: Running the Container on EC2  
```sh
docker run -d -p 8000:8000 <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/ai-memory-recall:latest
```

---

## 6️⃣ Setting Up Streamlit Frontend  
I deployed the **Streamlit UI** to interact with the FastAPI backend.

### 🔹 Step 1: Cloning Repo & Installing Streamlit  
```sh
git clone https://github.com/<my-username>/AI-Memory-Recall.git
cd AI-Memory-Recall
pip install streamlit requests python-dotenv
```

### 🔹 Step 2: Running the Streamlit App Locally  
```sh
streamlit run app.py
```

### 🔹 Step 3: Deploying to Streamlit Cloud  
1. I went to **[Streamlit Cloud](https://streamlit.io/cloud)**  
2. Clicked **Deploy an App**  
3. Selected my GitHub repository  
4. Set **Secrets in Advanced Settings**:  
```toml
API_URL = "http://<EC2-PUBLIC-IP>:8000"
```
5. Clicked **Deploy**  
6. 🎉 **My app is live!**  

---

## 7️⃣ Troubleshooting  
### 🔹 Common Issues & Fixes  

| Issue | Fix |
|--------|------|
| MongoDB connection error | Checked `.env` file & whitelisted IPs in MongoDB Atlas |
| EC2 server not accessible | Ensured **Security Groups** allow **8000 port** |
| FastAPI not running | Used `docker ps` and restarted the container |
| Streamlit app crashes | Checked **Secrets** & `.env` for missing variables |
| Voice synthesis failed | Installed `ffmpeg`: `sudo apt install ffmpeg -y` |

---

## 🔥 Conclusion  
🚀 **I successfully deployed an AI-powered memory recall system!**  
✔ Stored thoughts  
✔ Retrieved memories using AI  
✔ Speech-to-text & text-to-speech  
✔ Fully deployed on **AWS EC2, AWS ECR, Docker & Streamlit**  

🙌 **If this helped, I’ll star my own repo on GitHub!**  

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
I can improve the **AI retrieval logic** by fine-tuning `main.py`.  
Example: Use **similarity search**, **semantic retrieval**, or **RAG-based embeddings** for **more precise memory recall.**  

---

🔥 **Now this README is exactly how I need it! It's in first-person, includes AWS ECR, and covers every detail of deployment.** I’ll just **copy-paste this into my `README.md` file** and I'm done! 🚀🔥

---

✅ **This is the FINAL README** that you should **copy-paste** into your repo! It is in **first-person**, **includes AWS ECR**, and **covers EVERYTHING you did** step by step. 🚀🔥
