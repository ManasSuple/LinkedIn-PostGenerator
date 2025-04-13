import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate

# Set page config
st.set_page_config(page_title="LinkedIn Post Generator", page_icon="💼")

st.title("💼 LinkedIn Post Generator")

# System prompt defining behavior
system_prompt = """You are a professional LinkedIn post generator.
Your task is to create engaging, professional posts for LinkedIn based on the topic provided by the user.

Follow these guidelines:
- Keep posts between 150-300 words
- Include relevant hashtags (3-5)
- Maintain a professional but conversational tone
- Focus on providing value to the reader
- Structure posts with short paragraphs for readability
- Avoid clickbait and exaggerated claims

The user will provide a topic or idea for the post."""

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model='gemini-2.0-flash-thinking-exp-01-21',
    temperature=0.7,
    convert_system_message_to_human=True
)

# Create prompt template
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{user_input}")
])

# App UI
st.markdown("### ✍️ Generate professional LinkedIn posts with AI")
st.markdown("Enter a topic or idea to get a LinkedIn post tailored to your needs.")

user_input = st.text_area(
    "What would you like to post about?",
    placeholder="Example: Sharing my thoughts on the future of AI in healthcare",
    height=100
)

if st.button("Generate Post"):
    if user_input:
        with st.spinner("Creating your LinkedIn post..."):
            messages = prompt_template.format_messages(user_input=user_input)
            response = llm.invoke(messages)

            st.markdown("### 🎯 Your LinkedIn Post:")
            st.markdown(response.content)

            st.markdown("---")
            st.success("Copy this post and share it on LinkedIn!")
    else:
        st.error("Please enter a topic for your LinkedIn post.")
