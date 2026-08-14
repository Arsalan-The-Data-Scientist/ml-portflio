import streamlit as st

# 1. Must be the FIRST Streamlit command
st.set_page_config(
    page_title="Arslan Ahmad | AI Portfolio",
    page_icon="⚡",
    layout="wide"
)

# 2. Global CSS (Applies to all pages now)
st.markdown("""
<style>
/* Import Poppins Font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

/* Apply Poppins globally */
* {
    font-family: 'Poppins', sans-serif !important;
}

/* Hide default Streamlit UI */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Dark background for the whole app */
.stApp {
    background: #09090B;
}

/* Width and padding */
.block-container {
    max-width: 1300px;
    padding-top: 0.5rem;
    padding-bottom: 1rem;
}

/* Style the top navigation buttons */
[data-testid="stPageLink-NavLink"] {
    text-align: center;
    justify-content: center;
    transition: all 0.3s ease;
    background : none;
}
[data-testid="stPageLink-NavLink"]:hover {
    transform: translateY(-2px);
    background : none;
}
</style>
""", unsafe_allow_html=True)

# 3. Define pages
home_page = st.Page("apps/home.py", title="Home", default=True)
cnn_page = st.Page("apps/rose_classifier.py", title="Rose Classifier")
movie_review_sentiment_page = st.Page("apps/movie_review_sentiment.py", title="Movie Review Sentiment")

# 4. Hide the default sidebar menu by setting position="hidden"
pg = st.navigation([home_page, cnn_page, movie_review_sentiment_page], position="hidden")

# 5. Create the Custom Top Navigation Bar
st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)
nav_cols = st.columns([1, 1.5, 2, 5.5]) # Adjusted proportions for button lengths and right spacing

with nav_cols[0]:
    st.page_link(home_page)
with nav_cols[1]:
    st.page_link(cnn_page)
with nav_cols[2]:
    st.page_link(movie_review_sentiment_page)

# 6. Run selected page
pg.run()