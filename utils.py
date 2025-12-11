import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        /* --- הגדרות גלובליות --- */
        @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;700&display=swap');
        
        body, .stMarkdown, .stButton, .stSelectbox, .stRadio, .stExpander { 
            direction: rtl; 
            text-align: right; 
            font-family: 'Assistant', sans-serif; /* פונט מקצועי ונקי */
        }

        /* --- סרגל צד (Sidebar) מקצועי --- */
        [data-testid="stSidebar"] {
            background-color: #0F172A; /* כחול-לילה עמוק */
            border-left: 1px solid #334155;
        }
        [data-testid="stSidebar"] * {
            color: #E2E8F0 !important; /* טקסט כסוף */
        }
        
        /* --- כותרות --- */
        h1 {
            color: #1E293B;
            border-bottom: 2px solid #F59E0B; /* כתום-זהב עדין */
            padding-bottom: 10px;
            font-weight: 800;
        }
        h2, h3 { color: #334155; }

        /* --- כרטיסיות מידע (במקום אימוג'ים) --- */
        .info-card {
            background-color: #F8FAFC;
            border-right: 4px solid #3B82F6; /* כחול */
            padding: 15px;
            border-radius: 6px;
            margin: 10px 0;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
            color: #334155;
        }
        
        .warning-card {
            background-color: #FEFCE8;
            border-right: 4px solid #F59E0B; /* כתום */
            padding: 15px;
            border-radius: 6px;
            margin: 10px 0;
            color: #78350F;
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
        </style>
    """, unsafe_allow_html=True)
    
    # הסתרת אלמנטים מיותרים של סטרימליט
    st.markdown("<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>", unsafe_allow_html=True)