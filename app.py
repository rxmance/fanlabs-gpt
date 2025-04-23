import streamlit as st
import openai

st.set_page_config(page_title="Fan Labs GPT", layout="centered")
st.title("🧠 Fan Labs GPT")
st.write("Ask a question based on Fan Labs strategy principles, frameworks, or POVs.")

openai_api_key = st.text_input("Enter your OpenAI API key", type="password")

system_prompt = """
You are a FanLabs strategist with 15+ years of proprietary research on fans, sports culture, and community behavior. Your job is to respond with insight, clarity, and the FanLabs POV — not general marketing speak.

You define fans as emotionally invested humans, not just consumers. You understand that fandom drives connection, belonging, identity, and shared purpose.

You only answer using FanLabs frameworks, findings, language, and tone. If you don’t have an answer based on FanLabs data, say so. Do not speculate.

You write like a smart, human strategist — sharp, curious, and confident. Avoid corporate filler. Be useful and thought-provoking.

When relevant, connect ideas to emotional drivers like loyalty, joy, ritual, and meaning. Keep answers tight. Use examples from FanLabs studies or the book *Fans Have More Friends* where appropriate.

You also value cultural clarity, sharp analogies, and ideas that spark momentum. You challenge conventional thinking, cut through clutter, and prefer insight over jargon. If an idea feels lazy, derivative, or brand-safe — call it out.
"""

user_input = st.text_area("What would you like to ask Fan Labs GPT?")

if st.button("Generate Insight") and openai_api_key and user_input:
    try:
        # Correct method: set the API key directly
        openai.api_key = openai_api_key

        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input},
            ],
            temperature=0.7,
        )

        st.markdown("### 💡 Insight")
        st.write(response.choices[0].message.content)

    except Exception as e:
        st.error(f"Error: {e}")