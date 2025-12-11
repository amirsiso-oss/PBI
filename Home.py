import streamlit as st
import sys
import os

# ייבוא העיצוב (נשאר אותו עיצוב מקצועי שבחרנו)
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from utils import apply_custom_style

st.set_page_config(page_title="BI Compass", page_icon="🧭", layout="wide")
apply_custom_style()

st.title("BI Compass: המצפן לפרויקט הגמר 🧭")
st.caption("מערכת ליווי אינטראקטיבית לאנליסטים צעירים")

st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### ברוכים הבאים למדריך הצמוד שלכם.
    מערכת זו נועדה ללוות אתכם צעד אחר צעד בבניית פרויקט הגמר ב-Power BI, על בסיס הנתונים **שלכם**.
    
    אנחנו לא נתרגל כאן דוגמאות תיאורטיות.
    בכל שלב תקבלו את **הלוגיקה המדויקת**, את **קטעי הקוד (Snippets)** ואת **עקרונות הזהב** שאתם צריכים ליישם בקובץ שלכם.
    
    ### 🗺️ מפת הדרכים של הפרויקט:
    1.  **Modeling:** הפיכת המידע הגולמי למודל חכם (Star Schema).
    2.  **Base Measures:** בניית התשתית (אסור לגרור עמודות!).
    3.  **Ratios & Branching:** יצירת מדדים חכמים שמבוססים על הבסיס.
    4.  **Time Intelligence:** מסע בזמן (השוואה לשנה שעברה).
    5.  **Visualization:** הצגת הסיפור בצורה ויזואלית ומדויקת.
    """)

    st.markdown("""
    <div class="info-card">
        <b>איך עובדים עם המערכת?</b><br>
        פתחו את קובץ ה-Power BI שלכם במקביל לאתר זה.<br>
        עברו יחידה יחידה לפי הסדר, קראו את ההנחיה, ויישמו אותה מיד על הפרויקט שלכם.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("### 📌 עקרונות ברזל")
    st.markdown("""
    * **Don't Guess:** אל תנחשו. אם אתם לא מבינים למה מדד מסוים עובד, אל תתקדמו.
    * **Clean Code:** תנו שמות ברורים למדדים (באנגלית).
    * **Validation:** בדקו כל מספר שיוצא לכם.
    """)
    
    st.metric(label="שלבים לביצוע", value="5")

st.markdown("---")
st.success("👈 מוכנים להתחיל? גשו לתפריט הצד ובחרו בשלב הראשון: **Modeling**")