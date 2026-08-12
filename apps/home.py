import streamlit as st

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Arslan Ahmad | AI Portfolio",
    page_icon="⚡",
    layout="wide"
)

# ==========================================
# STYLES
# ==========================================

st.markdown("""
<style>

/* Hide Streamlit UI */

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Main app */

.stApp{
    background:#09090B;
}

/* Width */

.block-container{
    max-width:1200px;
    padding-top:2rem;
    padding-bottom:4rem;
}

/* Hero */

.hero{
    padding-top:120px;
    padding-bottom:120px;
}

.hero-tag{
    display:inline-block;

    border:1px solid #27272A;

    border-radius:999px;

    padding:8px 16px;

    color:#A1A1AA;

    font-size:14px;

    margin-bottom:30px;
}

.hero-title{
    color:white;

    font-size:78px;

    font-weight:800;

    line-height:1.0;

    letter-spacing:-4px;
}

.hero-subtitle{
    color:#A1A1AA;

    font-size:22px;

    margin-top:30px;

    max-width:750px;

    line-height:1.7;
}

/* Buttons */

.button-row{
    margin-top:40px;
}

.primary-btn{
    display:inline-block;

    background:white;

    color:black;

    padding:14px 26px;

    border-radius:12px;

    font-weight:600;

    margin-right:15px;
}

.secondary-btn{
    display:inline-block;

    border:1px solid #27272A;

    color:white;

    padding:14px 26px;

    border-radius:12px;

    font-weight:600;
}

/* Sections */

.section-title{
    color:white;

    font-size:36px;

    font-weight:700;

    margin-top:80px;

    margin-bottom:30px;
}

/* Cards */

.card{
    background:#111113;

    border:1px solid #27272A;

    border-radius:20px;

    padding:30px;

    min-height:260px;

    transition:all .25s ease;
}

.card:hover{
    border-color:#52525B;

    transform:translateY(-3px);
}

.card-title{
    color:white;

    font-size:24px;

    font-weight:700;

    margin-bottom:15px;
}

.card-text{
    color:#A1A1AA;

    line-height:1.8;
}

/* Metrics */

.metric{
    background:#111113;

    border:1px solid #27272A;

    border-radius:20px;

    padding:30px;
}

.metric-number{
    color:white;

    font-size:42px;

    font-weight:800;
}

.metric-label{
    color:#A1A1AA;
}

/* Skills */

.skill-pill{
    display:inline-block;

    border:1px solid #27272A;

    color:#D4D4D8;

    border-radius:999px;

    padding:10px 18px;

    margin:6px;
}

/* Divider */

.line{
    height:1px;
    background:#27272A;
    margin-top:60px;
    margin-bottom:60px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HERO
# ==========================================

st.markdown('<div class="hero"><div class="hero-tag">AI Engineer • Machine Learning • Deep Learning</div><div class="hero-title">Building AI Products<br>That Solve<br>Real Problems.</div><div class="hero-subtitle">Data Science student focused on Machine Learning, Computer Vision and Natural Language Processing. Building practical AI systems using modern tools and production-ready workflows.</div></div>', unsafe_allow_html=True)

# ==========================================
# STATS
# ==========================================

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('<div class="metric"><div class="metric-number">10+</div><div class="metric-label">Projects</div></div>', unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric">
        <div class="metric-number">20+</div>
        <div class="metric-label">Models Built</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric">
        <div class="metric-number">15+</div>
        <div class="metric-label">Datasets</div>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# PROJECTS
# ==========================================

st.markdown(
    '<div class="section-title">Featured Projects</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card"><div class="card-title">Rose Classification System</div><div class="card-text">Deep CNN model built with PyTorch for flower classification using image augmentation and transfer learning.</div></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><div class="card-title">Spam Email Detector</div><div class="card-text">NLP application using TF-IDF, feature engineering and machine learning for email classification.</div></div>', unsafe_allow_html=True)

# ==========================================
# SKILLS
# ==========================================

st.markdown(
    '<div class="section-title">Technology Stack</div>',
    unsafe_allow_html=True
)

skills = [
    "Python",
    "PyTorch",
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "Computer Vision",
    "SQL",
    "Pandas",
    "NumPy",
    "Scikit-Learn",
    "Power BI",
    "Streamlit"
]

html = ""

for skill in skills:
    html += f'<span class="skill-pill">{skill}</span>'

st.markdown(html, unsafe_allow_html=True)

# ==========================================
# ABOUT
# ==========================================

st.markdown(
    '<div class="section-title">About</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div style="
background:#111113;
border:1px solid #27272A;
border-radius:20px;
padding:35px;
color:#A1A1AA;
line-height:1.9;
">

I am a Data Science student with a strong interest in
Machine Learning, Deep Learning, Computer Vision and
Natural Language Processing.

My focus is on building practical AI applications,
training predictive models and deploying solutions
that solve real-world problems.

</div>
""", unsafe_allow_html=True)