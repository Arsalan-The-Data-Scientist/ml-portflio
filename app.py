import streamlit as st

# Must be first Streamlit command
st.set_page_config(
    page_title="My ML Portfolio",
    page_icon="🚀"
)

# Define pages
cnn_page = st.Page("apps/rose_classifier.py", title="CNN Image Classifier",icon="🖼️")
home_page = st.Page("apps/home.py", title="Home", icon="🏠")

pg = st.navigation([
    home_page,
    cnn_page
])


# Run selected page
pg.run()