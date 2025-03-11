import streamlit as st
import requests
import os
import io
from dotenv import load_dotenv
from gtts import gTTS

# ✅ Load environment variables
load_dotenv()
API_URL = os.getenv("API_URL")

# ✅ Check if API_URL is set
if not API_URL:
    st.error("⚠️ API_URL is missing! Set it in `.env` or Streamlit Secrets.")
    st.stop()

# ✅ Set Page Config
st.set_page_config(
    page_title="AI Memory Recall",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ✅ Custom Styling
st.markdown("""
    <style>
        body { background-color: #0d1117; color: white; font-family: 'Arial', sans-serif; }
        .stTextInput input, .stTextArea textarea { background-color: #161b22; color: white; }
        .stButton button { background-color: #1f6feb; color: white; font-size: 16px; padding: 10px; width: 100%; }
        .stMarkdown h1 { font-size: 30px; font-weight: bold; text-align: center; }
        .stMarkdown p { font-size: 16px; color: #b0b3b8; text-align: center; }
        .memory-box { padding: 15px; background-color: #1e2a38; border-radius: 10px; color: white; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# ✅ Title & Description
st.markdown("<h1>AI Memory Recall System</h1>", unsafe_allow_html=True)
st.markdown("<p>Seamlessly store and recall thoughts using AI-powered memory retrieval.</p>", unsafe_allow_html=True)

# 📌 **Store New Memory**
st.subheader("Store New Memory")
memory_text = st.text_area("Enter something to store in memory:")

if st.button("Store Memory"):
    if memory_text.strip():
        response = requests.post(f"{API_URL}/store-memory", json={"query": memory_text.strip()})
        if response.status_code == 200:
            st.success("✅ Memory stored successfully!")
        else:
            st.error(f"⚠️ Error storing memory: {response.json()}")
    else:
        st.warning("❗ Please enter something to store.")

# 📌 **Recall Memory**
st.subheader("Recall a Memory")
query_text = st.text_input("Ask a question:")

if st.button("Recall Memory"):
    if query_text.strip():
        response = requests.post(f"{API_URL}/ai-recall", json={"query": query_text.strip()})
        if response.status_code == 200:
            recalled_memories = response.json().get("recalled_memory", "No memory found.")

            if recalled_memories:
                # ✅ Format response for clean display
                formatted_response = recalled_memories.replace("\n", "\n\n")
                st.markdown(f"<div class='memory-box'>🧠 AI Response:<br><br>{formatted_response}</div>", unsafe_allow_html=True)

                # ✅ **Generate Voice Output (In-Memory)**
                tts = gTTS(text=recalled_memories, lang="en")
                audio_buffer = io.BytesIO()
                tts.write_to_fp(audio_buffer)
                audio_buffer.seek(0)

                # ✅ **Play the Audio**
                st.subheader("🔊 Voice Output")
                st.audio(audio_buffer, format="audio/mp3")
            else:
                st.warning("⚠️ No memory found.")
        else:
            st.error("⚠️ Error fetching response from AI.")
    else:
        st.warning("❗ Please enter a question.")

# ✅ Footer
st.markdown("<p style='text-align: center; font-size: 14px;'>⚡ Powered by AI Memory Recall System - Designed for Professionals</p>", unsafe_allow_html=True)
