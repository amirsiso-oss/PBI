import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        /* --- ייבוא פונט --- */
        @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;600;800&display=swap');
        
        /* --- הגדרות גלובליות חזקות (Iron Dome RTL) --- */
        html, body, [class*="css"] {
            font-family: 'Assistant', sans-serif;
            direction: rtl;
        }

        /* יישור לימין של כל רכיבי הטקסט */
        .stMarkdown, .stButton, .stSelectbox, .stRadio, .stExpander, .stTextInput, .stText, p, div {
            text-align: right !important;
            direction: rtl !important;
        }

        /* --- תיקון ספציפי לכותרות (הבעיה שציינת) --- */
        h1, h2, h3, h4, h5, h6 {
            text-align: right !important;
            direction: rtl !important;
            font-family: 'Assistant', sans-serif !important;
        }
        
        /* כותרת ראשית מעוצבת */
        h1 {
            color: #1E293B;
            border-bottom: 2px solid #F59E0B;
            padding-bottom: 10px;
            font-weight: 800;
        }

        /* --- סרגל צד (Sidebar) --- */
        [data-testid="stSidebar"] {
            background-color: #0F172A;
            border-left: 1px solid #334155;
        }
        
        /* תיקון יישור טקסט בתוך הסרגל */
        [data-testid="stSidebar"] .stMarkdown, 
        [data-testid="stSidebar"] h1, 
        [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] div {
            color: #E2E8F0 !important;
            text-align: right !important;
            direction: rtl !important;
        }

        /* --- כרטיסיות מידע --- */
        .info-card {
            background-color: #F8FAFC;
            border-right: 4px solid #3B82F6;
            padding: 15px;
            border-radius: 6px;
            margin: 10px 0;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
            color: #334155;
            text-align: right !important;
        }
        
        .success-card {
            background-color: #ECFDF5;
            border-right: 4px solid #10B981;
            padding: 15px;
            border-radius: 6px;
            color: #064E3B;
            text-align: right !important;
        }
        
        .warning-card {
            background-color: #FEFCE8;
            border-right: 4px solid #F59E0B;
            padding: 15px;
            border-radius: 6px;
            color: #78350F;
            text-align: right !important;
        }

        /* --- כפתורים --- */
        .stButton > button {
            width: 100%;
            border-radius: 6px;
            font-weight: 600;
            background-color: white;
            border: 1px solid #CBD5E1;
            color: #0F172A;
            transition: all 0.2s;
        }
        .stButton > button:hover {
            border-color: #F59E0B;
            background-color: #FFFBEB;
            color: #B45309;
        }

        /* --- חריגים: קוד וגרפים (חייבים להישאר LTR) --- */
        .stCode, .stCodeBlock {
            direction: ltr !important;
            text-align: left !important;
        }
        
        /* הסתרת תפריט עליון של סטרימליט */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        </style>
    """, unsafe_allow_html=True)