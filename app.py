import streamlit as st
import requests

st.title("🤖 AI Генератор идей")

st.sidebar.title("Меню")
st.sidebar.write("Введите тему и получите идеи от AI")

topic = st.text_input("Введите тему:")

if st.button("Сгенерировать идеи"):
    
    if topic:
        url = "https://openrouter.ai/api/v1/chat/completions"
        
        headers = {
            "Authorization": "Bearer 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",
            "Content-Type": "application/json"
        }

        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": f"Придумай 5 идей на тему: {topic}"}
            ]
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            result = response.json()

            st.write(result["choices"][0]["message"]["content"])

        except:
            st.error("Ошибка при работе AI 😢")
    
    else:
        st.warning("Введите тему!")