import streamlit as st

# --- הגדרת הדף ---
st.set_page_config(
    page_title="Data Analyst Simulator",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- פונקציית העיצוב החדשה (נשמור אותה כאן ונשתמש בה בכל דף) ---
def apply_custom_style():
    st.markdown("""
        <style>
        /* יישור לימין גלובלי */
        body, .stMarkdown, .stButton, .stSelectbox, .stRadio { direction: rtl; text-align: right; }
        
        /* הסתרת התפריט של סטרימליט למעלה למראה נקי */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* עיצוב כותרות - נקי וחד */
        h1 {
            font-family: 'Segoe UI', sans-serif;
            color: #1F2937;
            font-weight: 700;
            padding-bottom: 10px;
            border-bottom: 2px solid #F2C811; /* פס צהוב דק מתחת לכותרת */
        }
        
        h2, h3 {
            color: #374151;
            font-family: 'Segoe UI', sans-serif;
        }

        /* כרטיסיות מידע במקום אימוג'ים */
        .info-card {
            background-color: #F3F4F6;
            border-right: 4px solid #3B82F6; /* פס כחול */
            padding: 15px;
            border-radius: 4px;
            margin-bottom: 15px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }

        .success-card {
            background-color: #ECFDF5;
            border-right: 4px solid #10B981; /* פס ירוק */
            padding: 15px;
            border-radius: 4px;
            color: #065F46;
        }

        /* כפתורים מרובעים ומקצועיים במקום מעוגלים */
        .stButton > button {
            width: 100%;
            border-radius: 4px;
            border: 1px solid #D1D5DB;
            background-color: white;
            color: #1F2937;
            font-weight: 500;
            transition: all 0.2s;
        }
        
        .stButton > button:hover {
            border-color: #F2C811;
            color: black;
            background-color: #FEFCE8;
        }

        /* תיקון ליישור סרגל צד */
        [data-testid="stSidebar"] {
            background-color: #111827; /* סרגל צד כהה מאוד ומקצועי */
        }
        [data-testid="stSidebar"] * {
            color: #E5E7EB !important; /* טקסט בהיר בסרגל */
            direction: rtl;
            text-align: right;
        }
        </style>
    """, unsafe_allow_html=True)

apply_custom_style()

# --- תוכן דף הבית בעיצוב החדש ---

# כותרת ללא אימוג'ים
st.markdown("# מערכת הכשרה: ניתוח נתונים ו-BI")
st.caption("מערך כבאות והצלה לישראל | מחלקת דאטה")

st.markdown("---")

# שימוש ב-Columns ליצירת גריד נקי
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### ברוכים הבאים לסימולטור")
    st.markdown("""
    מטרת המערכת היא להכשיר אנליסטים לפתרון בעיות עסקיות מורכבות באמצעות נתונים.
    התהליך מדמה פרויקט מלא מקצה לקצה ("End-to-End"), משלב קבלת הדרישה ועד להצגת המסקנות להנהלה.
    
    **עקרונות עבודה:**
    * **Data First:** קודם מבינים את הנתונים, אחר כך בונים גרפים.
    * **Business Logic:** הטכנולוגיה משרתת את הצורך העסקי.
    * **Precision:** דיוק לפני יופי.
    """)
    
    # דוגמה לשימוש ב"כרטיסייה" מקצועית במקום אימוג'י
    st.markdown("""
    <div class="info-card">
        <b>סטטוס מערכת:</b> יחידות 1-6 זמינות לתרגול.<br>
        אנא בחרו את היחידה הרצויה מתפריט הניווט בצד ימין.
    </div>
    """, unsafe_allow_html=True)

with col2:
    # אזור מטריקות (נראה כמו דשבורד אמיתי)
    st.metric(label="יחידות להשלמה", value="6")
    st.metric(label="רמת קושי", value="מתקדם")
    st.metric(label="גרסת סימולטור", value="v2.0 Pro")

st.markdown("---")
st.button("התחל תרגול ביחידה 1")