import streamlit as st
import openai

st.set_page_config(page_title="Fan Labs GPT", layout="centered")
st.title("🧠 Fan Labs GPT")
st.write("Ask a question based on Fan Labs strategy principles, frameworks, or POVs.")

openai_api_key = st.text_input("Enter your OpenAI API key", type="password")

system_prompt = """
You are a strategic thinker trained in the Fan Labs methodology. You generate smart, punchy, and culturally aware insights about fan engagement, community, and brand strategy.
"""

user_input = st.text_area("What would you like to ask Fan Labs GPT?")

if st.button("Generate Insight") and openai_api_key and user_input:
    try:
        openai_client = openai.OpenAI(api_key=openai_api_key)

        response = openai_client.chat.completions.create(
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