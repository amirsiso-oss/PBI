import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        /* --- ייבוא פונט --- */
        @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;600;800&display=swap');
        
        /* --- הגדרות בסיס (Root) --- */
        html, body, [class*="css"] {
            font-family: 'Assistant', sans-serif;
        }

        /* --- 1. טיפול בתוכן הראשי (Main Content) --- */
        /* זה תופס את כל הבלוק המרכזי ומיישר אותו לימין */
        .block-container {
            direction: rtl !important;
            text-align: right !important;
        }

        /* יישור פרטני לכל רכיבי הטקסט */
        p, div, h1, h2, h3, h4, h5, h6, .stMarkdown, .stButton, .stSelectbox, .stRadio, .stExpander, .stTextInput, .stAlert {
            text-align: right !important;
            direction: rtl !important;
        }

        /* --- 2. טיפול בסרגל הצד (Sidebar) - התיקון הקריטי --- */
        
        /* צבע רקע כהה */
        section[data-testid="stSidebar"] {
            background-color: #0F172A !important; /* כחול לילה */
            border-left: 1px solid #334155;
        }

        /* חוק גורף: כל טקסט בסרגל הצד חייב להיות בהיר */
        section[data-testid="stSidebar"] * {
            color: #F8FAFC !important; /* לבן/כסוף */
            text-align: right !important;
            direction: rtl !important;
        }

        /* תיקון ספציפי לקישורים בתפריט הניווט (שלא היו קריאים) */
        section[data-testid="stSidebar"] a {
            color: #F8FAFC !important;
        }
        
        /* תיקון ספציפי: שדות קלט בתוך הסרגל (כדי שלא יהיה טקסט לבן על רקע לבן בתוך תיבת טקסט) */
        section[data-testid="stSidebar"] input, 
        section[data-testid="stSidebar"] textarea, 
        section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] div {
            color: #0F172A !important; /* טקסט כהה בתוך שדות הקלדה */
            background-color: #FFFFFF !important;
        }

        /* --- 3. עיצוב אלמנטים כלליים --- */
        
        /* כותרות */
        h1 {
            color: #1E293B; /* צבע כותרת בתוכן הראשי */
            border-bottom: 2px solid #F59E0B;
            padding-bottom: 10px;
        }

        /* כרטיסיות מידע */
        .info-card {
            background-color: #F8FAFC;
            border-right: 4px solid #3B82F6;
            padding: 15px;
            border-radius: 6px;
            margin: 10px 0;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
            color: #334155 !important; /* טקסט כהה בתוך כרטיסייה */
            text-align: right !important;
        }
        
        .success-card {
            background-color: #ECFDF5;
            border-right: 4px solid #10B981;
            padding: 15px;
            border-radius: 6px;
            color: #064E3B !important;
            text-align: right !important;
        }
        
        .warning-card {
            background-color: #FEFCE8;
            border-right: 4px solid #F59E0B;
            padding: 15px;
            border-radius: 6px;
            color: #78350F !important;
            text-align: right !important;
        }

        /* כפתורים */
        .stButton > button {
            width: 100%;
            border-radius: 6px;
            border: 1px solid #CBD5E1;
            background-color: white;
            color: #0F172A !important; /* טקסט כהה בכפתור */
        }
        .stButton > button:hover {
            border-color: #F59E0B;
            background-color: #FFFBEB;
            color: #B45309 !important;
        }

        /* --- 4. חריגים (Ltr) --- */
        /* קוד חייב להישאר משמאל לימין */
        .stCode, code {
            direction: ltr !important;
            text-align: left !important;
        }

        /* הסתרת תפריט עליון */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        </style>
    """, unsafe_allow_html=True)