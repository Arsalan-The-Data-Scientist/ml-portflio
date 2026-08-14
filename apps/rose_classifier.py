import streamlit as st

# ==========================================
# PAGE STYLES
# ==========================================

st.markdown("""
<style>

/* Page Header */
.page-title {
    text-align: center;
    color: white;
    font-size: 48px;
    font-weight: 800;
    margin-bottom: 10px;
}

.page-subtitle {
    text-align: center;
    color: #A1A1AA;
    font-size: 18px;
    margin-bottom: 40px;
}

/* Native Streamlit Container Styling */
[data-testid="stVerticalBlockBorderWrapper"] {
    border: 1px solid #27272A !important;
    border-radius: 24px !important;
    padding: 25px !important;
    background: #111113 !important;
    min-height: 550px !important;
}

/* Upload Box */
[data-testid="stFileUploader"] {
    border: 2px dashed #8B5CF6;
    border-radius: 24px;
    padding: 2rem;
    background: linear-gradient(
        135deg,
        rgba(59,130,246,0.05),
        rgba(139,92,246,0.05)
    );
}

/* Hover Effect */
[data-testid="stFileUploader"]:hover {
    border-color: #A78BFA;
    box-shadow: 0 0 25px rgba(139,92,246,0.15);
}

/* Hide uploader label */
[data-testid="stFileUploader"] label {
    display: none;
}

/* Upload button */
[data-testid="stFileUploader"] section button {
    background: linear-gradient(
        90deg,
        #3B82F6,
        #8B5CF6
    ) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
}

.section-title {
    color: white;
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 20px;
}

/* Placeholder */
.placeholder-box {
    height: 50px;
    border: 1px dashed #27272A;
    border-radius: 16px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #71717A;
    text-align: center;
    font-size: 16px;
}

/* ==========================================
   IMAGE SIZING & CENTERING
========================================== */

/* Center the image container and lock its height */
[data-testid="stImage"] {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 350px; /* Matches placeholder height so layout doesn't jump */
}

/* Constrain the actual image size & enforce aspect ratio */
[data-testid="stImage"] img {
    border-radius: 16px;
    max-width: 100% !important;
    max-height: 350px !important; /* Smaller fixed size */
    width: auto !important;
    height: auto !important;
    object-fit: contain !important; /* Maintains true aspect ratio */
}

/* Reduce top padding */
.block-container {
    padding-top: 1rem;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# PAGE HEADER
# ==========================================

st.markdown("""
<div class="page-title">
    CNN Rose Classifier 🌹
</div>

<div class="page-subtitle">
    Upload a flower image and let the model classify it.
</div>
""", unsafe_allow_html=True)

# ==========================================
# TWO COLUMN LAYOUT
# ==========================================

left_col, right_col = st.columns([1, 1])

# ==========================================
# LEFT SIDE - UPLOADER
# ==========================================

with left_col:
    with st.container(border=True):

        uploaded_file = st.file_uploader(
            "",
            type=["jpg", "jpeg", "png"],
            label_visibility="collapsed"
        )

# ==========================================
# RIGHT SIDE - PREVIEW
# ==========================================

with right_col:
    with st.container(border=True):

        if uploaded_file is not None:
            # use_container_width is removed so CSS handles the constraints
            st.image(uploaded_file)
        else:
            st.markdown("""
            <div class="placeholder-box">
                Upload an image to see preview
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# MODEL INFERENCE SECTION
# ==========================================

if uploaded_file is not None:
    st.markdown("<br>", unsafe_allow_html=True)

    # Example:
    # prediction = predict(uploaded_file)
    # st.metric("Prediction", prediction)