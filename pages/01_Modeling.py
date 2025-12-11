import streamlit as st
import sys
import os
import graphviz

# ייבוא העיצוב
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import apply_custom_style

st.set_page_config(page_title="Modeling", page_icon="🏗️", layout="wide")
apply_custom_style()

# --- כותרת ופתיח אישי ---
st.title("שלב 1: ארכיטקטורת המידע (Modeling)")
st.caption("מטבלה שטוחה למודל כוכב | הנדסת נתונים")

st.markdown("""
### שלום, הגעתם לרגע האמת של הפרויקט.
עד עכשיו עבדתם קשה כדי להשיג נתונים. עכשיו אתם מסתכלים על טבלה ענקית ועמוסה, ואולי שואלים: 
*"איך אני אמור להוציא מזה תובנות?"*

אל דאגה. זה בדיוק השלב שבו אנחנו הופכים **"רשימת מכולת"** למערכת חכמה.
אנחנו הולכים לפרק את הטבלה הגדולה שלכם לגורמים (ישויות), כדי שיהיה לכם קל ומהיר לעבוד בהמשך.
זהו שלב **קריטי**. אם המודל ייבנה נכון עכשיו - כל המשך הפרויקט יזרום חלק.
""")

st.divider()

# --- חלק 1: למה אנחנו עושים את זה? ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### ❌ המצב המצוי: טבלה שטוחה")
    st.markdown("""
    <div class="warning-card">
        <b>הבעיה:</b> כפילות עצומה.
        כמו בקבלה של סופר - בכל שורה של "חלב" חוזרת הכתובת של הסופר ושם הקופאי.
        זה מכביד על המערכת ומקשה על ניתוח.
    </div>
    """, unsafe_allow_html=True)
    
    # דיאגרמה שטוחה
    flat = graphviz.Digraph()
    flat.attr(rankdir='TB', size='3')
    flat.node('A', 'טבלה ענקית ומבולגנת\n[תאריך | לקוח | עיר | מוצר | מכירות...]', shape='note', style='filled', fillcolor='#FEE2E2', fontname="Assistant")
    st.graphviz_chart(flat)

with col2:
    st.markdown("#### ✅ המצב הרצוי: מודל כוכב")
    st.markdown("""
    <div class="success-card">
        <b>הפתרון:</b> הפרדת כוחות.
        נשים את האירועים במרכז, ואת התיאורים (לקוחות, ערים) מסביב.
    </div>
    """, unsafe_allow_html=True)

    # דיאגרמת כוכב משופרת (גיאומטרית)
    star = graphviz.Digraph(engine='neato') # שימוש במנוע שמבין מיקומים
    star.attr(overlap='false', splines='ortho')
    
    # מיקומים קבועים ליצירת צורת כוכב/משולש ברור
    star.node('F', 'FACT\n(טבלת העובדות)', shape='rect', style='filled', fillcolor='#DBEAFE', pos='0,0!', width='1.5', height='1')
    star.node('D1', 'DIM\n(לקוחות)', shape='ellipse', style='filled', fillcolor='#FEF9C3', pos='0,1.5!')
    star.node('D2', 'DIM\n(ערים)', shape='ellipse', style='filled', fillcolor='#FEF9C3', pos='2,-1!')
    star.node('D3', 'DIM\n(מוצרים)', shape='ellipse', style='filled', fillcolor='#FEF9C3', pos='-2,-1!')
    
    star.edge('D1', 'F')
    star.edge('D2', 'F')
    star.edge('D3', 'F')
    
    st.graphviz_chart(star)

st.divider()

# --- חלק 2: המושג שבלעדיו אי אפשר (Unique Key) ---
st.markdown("### 2. תנאי סף: המזהה הייחודי (Unique Key)")

st.markdown("""
לפני שמתחילים לחתוך, חייבים להבין חוק אחד פשוט:
**בטבלת התיאור (Dim) שאנחנו יוצרים, אסור שאותו ערך יופיע פעמיים.**
""")

# הסבר ויזואלי להשוואה
col_k1, col_k2 = st.columns(2)
with col_k1:
    st.error("לא תקין (Duplicated)")
    st.code("""
    עיר       |  אזור
    ------------------
    תל אביב   |  מרכז
    תל אביב   |  מרכז  <-- כפילות!
    חיפה      |  צפון
    """, language="text")
    st.caption("במצב כזה, Power BI לא ייתן לכם לחבר את הטבלאות.")
    
with col_k2:
    st.success("תקין (Unique Key)")
    st.code("""
    עיר       |  אזור
    ------------------
    תל אביב   |  מרכז
    חיפה      |  צפון
    ירושלים   |  הר
    """, language="text")
    st.caption("כל עיר מופיעה בדיוק פעם אחת. זהו מזהה ייחודי.")

st.divider()

# --- חלק 3: המחולל האישי (The Builder) ---
st.markdown("### 3. יצירת הטבלה האישית שלך")
st.markdown("""
אנחנו לא עובדים "באוויר". כדי לקבל הוראות מדויקות, כתוב את שם הישות שאתה עובד עליה כרגע.
(טיפ: בצע את התהליך הזה בנפרד לכל נושא - פעם ללקוחות, פעם לסניפים וכו').
""")

# קלט יחיד וממוקד
user_entity = st.text_input("על איזו ישות אנחנו עובדים עכשיו? (למשל: סוגי עבירות)", placeholder="הקלד כאן...")

# קביעת השם לשימוש בהוראות
target_name = user_entity if user_entity else "שם_הישות_שלכם"
clean_name = f"Dim_{target_name.replace(' ', '_')}"

