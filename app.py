import streamlit as st

# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Arslan Ahmad | AI Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# 2. MASTERPIECE ENGINE (PRECISION CSS & FLEXBOX SYSTEM)
# ============================================================

st.markdown(
    """
    <style>
    /* --------------------------------------------------------
       A. CORE ENGINE & RESET
       -------------------------------------------------------- */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Space+Grotesk:wght@500;600;700&display=swap');

    html, body, .stApp {
        background-color: #08080E !important;
        color: #9CA3AF !important;
        font-family: 'Inter', -apple-system, sans-serif !important;
        -webkit-font-smoothing: antialiased;
    }

    /* Headings */
    h1, h2, h3, h4, .font-heading {
        font-family: 'Space Grotesk', sans-serif !important;
        color: #F9FAFB !important;
        letter-spacing: -0.03em !important;
    }

    code, .font-mono {
        font-family: 'JetBrains Mono', monospace !important;
    }

    /* Remove Streamlit Default Elements */
    header[data-testid="stHeader"], 
    footer, 
    #MainMenu, 
    .stDeployButton {
        display: none !important;
    }

    /* Precise Margin Elimination */
    .block-container {
        max-width: 1200px !important;
        padding-top: 1.5rem !important;
        padding-bottom: 4rem !important;
        padding-left: 1.5rem !important;
        padding-right: 1.5rem !important;
    }

    /* --------------------------------------------------------
       B. FLOATING HEADER & NAVBAR
       -------------------------------------------------------- */
    .nav-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 12px 24px;
        background: rgba(15, 17, 26, 0.75);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        margin-bottom: 3.5rem;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
    }

    .brand-logo {
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        font-size: 1.1rem;
        color: #FFFFFF;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .brand-dot {
        width: 8px;
        height: 8px;
        background: #00E5FF;
        border-radius: 50%;
        box-shadow: 0 0 12px #00E5FF;
    }

    .status-pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 4px 12px;
        border-radius: 20px;
        background: rgba(16, 185, 129, 0.1);
        border: 1px solid rgba(16, 185, 129, 0.25);
        color: #34D399;
        font-size: 0.75rem;
        font-weight: 500;
    }

    .pulse-dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background-color: #10B981;
        box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7);
        animation: pulse-ring 2s infinite;
    }

    @keyframes pulse-ring {
        0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
        70% { transform: scale(1); box-shadow: 0 0 0 6px rgba(16, 185, 129, 0); }
        100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
    }

    /* Nav PageLink Overrides */
    [data-testid="stPageLink-NavLink"] {
        height: 38px !important;
        padding: 0 16px !important;
        border-radius: 8px !important;
        background: transparent !important;
        border: 1px solid transparent !important;
        color: #9CA3AF !important;
        font-weight: 500 !important;
        font-size: 0.875rem !important;
        transition: all 0.2s ease !important;
    }

    [data-testid="stPageLink-NavLink"]:hover {
        color: #F9FAFB !important;
        background: rgba(255, 255, 255, 0.05) !important;
        border-color: rgba(255, 255, 255, 0.08) !important;
    }

    [data-testid="stPopover"] > div > button {
        height: 38px !important;
        background: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 8px !important;
        color: #D1D5DB !important;
        font-size: 0.875rem !important;
        font-weight: 500 !important;
    }

    [data-testid="stPopoverBody"] {
        background: #0E1017 !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
    }

    /* --------------------------------------------------------
       C. HERO SECTION
       -------------------------------------------------------- */
    .hero-container {
        padding: 2rem 0 3rem 0;
        text-align: left;
    }

    .hero-eyebrow {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 4px 12px;
        border-radius: 6px;
        background: rgba(99, 102, 241, 0.1);
        border: 1px solid rgba(99, 102, 241, 0.25);
        color: #818CF8;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.8rem;
        margin-bottom: 1.5rem;
    }

    .hero-title {
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 700;
        line-height: 1.1;
        margin-bottom: 1.25rem;
        background: linear-gradient(180deg, #FFFFFF 0%, #9CA3AF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        font-size: 1.125rem;
        line-height: 1.6;
        color: #9CA3AF;
        max-width: 680px;
        margin-bottom: 2rem;
    }

    /* --------------------------------------------------------
       D. METRICS BAR
       -------------------------------------------------------- */
    .metrics-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 16px;
        margin-bottom: 4rem;
    }

    .metric-card {
        background: rgba(15, 17, 26, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 12px;
        padding: 20px;
        transition: border-color 0.2s ease;
    }

    .metric-card:hover {
        border-color: rgba(99, 102, 241, 0.3);
    }

    .metric-value {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2rem;
        font-weight: 700;
        color: #F9FAFB;
        margin-bottom: 4px;
    }

    .metric-label {
        font-size: 0.85rem;
        color: #6B7280;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* --------------------------------------------------------
       E. PROJECT CARDS GRID
       -------------------------------------------------------- */
    .section-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 1.5rem;
        padding-bottom: 0.75rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    }

    .section-title {
        font-size: 1.5rem;
        color: white;
        font-weight: 700;
    }

    .project-card {
        background: rgba(15, 17, 26, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.07);
        border-radius: 14px;
        padding: 24px;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .project-card:hover {
        transform: translateY(-3px);
        border-color: rgba(0, 229, 255, 0.3);
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
    }

    .card-tag {
        display: inline-block;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        color: #00E5FF;
        background: rgba(0, 229, 255, 0.08);
        padding: 3px 10px;
        border-radius: 4px;
        margin-bottom: 12px;
    }

    .card-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: #F9FAFB;
        margin-bottom: 8px;
    }

    .card-desc {
        font-size: 0.9rem;
        color: #9CA3AF;
        line-height: 1.5;
        margin-bottom: 16px;
    }

    .card-footer {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding-top: 16px;
        border-top: 1px solid rgba(255, 255, 255, 0.04);
    }

    .tech-pill {
        font-size: 0.75rem;
        color: #6B7280;
        background: rgba(255, 255, 255, 0.03);
        padding: 2px 8px;
        border-radius: 4px;
    }

    /* --------------------------------------------------------
       F. TECH STACK MATRIX
       -------------------------------------------------------- */
    .stack-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
        gap: 12px;
        margin-top: 1rem;
    }

    .stack-item {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 8px;
        padding: 12px;
        text-align: center;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.85rem;
        color: #D1D5DB;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# 3. ROUTE DEFINITIONS
# ============================================================

home_page = st.Page("apps/Home/home.py", title="Home", default=True)
cnn_page = st.Page("apps/Rose Type Classifier/rose_classifier.py", title="Rose Classifier")
resnet50_food_page = st.Page("apps/ResNet Food Image Classification/ResNet50_Food_Classifier.py", title="Food Classifier")
movie_review_page = st.Page("apps/Movie Review Sentiment/movie_review_sentiment.py", title="Movie Sentiment")
fake_news_page = st.Page("apps/Fake News Prediction/fake_news_prediction.py", title="Fake News Detector")

pg = st.navigation(
    [home_page, cnn_page, resnet50_food_page, movie_review_page, fake_news_page],
    position="hidden"
)


# ============================================================
# 4. CUSTOM NAVBAR LAYOUT
# ============================================================

nav_cols = st.columns([3, 1.2, 1.2, 1.5, 2.5], vertical_alignment="center")

with nav_cols[0]:
    st.markdown(
        """
        <div class="brand-logo">
            <div class="brand-dot"></div>
            ARSLAN AHMAD
        </div>
        """,
        unsafe_allow_html=True
    )

with nav_cols[1]:
    st.page_link(home_page, label="Home")


with nav_cols[2]:
    with st.popover("All Models ▾", use_container_width=True):
        st.caption("Computer Vision")
        st.page_link(cnn_page, label="Rose Classifier")
        st.page_link(resnet50_food_page, label="ResNet-50 Food")
        st.divider()
        st.caption("Natural Language Processing")
        st.page_link(movie_review_page, label="Movie Sentiment")
        st.page_link(fake_news_page, label="Fake News")

with nav_cols[4]:
    st.markdown(
        """
        <div style="display: flex; justify-content: flex-end;">
            <div class="status-pill">
                <span class="pulse-dot"></span> Available for Projects
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)


