import streamlit as st

st.set_page_config(page_title="יחידה 3: המנוע (DAX)", page_icon="🧮", layout="wide")

# CSS RTL
st.markdown("""
    <style>
    body { direction: rtl; text-align: right; }
    .stMarkdown, .stButton, .stRadio, .stSelectbox, .stExpander, .stDownloadButton, .stAlert, .stCode { text-align: right; direction: rtl; }
    div[data-testid="stSidebar"] { text-align: right; direction: rtl; }
    h1, h2, h3, h4, p, li { text-align: right; }
    </style>
    """, unsafe_allow_html=True)

st.title("יחידה 3: המנוע הלוגי (DAX) 🧮")

# תיאוריה
with st.expander("📚 המחשבון הווירטואלי (Measure)", expanded=True):
    st.markdown("""
    באקסל, כשרוצים לחשב סכום, כותבים נוסחה והתוצאה נצרבת בתא.
    ב-Power BI, אנחנו יוצרים **Measure**.
    זוהי נוסחה ש"צפה באוויר". היא לא מחושבת עד שגוררים אותה לגרף, והתוצאה שלה משתנה לפי מה שהמשתמש בוחר (פילטרים).
    """)

st.divider()

# האתגר
st.subheader("האתגר: ספירת אירועים")
st.write("אנחנו רוצים לדעת כמה אירועי שריפה היו בסך הכל. בקובץ הנתונים, כל שורה היא אירוע.")

st.code("Total Incidents = ???", language="dax")

ans = st.radio("איזו פונקציה תבצע את העבודה?", 
               ["SUM(Events[EventID])", "COUNTROWS(Events)", "AVERAGE(Events[Damage])"])

if st.button("בדוק קוד"):
    if ans == "COUNTROWS(Events)":
        st.success("✅ נכון מאוד! אנחנו סופרים את השורות בטבלה. SUM היה מנסה לחבר את המזהים (ID) וזה חסר משמעות.")
    else:
        st.error("❌ לא מתאים. נסה לחשוב מה מייצג 'כמות אירועים' בטבלה שטוחה.")

st.info("💡 **טיפ:** תמיד תנו למדדים שמות באנגלית (כמו Total Sales) כדי שיהיה קל להשתמש בהם בנוסחאות אחרות.")

# נקודת שמירה
st.download_button("💾 הורד קובץ PBIX התחלתי ליחידה זו", data="simulated_content", file_name="Stage_2_End.pbix")