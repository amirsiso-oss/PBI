import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="יחידה 5: לספר את הסיפור", page_icon="🎨", layout="wide")

# CSS RTL
st.markdown("""
    <style>
    body { direction: rtl; text-align: right; }
    .stMarkdown, .stButton, .stRadio, .stSelectbox, .stExpander, .stDownloadButton, .stAlert { text-align: right; direction: rtl; }
    div[data-testid="stSidebar"] { text-align: right; direction: rtl; }
    h1, h2, h3, h4, p, li { text-align: right; }
    </style>
    """, unsafe_allow_html=True)

st.title("יחידה 5: אומנות הויזואליזציה 🎨")

with st.expander("עקרון הזהב: פחות זה יותר", expanded=True):
    st.write("המטרה של דשבורד היא לא להיות יפה, אלא להיות **מובן ב-5 שניות**.")

st.divider()

st.subheader("תרגיל: תקן את הדשבורד")
col1, col2 = st.columns(2)

with col1:
    st.error("❌ איך לא לעבוד")
    st.write("גרף עוגה עם 12 פרוסות (ערים).")
    # סימולציה של גרף רע (Dataframe רנדומלי)
    chart_data = pd.DataFrame(np.random.rand(12, 1), columns=["Events"])
    st.write("נסו להבין איזו עיר גדולה יותר: פרוסה 3 או פרוסה 7? זה בלתי אפשרי.")

with col2:
    st.success("✅ הפתרון הנכון")
    st.write("איזה גרף יתאים להשוואה בין 12 ערים?")
    viz_choice = st.radio("", ["גרף עוגה תלת מימד", "גרף עמודות (Bar Chart)", "כרטיסייה (Card)"])

if viz_choice == "גרף עמודות (Bar Chart)":
    st.bar_chart(chart_data)
    st.caption("הרבה יותר קל להשוות גבהים מאשר זוויות!")

st.download_button("💾 הורד קובץ PBIX התחלתי ליחידה זו", data="simulated", file_name="Stage_4_End.pbix")