# ============================================================
# 5. HOMEPAGE CONTENT (IF ACTIVE)
# ============================================================

# Check if current routed page is Home
if pg == home_page:

    # --- HERO SECTION ---
    st.markdown(
        """
        <div class="hero-container">
            <div class="hero-eyebrow">
                <span>AI / ML & COMPUTER VISION ENGINEER</span>
            </div>
            <h1 class="hero-title">
                Deploying Production-Grade Deep Learning Models.
            </h1>
            <p class="hero-subtitle">
                Specialized in high-performance Computer Vision architectures and Natural Language Processing pipelines. Focused on model accuracy, inference optimization, and seamless web deployment.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- METRICS STRIP ---
    st.markdown(
        """
        <div class="metrics-grid">
            <div class="metric-card">
                <div class="metric-value">04</div>
                <div class="metric-label">Deployed AI Models</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">ResNet-50</div>
                <div class="metric-label">Vision Backbone</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">98.4%</div>
                <div class="metric-label">Top Classifier Accuracy</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">< 120ms</div>
                <div class="metric-label">Avg Inference Time</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- FEATURED COMPUTER VISION MODELS ---
    st.markdown(
        """
        <div class="section-header">
            <div class="section-title">COMPUTER VISION</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    cv_col1, cv_col2 = st.columns(2)

    with cv_col1:
        st.markdown(
            """
            <div class="project-card">
                <div>
                    <span class="card-tag">CNN / PyTorch</span>
                    <div class="card-title">Rose Type Classifier</div>
                    <div class="card-desc">
                        Custom Convolutional Neural Network trained to classify multi-class rose varieties with visual feature extraction and confidence scoring.
                    </div>
                </div>
                <div class="card-footer">
                    <span class="tech-pill">Image Classification</span>
                    <span class="tech-pill">CNN</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.page_link(cnn_page, label="Launch Model Demo →", use_container_width=True)

    with cv_col2:
        st.markdown(
            """
            <div class="project-card">
                <div>
                    <span class="card-tag">Transfer Learning</span>
                    <div class="card-title">ResNet-50 Food Classifier</div>
                    <div class="card-desc">
                        Deep residual network fine-tuned on food datasets to recognize diverse culinary items with high top-1 and top-5 accuracy metrics.
                    </div>
                </div>
                <div class="card-footer">
                    <span class="tech-pill">ResNet-50</span>
                    <span class="tech-pill">PyTorch</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.page_link(resnet50_food_page, label="Launch Model Demo →", use_container_width=True)

    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

    # --- FEATURED NLP MODELS ---
    st.markdown(
        """
        <div class="section-header">
            <div class="section-title">NATURAL LANGUAGE PROCESSING</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    nlp_col1, nlp_col2 = st.columns(2)

    with nlp_col1:
        st.markdown(
            """
            <div class="project-card">
                <div>
                    <span class="card-tag">NLP / Sentiment</span>
                    <div class="card-title">Movie Review Sentiment Engine</div>
                    <div class="card-desc">
                        Text classification engine evaluating film reviews to extract polarity, sentiment scores, and key text vectors in real-time.
                    </div>
                </div>
                <div class="card-footer">
                    <span class="tech-pill">TF-IDF</span>
                    <span class="tech-pill">Scikit-Learn</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.page_link(movie_review_page, label="Launch Model Demo →", use_container_width=True)

    with nlp_col2:
        st.markdown(
            """
            <div class="project-card">
                <div>
                    <span class="card-tag">NLP / Classification</span>
                    <div class="card-title">Fake News Detector</div>
                    <div class="card-desc">
                        Predictive model analyzing headline syntactical patterns and textual probability to flag unverified news articles.
                    </div>
                </div>
                <div class="card-footer">
                    <span class="tech-pill">Logistic Reg</span>
                    <span class="tech-pill">Text Mining</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.page_link(fake_news_page, label="Launch Model Demo →", use_container_width=True)

    # --- TECH STACK MATRIX ---
    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="section-header">
            <div class="section-title">TECHNICAL STACK</div>
        </div>
        <div class="stack-grid">
            <div class="stack-item">PyTorch</div>
            <div class="stack-item">TensorFlow</div>
            <div class="stack-item">OpenCV</div>
            <div class="stack-item">Scikit-Learn</div>
            <div class="stack-item">ResNet-50</div>
            <div class="stack-item">Streamlit</div>
            <div class="stack-item">Python</div>
            <div class="stack-item">Git / Docker</div>
        </div>
        """,
        unsafe_allow_html=True
    )

else:
    # Render the sub-page route when clicked
    pg.run()