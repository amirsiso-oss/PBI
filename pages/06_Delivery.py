import streamlit as st

st.set_page_config(page_title="יחידה 6: רגע האמת", page_icon="🏆", layout="wide")

# CSS RTL
st.markdown("""
    <style>
    body { direction: rtl; text-align: right; }
    .stMarkdown, .stButton, .stRadio, .stSelectbox, .stExpander, .stDownloadButton, .stTextInput { text-align: right; direction: rtl; }
    div[data-testid="stSidebar"] { text-align: right; direction: rtl; }
    h1, h2, h3, h4, p, li { text-align: right; }
    </style>
    """, unsafe_allow_html=True)

st.title("יחידה 6: רגע האמת 🏆")

st.markdown("""
### ישיבת ההנהלה התחילה.
הנציב מסתכל על הדשבורד שבנית ושואל:
**"אז איפה הבעיה? איפה אנחנו צריכים להוסיף רחפנים?"**
""")

st.info("השתמשו בדשבורד שבניתם כדי לענות.")

# טופס מסכם
conclusion = st.text_input("המסקנה שלך (למשל: מחוז צפון, שעות הצהריים):")

if st.button("הגש המלצה"):
    if len(conclusion) > 5:
        st.balloons()
        st.success(f"תודה רבה! ההמלצה '{conclusion}' נרשמה והועברה לביצוע.")
        st.markdown("### 🎓 כל הכבוד! סיימת את הסימולטור.")
        st.write("הוכחת יכולת לקחת נתונים גולמיים ולהפוך אותם לתובנה עסקית.")
    else:
        st.warning("נא לכתוב תשובה מפורטת יותר.")