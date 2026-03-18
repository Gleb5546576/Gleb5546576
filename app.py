import streamlit as st

st.title("🤖 AI Генератор идей")

st.sidebar.title("Меню")
st.sidebar.write("Введите тему")

topic = st.text_input("Введите тему:")

if st.button("Сгенерировать"):
    if topic:
        st.write(f"Идеи по теме: {topic}")
        st.write("1. Создать приложение")
        st.write("2. Сделать сайт")
        st.write("3. Открыть бизнес")
    else:
        st.warning("Введите тему!")