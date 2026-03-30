import streamlit as st
import pandas as pd

# إعداد الصفحة
st.set_page_config(page_title="Tourism AI Chatbot", layout="wide")

st.title("🌍 Tourism AI Chatbot")
st.write("Ask about any country and discover places ✈️")

# قراءة الداتا
data = pd.read_csv("tourism_dataset.csv")

# input
user_input = st.text_input("Enter a country:")

# البحث
if user_input:
    results = data[data["Country"].str.lower().str.contains(user_input.lower())]

    if not results.empty:
        st.success(f"Found places in {user_input.capitalize()} 👇")

        for i, row in results.iterrows():
            st.subheader(row["Location"])
            st.write(f"📍 Country: {row['Country']}")
            st.write(f"🏷️ Category: {row['Category']}")
            st.write(f"⭐ Rating: {row['Rating']}")
            st.divider()
    else:
        st.error("No results found 😅")