if user_entity:
    st.markdown(f"""
    <div class="info-card">
        מעולה. ההוראות למטה עודכנו עבור הטבלה: <b>{target_name}</b>.
    </div>
    """, unsafe_allow_html=True)

# --- המדריך המעשי (Power Query) ---
st.markdown(f"#### 🛠️ הביצוע ב-Power Query:")

# צעד 1
col_s1_txt, col_s1_img = st.columns([2, 1])
with col_s1_txt:
    st.markdown("**1️⃣ יצירת העתק חי (Reference)**")
    st.write("אנחנו לא נוגעים בטבלה המקורית. אנחנו יוצרים 'השתקפות' שלה.")
    st.info("עמדו על הטבלה הראשית בצד שמאל -> **קליק ימני** -> **Reference**.")
with col_s1_img:
    st.warning("GIF: Right Click -> Reference")

st.markdown("---")

# צעד 2
col_s2_txt, col_s2_img = st.columns([2, 1])
with col_s2_txt:
    st.markdown(f"**2️⃣ בחירת עמודות ה-{target_name}**")
    st.write(f"השאירו בטבלה החדשה רק את העמודות שמתארות את {target_name}.")
    st.info("סמנו את העמודות הרצויות (עם Ctrl) -> **קליק ימני על הכותרת** -> **Remove Other Columns**.")
with col_s2_img:
     st.warning("GIF: Remove Other Columns")

st.markdown("---")

# צעד 3
col_s3_txt, col_s3_img = st.columns([2, 1])
with col_s3_txt:
    st.markdown("**3️⃣ יצירת המזהה הייחודי (השלב הקריטי!)**")
    st.write("כדי למנוע את השגיאה שראינו למעלה, חייבים לנקות כפילויות.")
    st.error(f"חובה: עמדו על העמודה המזהה של {target_name} -> **קליק ימני** -> **Remove Duplicates**.")
with col_s3_img:
    st.warning("GIF: Remove Duplicates")

st.markdown("---")

# צעד 4
col_s4_txt, col_s4_img = st.columns([2, 1])
with col_s4_txt:
    st.markdown("**4️⃣ סיום וטעינה**")
    st.write("תנו לטבלה שם מקצועי כדי שתמצאו אותה אח\"כ.")
    st.info(f"1. שנו את שם הטבלה בצד ימין ל-**{clean_name}**.\n2. לחצו למעלה בצד שמאל על **Close & Apply**.")
with col_s4_img:
    st.warning("GIF: Rename & Close")

st.divider()

# --- חלק 4: הרכבת המודל (Model View) - הוחזר במלואו ---
st.markdown("### 4. מחברים את החלקים (Model View)")
st.markdown("עכשיו כשיש לכם טבלאות נפרדות, הגיע הזמן לחבר אותן. זה השלב שבו הכוכב נבנה.")

# מדריך ויזואלי למיקום הכפתורים
st.markdown("#### 🧭 איפה אני נמצא?")
st.write("הסתכלו על הצד השמאלי ביותר של המסך ב-Power BI. יש שם שלושה אייקונים קטנים.")
st.info("לחצו על האייקון השלישי (התחתון) שנראה כמו **תרשים זרימה** או רשת קווים.")



st.markdown("#### 🔗 פעולת החיבור:")
col_final_1, col_final_2 = st.columns(2)

with col_final_1:
    st.markdown(f"""
    **מה גוררים לאן?**
    1. אתרו את הטבלה החדשה שיצרתם (**{clean_name}**).
    2. אתרו את הטבלה המרכזית הגדולה.
    3. גררו את העמודה המשותפת (למשל *שם {target_name}*) מהטבלה הקטנה --> אל העמודה המקבילה בטבלה הגדולה.
    """)

with col_final_2:
    st.markdown("""
    <div class="info-card">
        <b>טיפ למקצוענים:</b><br>
        תמיד תגררו מהטבלה הקטנה (Dim) אל הגדולה (Fact). זה עוזר ל-Power BI להבין את כיוון הסינון.
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- חלק 5: הבוט המאבחן ---
st.markdown("### 5. בדיקת תקינות המודל 🕵️‍♂️")
st.write("הסתכלו על הקו שנוצר בין הטבלאות. איך הוא נראה?")

status = st.radio("בחרו את התרחיש שמופיע אצלכם:", 
                  ["קו עם הספרה 1 וכוכבית (*)", 
                   "קו עם כוכבית (*) בשני הצדדים", 
                   "קו מקווקו (לא רציף)"], 
                  index=None,
                  label_visibility="collapsed")

if status == "קו עם הספרה 1 וכוכבית (*)":
    st.success("✅ **מצוין!** המודל תקין (One-to-Many). אתם יכולים להמשיך לישות הבאה או לעבור ליחידה הבאה.")
    st.balloons()

elif status == "קו עם כוכבית (*) בשני הצדדים":
    st.error("🛑 **שגיאת Many-to-Many**")
    st.write("זה אומר שיש כפילויות בטבלת ה-Dim שלכם. שכחתם לעשות **Remove Duplicates** ב-Power Query.")
    st.code("Relationship has cardinality Many-Many...", language="text")

elif status == "קו מקווקו (לא רציף)":
    st.warning("⚠️ **הקו אינו פעיל**")
    st.write("זה קורה בדרך כלל כשיש כבר קשר אחר פעיל שמתנגש, או בעיה בנתונים. נסו למחוק ולחבר מחדש.")