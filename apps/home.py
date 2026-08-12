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
/* Import Poppins Font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

/* Apply Poppins globally */
* {
    font-family: 'Poppins', sans-serif !important;
}

/* Hide Streamlit UI */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Main app */
.stApp {
    background: #09090B;
}

/* Width */
.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* Hero Section */
.hero {
    padding-top: 100px;
    padding-bottom: 80px;
    animation: fadeIn 1.2s ease-in-out;
}

.hero-tag {
    display: inline-block;
    border: 1px solid rgba(139, 92, 246, 0.3);
    background: rgba(139, 92, 246, 0.05);
    border-radius: 999px;
    padding: 8px 20px;
    color: #C4B5FD;
    font-size: 14px;
    font-weight: 500;
    margin-bottom: 30px;
    box-shadow: 0 0 20px rgba(139, 92, 246, 0.1);
}

.hero-title {
    color: white;
    font-size: 72px;
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -2px;
}

.text-gradient {
    background: linear-gradient(90deg, #3B82F6, #8B5CF6, #EC4899);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    color: #A1A1AA;
    font-size: 20px;
    margin-top: 30px;
    max-width: 750px;
    line-height: 1.8;
    font-weight: 300;
}

/* Buttons */
.button-row {
    margin-top: 40px;
    display: flex;
    gap: 15px;
}

.primary-btn {
    display: inline-block;
    background: linear-gradient(90deg, #3B82F6, #8B5CF6);
    color: white !important;
    text-decoration: none !important;
    padding: 14px 32px;
    border-radius: 12px;
    font-weight: 600;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(139, 92, 246, 0.3);
}

.primary-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(139, 92, 246, 0.5);
}

.secondary-btn {
    display: inline-block;
    border: 1px solid #27272A;
    background: rgba(255,255,255,0.02);
    color: white !important;
    text-decoration: none !important;
    padding: 14px 32px;
    border-radius: 12px;
    font-weight: 600;
    transition: all 0.3s ease;
}

.secondary-btn:hover {
    border-color: #52525B;
    background: rgba(255,255,255,0.05);
    transform: translateY(-2px);
}

/* Sections */
.section-title {
    color: white;
    font-size: 32px;
    font-weight: 700;
    margin-top: 80px;
    margin-bottom: 30px;
    display: flex;
    align-items: center;
    gap: 15px;
}

.section-title::after {
    content: "";
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, #27272A, transparent);
}

/* Cards (Projects) */
.card {
    background: #111113;
    border: 1px solid #27272A;
    border-radius: 20px;
    padding: 35px;
    min-height: 240px;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: linear-gradient(90deg, #3B82F6, #8B5CF6);
    opacity: 0;
    transition: opacity 0.3s ease;
}

.card:hover {
    border-color: #3f3f46;
    transform: translateY(-5px);
    box-shadow: 0 10px 30px -10px rgba(139, 92, 246, 0.15);
}

.card:hover::before {
    opacity: 1;
}

.card-title {
    color: white;
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 15px;
}

.card-text {
    color: #A1A1AA;
    line-height: 1.8;
    font-weight: 300;
}

/* Metrics */
.metric {
    background: linear-gradient(180deg, #111113 0%, #09090B 100%);
    border: 1px solid #27272A;
    border-radius: 20px;
    padding: 30px;
    text-align: center;
    transition: all 0.3s ease;
}

.metric:hover {
    border-color: #3B82F6;
    background: rgba(59, 130, 246, 0.02);
}

.metric-number {
    background: linear-gradient(90deg, #fff, #A1A1AA);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 48px;
    font-weight: 800;
    margin-bottom: 5px;
}

.metric-label {
    color: #8B5CF6;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-size: 14px;
}

/* Skills */
.skill-pill {
    display: inline-block;
    border: 1px solid #27272A;
    background: #111113;
    color: #D4D4D8;
    border-radius: 999px;
    padding: 10px 22px;
    margin: 6px;
    font-weight: 500;
    font-size: 15px;
    transition: all 0.3s ease;
}

.skill-pill:hover {
    border-color: #8B5CF6;
    background: rgba(139, 92, 246, 0.1);
    color: white;
    transform: translateY(-2px);
}

/* About Box */
.about-box {
    background: linear-gradient(145deg, #111113 0%, #09090B 100%);
    border: 1px solid #27272A;
    border-radius: 20px;
    padding: 40px;
    color: #A1A1AA;
    line-height: 2.0;
    font-size: 18px;
    font-weight: 300;
}

.about-box span {
    color: white;
    font-weight: 500;
}

/* Animations */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HERO
# ==========================================

hero_html = """
<div class="hero">
    <div class="hero-tag">⚡ AI Engineer • Machine Learning • Deep Learning</div>
    <div class="hero-title">
        Building <span class="text-gradient">AI Products</span><br>
        That Solve<br>
        Real Problems.
    </div>
    <div class="hero-subtitle">
        Data Science student focused on Machine Learning, Computer Vision, and Natural Language Processing. Building practical AI systems using modern tools and production-ready workflows.
    </div>
    <div class="button-row">
        <a href="#featured-projects" class="primary-btn">View Projects</a>
        <a href="https://github.com/arsalan-the-data-scientist" target="_blank" class="secondary-btn">GitHub Profile</a>
    </div>
</div>
"""
st.markdown(hero_html, unsafe_allow_html=True)

# ==========================================
# STATS
# ==========================================

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('<div class="metric"><div class="metric-number">2</div><div class="metric-label">Projects</div></div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="metric"><div class="metric-number">2</div><div class="metric-label">Models Built</div></div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="metric"><div class="metric-number">2</div><div class="metric-label">Datasets</div></div>', unsafe_allow_html=True)

# ==========================================
# PROJECTS
# ==========================================

st.markdown('<div id="featured-projects" class="section-title">Featured Projects</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">Rose Classification System 🌹</div>
        <div class="card-text">Deep CNN model built with PyTorch for flower classification using advanced image augmentation and transfer learning techniques to achieve high accuracy.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">Spam Email Detector 🛡️</div>
        <div class="card-text">NLP application utilizing TF-IDF, intelligent feature engineering, and robust machine learning algorithms to accurately classify and filter malicious emails.</div>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# SKILLS
# ==========================================

st.markdown('<div class="section-title">Technology Stack</div>', unsafe_allow_html=True)

skills = [
    "Python", "PyTorch", "Machine Learning", "Deep Learning",
    "NLP", "Computer Vision", "SQL", "Pandas",
    "NumPy", "Scikit-Learn", "Power BI", "Streamlit"
]

html = '<div style="display:flex; flex-wrap:wrap;">'
for skill in skills:
    html += f'<span class="skill-pill">{skill}</span>'
html += '</div>'

st.markdown(html, unsafe_allow_html=True)

# ==========================================
# ABOUT
# ==========================================

st.markdown('<div class="section-title">About</div>', unsafe_allow_html=True)

st.markdown("""
<div class="about-box">
    I am a Data Science student with a strong interest in <span>Machine Learning</span>, <span>Deep Learning</span>, <span>Computer Vision</span>, and <span>Natural Language Processing</span>.<br><br>
    My focus is on building practical AI applications, training predictive models, and deploying solutions that solve real-world problems. I thrive on translating raw data into actionable insights and intelligent systems.
</div>
""", unsafe_allow_html=True)