
---

# ✍️ LinkedIn Post Generator

This project builds a **Streamlit web app** that generates professional and engaging LinkedIn posts using **Google Gemini**, **LangChain**, and **Streamlit**.

Simply provide a topic or idea, and the app will:

- Analyze your input
- Apply tone and formatting guidelines
- Generate a full-length LinkedIn post (150–300 words)
- Add relevant hashtags and structure

### 🚀 Features

- 🧠 Powered by Gemini 2.0 (via LangChain)
- 🗣️ Takes natural language topics as input
- ✍️ Generates professional LinkedIn-style posts
- 🔗 Adds hashtags and maintains tone consistency
- 🎨 Built with Streamlit for easy interaction

---

## 🔮 Future Improvements

- ✅ Add support for post formatting (bullets, bold)
- ✅ Option to select industry/voice style
- ✅ Export to LinkedIn directly via API (TBD)
- ✅ Deploy fully on Hugging Face or GCP
- ✅ Save generated posts in session history

---

## 🛠️ Setup

### 1. Install Dependencies

```bash
pip install streamlit langchain langchain-google-genai langchain_community pyngrok google-generativeai
```

### 2. Configure API Keys

In Colab, use:

```python
from google.colab import userdata
os.environ['GOOGLE_API_KEY'] = userdata.get('GEMINI_API_KEY')
os.environ['NGROK_AUTH_TOKEN'] = userdata.get('NGROK_API_KEY')
```

If running locally, you can set them via environment variables or a `.env` file.

---

## 🧱 Project Structure

```
.
├── linkedin_app.py       # Streamlit frontend and post generation logic
├── logs.txt              # Ngrok and Streamlit logs
└── README.md             # This documentation file
```

---

## 🧠 How It Works

- Prompts Gemini using LangChain for context-aware generation
- Prompts are structured to follow specific rules for tone and clarity
- Gemini returns a completed LinkedIn-style post
- Streamlit displays it in a user-friendly format

> Posts are ideal for professionals, thought leaders, or marketers who want to engage audiences with minimal effort.

---

## 🚀 Running the App (in Colab)

```bash
!streamlit run linkedin_app.py --server.port=8989 &>./logs.txt &
```

Expose it with Ngrok:

```python
from pyngrok import ngrok

ngrok.kill()  # Stop previous tunnels
ngrok.set_auth_token(userdata.get('NGROK_API_KEY'))
ngrok_tunnel = ngrok.connect(8989)
print("Streamlit App:", ngrok_tunnel.public_url)
```

---

## 🛑 Stop the App

```bash
ngrok.kill()
!ps -ef | grep streamlit
!sudo kill -9 <process_id>
```

---

## 🔁 Optional: Run Locally

1. Clone the repo

```bash
git clone https://github.com/your-username/linkedin-post-generator.git
cd linkedin-post-generator
```

2. Set environment variables:

```bash
export GOOGLE_API_KEY='your-gemini-key'
export NGROK_AUTH_TOKEN='your-ngrok-key'
```

3. Install and run:

```bash
pip install -r requirements.txt
streamlit run linkedin_app.py --server.port=8989
```

4. Optionally expose it:

```bash
ngrok http 8989
```

---

## 🤝 Contributing

Pull requests and suggestions are welcome! Feel free to fork the repo and help improve the app.

---

## 📫 Contact

Find my contact info in my GitHub profile.  
DMs are open for feedback or collaboration!

---

## 📜 License

This project is licensed under the MIT License.

---
