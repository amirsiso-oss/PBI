import streamlit as st

# הגדרת דף הבית
st.set_page_config(
    page_title="פרויקט מבט לאש - לובי",
    page_icon="🚒",
    layout="wide"
)

# הזרקת CSS ליישור לימין (RTL) - חובה בכל דף
st.markdown("""
    <style>
    body { direction: rtl; text-align: right; }
    .stMarkdown, .stButton, .stRadio, .stSelectbox, .stExpander { text-align: right; direction: rtl; }
    div[data-testid="stSidebar"] { text-align: right; direction: rtl; }
    h1, h2, h3, p { text-align: right; }
    </style>
    """, unsafe_allow_html=True)

# כותרת ראשית
st.title("🚒 סימולטור הכשרה: פרויקט 'מבט לאש'")
st.caption("🟢 גרסה 1.1 | המערכת עודכנה בהצלחה בזמן אמת")

# פתיח
st.markdown("""
### ברוכים הבאים לצוות הדאטה של נציבות הכבאות וההצלה.

בקורס הזה אנחנו לא נלמד "איפה ללחוץ ב-Power BI". את זה יש ביוטיוב.
כאן אנחנו נלמד איך **לחשוב** כמו אנליסטים, איך **לפתור בעיות**, ואיך להפוך נתונים להחלטות מצילות חיים.

#### איך זה עובד?
1.  👈 **התפריט בצד ימין:** מאפשר לעבור בין יחידות הלימוד.
2.  💾 **קבצים להורדה:** בכל יחידה תקבלו נתונים "מלוכלכים" להתמודד איתם.
3.  🧠 **אתגרים:** המערכת תציג לכם דילמות בזמן אמת.
""")

st.info("👈 כדי להתחיל, לחצו על **'Strategy'** בתפריט הניווט בצד.")

# קרדיט קטן למטה
st.divider()
st.caption("פותח עבור פרויקט גמר יב' - סימולטור מבוסס Streamlit")