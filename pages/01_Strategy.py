import streamlit as st
import pandas as pd
import io

# הגדרת הדף
st.set_page_config(page_title="יחידה 1: אסטרטגיה", page_icon="🎯", layout="wide")

# הזרקת CSS ליישור לימין (RTL)
st.markdown("""
    <style>
    body { direction: rtl; text-align: right; }
    .stMarkdown, .stButton, .stRadio, .stSelectbox, .stExpander, .stDownloadButton { text-align: right; direction: rtl; }
    div[data-testid="stSidebar"] { text-align: right; direction: rtl; }
    h1, h2, h3, p { text-align: right; }
    </style>
    """, unsafe_allow_html=True)

st.title("יחידה 1: להבין את המטרה 🎯")

# --- חלק א: התיאוריה ---
with st.expander("📚 רגע של תיאוריה: מה זה KPI?", expanded=False):
    st.markdown("""
    **KPI (מדד ביצוע מרכזי)** הוא המצפן שלנו.
    
    דמיינו מד מהירות באוטו: הוא אומר לכם כרגע מה המצב והאם צריך להאיץ או להאט.
    כך גם בעסקים - KPI חייב להיות:
    1. **מדיד** (מספר, לא תחושה).
    2. **השוואתי** (ביחס ליעד או לעבר).
    3. **מניע לפעולה** (אם הוא אדום - עושים משהו).
    """)

# --- חלק ב: הסיפור ---
st.write("---")
col1, col2 = st.columns([1, 3]) # חלוקה לעמודות: תמונה וטקסט

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/2991/2991108.png", width=100) # אייקון כבאי

with col2:
    st.info("""
    **הודעה דחופה מנציב הכבאות:**
    "צוות יקר, אני טובע באקסלים! שולחים לי דוחות עם 50,000 שורות ואני לא מוצא את הידיים והרגליים.
    יש לי תחושה שזמני התגובה בפריפריה מתארכים, אבל אין לי הוכחה. תבנו לי משהו פשוט."
    """)

# --- חלק ג: האתגר ---
st.write("### 🧠 האתגר שלך:")
st.write("מתוך הבקשה של הנציב, איזה מדד הכי קריטי להציג לו בדשבורד?")

choice = st.radio(
    label="בחר את התשובה:",
    options=[
        "א. כמות האירועים הכוללת בכל עיר (ספירה רגילה)",
        "ב. רשימת כל השריפות שהיו השבוע (טבלה מפורטת)",
        "ג. זמן הגעה ממוצע - השוואה בין מחוזות (KPI)"
    ],
    index=None
)

section_completed = False # משתנה למעקב אם עברו את השלב

if st.button("בדוק תשובה"):
    if "ג." in str(choice):
        st.success("✅ בול! זה המדד. הנציב דיבר על 'זמני תגובה' ועל 'השוואה'. זה המצפן שלנו.")
        section_completed = True
    elif "א." in str(choice):
        st.error("❌ לא מדויק. לדעת 'כמה שריפות היו' זה נחמד (Volume), אבל זה לא אומר כלום על הביצועים שלנו (Performance).")
    elif "ב." in str(choice):
        st.error("❌ טעות. רשימות זה לא דשבורד. מנהל לא יכול לקרוא 1000 שורות. הוא צריך סיכום.")
    else:
        st.warning("נא לבחור תשובה.")

# --- חלק ד: המעבר לפרקטיקה (רק אם ענו נכון) ---
if section_completed:
    st.write("---")
    st.header("📥 השלב הבא: קבלת הנתונים")
    st.write("עכשיו כשיש לנו שאלת מחקר ('מה זמן ההגעה?'), אנחנו צריכים נתונים.")
    
    st.warning("⚠️ אזהרה: ה-IT שלח לנו קובץ נתונים גולמי. הוא מכיל טעויות, תאריכים הפוכים ולכלוך. זה מכוון.")

    # --- יצירת דאטה מזויף בזמן אמת (Python Power!) ---
    # כאן אנחנו מדגימים את הכוח של פייתון לייצר את הקובץ להורדה
    df = pd.DataFrame({
        'Date': ['01/01/2023', '02/15/2023', '03/30/2023'],
        'City': ['Tel Aviv', 'Haifa', 'Jerusalem'],
        'Response_Time': ['12 min', '8', 'unknown'] # לכלוך בכוונה
    })
    
    # המרת הדאטה לקובץ CSV בזיכרון
    csv_buffer = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="הורד את קובץ הנתונים (Fire_Data_Raw.csv)",
        data=csv_buffer,
        file_name="Fire_Data_Raw.csv",
        mime="text/csv",
    )
    
    st.info("👉 לאחר ההורדה, עברו ליחידה 2 בתפריט (עדיין בבנייה) כדי להתחיל לנקות את הנתונים.")