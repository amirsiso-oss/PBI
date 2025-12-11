import streamlit as st

st.set_page_config(page_title="יחידה 4: לוגיקה מתקדמת", page_icon="🧠", layout="wide")

# CSS RTL
st.markdown("""
    <style>
    body { direction: rtl; text-align: right; }
    .stMarkdown, .stButton, .stRadio, .stSelectbox, .stExpander, .stDownloadButton, .stAlert, .stCode { text-align: right; direction: rtl; }
    div[data-testid="stSidebar"] { text-align: right; direction: rtl; }
    h1, h2, h3, h4, p, li { text-align: right; }
    </style>
    """, unsafe_allow_html=True)

st.title("יחידה 4: לשלוט בזמן ובמרחב 🧠")

st.markdown("""
הנציב שאל: **"האם המצב החמיר לעומת שנה שעברה?"**
בשביל זה צריך "מכונת זמן".
""")

# סימולטור CALCULATE
st.subheader("מעבדת ה-CALCULATE")
st.write("הפונקציה `CALCULATE` היא היחידה שיכולה לשנות את חוקי המשחק (לנטרל פילטרים או להוסיף חדשים).")

st.code("""
Incidents LY = 
CALCULATE(
    [Total Incidents], 
    SAMEPERIODLASTYEAR( 'Events'[Date] )
)
""", language="dax")

st.write("מה תעשה הנוסחה הזו אם נציג אותה בגרף של שנת **2023**?")

logic_check = st.selectbox("בחר את הפרשנות הנכונה:", 
                           ["תציג את נתוני 2023", "תציג את נתוני 2022 (תזיז את הזמן אחורה)", "תציג שגיאה"])

if st.button("הפעל הגיון"):
    if "2022" in logic_check:
        st.success("🎯 בדיוק! היא לוקחת את ההקשר הנוכחי (2023) ומסיטה אותו שנה אחורה.")
    else:
        st.error("❌ טעות. הפונקציה SAMEPERIODLASTYEAR נועדה בדיוק כדי 'לזוז' בזמן.")

st.download_button("💾 הורד קובץ PBIX התחלתי ליחידה זו", data="simulated", file_name="Stage_3_End.pbix")
