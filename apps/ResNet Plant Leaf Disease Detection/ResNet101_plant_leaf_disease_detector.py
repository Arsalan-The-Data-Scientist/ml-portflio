import streamlit as st
import torch
from torchvision import transforms, models
import torch.nn as nn
from PIL import Image
from pathlib import Path
import base64
from io import BytesIO
import re

# ============================================================
# 1. MODEL PATH & CONFIG
# ============================================================
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "plantvillage_resnet101.pth"


# ============================================================
# 2. CUSTOM CSS (SIDE-BY-SIDE EQUAL HEIGHT CARDS)
# ============================================================

st.markdown(
    """
    <style>
    /* Card Container Base */
    .panel-header {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 0.95rem;
        font-weight: 600;
        color: #F9FAFB;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* Target File Uploader Dropzone Height */
    [data-testid="stFileUploader"] {
        width: 100% !important;
    }

    [data-testid="stFileUploaderDropzone"] {
        background: rgba(15, 17, 26, 0.6) !important;
        border: 1.5px dashed rgba(255, 255, 255, 0.15) !important;
        border-radius: 14px !important;
        padding: 1.5rem 1rem !important;
        min-height: 260px !important;
        height: 260px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        transition: all 0.25s ease !important;
    }

    [data-testid="stFileUploaderDropzone"]:hover {
        border-color: #00E5FF !important;
        background: rgba(0, 229, 255, 0.03) !important;
    }

    /* Rendered Image Preview Frame */
    .preview-card, .placeholder-card {
        width: 100%;
        height: 260px;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: rgba(15, 17, 26, 0.3);
    }

    .preview-card {
        border: 1px solid rgba(255, 255, 255, 0.1);
        overflow: hidden;
    }

    .placeholder-card {
        border: 1.5px dashed rgba(255, 255, 255, 0.08);
        flex-direction: column;
        color: #6B7280;
        font-size: 0.875rem;
    }

    .preview-card img {
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
        padding: 8px;
    }

    /* Results Card & Progress Meters */
    .result-badge {
        background: rgba(16, 185, 129, 0.08);
        border: 1px solid rgba(16, 185, 129, 0.25);
        color: #34D399;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.4rem;
        font-weight: 700;
        padding: 16px 20px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .prob-bar-container {
        margin-bottom: 12px;
    }

    .prob-label {
        display: flex;
        justify-content: space-between;
        font-size: 0.85rem;
        color: #D1D5DB;
        margin-bottom: 4px;
        font-family: 'JetBrains Mono', monospace;
    }

    .prob-bar-bg {
        width: 100%;
        height: 8px;
        background: rgba(255, 255, 255, 0.06);
        border-radius: 4px;
        overflow: hidden;
    }

    .prob-bar-fill {
        height: 100%;
        background: linear-gradient(90deg, rgba(0, 229, 255, 0.2) 0%, rgba(0, 229, 255, 0.8) 100%);
        border-radius: 4px;
    }

    /* Classify Button & Header Button Styling */
    .stButton > button {
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 8px !important;
        padding: 8px 12px !important;
        border-radius: 6px !important;
        background: rgba(0, 229, 255, 0.08) !important;
        border: 1px solid rgba(0, 229, 255, 0.2) !important;
        color: #00E5FF !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.75rem !important;
        width: 100% !important;
        transition: all 0.2s ease !important;
    }

    .stButton > button:hover {
        background: rgba(0, 229, 255, 0.15) !important;
        border-color: rgba(0, 229, 255, 0.5) !important;
        color: #FFFFFF !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)



# ============================================================
# 3. CACHED MODEL LOADER
# ============================================================
@st.cache_resource
def load_model_and_labels():
    device = torch.device("cuda" if torch.cuda.is_available() else 'cpu')

    if not MODEL_PATH.exists():
        st.error(f"Checkpoint not found at `{MODEL_PATH}`")
        return None, [], device

    checkpoint = torch.load(MODEL_PATH, map_location=device)
    class_names = checkpoint['class_names']

    model = models.resnet101(weights=None)
    model.fc = nn.Linear(model.fc.in_features, len(class_names))
    model.load_state_dict(checkpoint['model_state_dict'])
    model = model.to(device)

    model.eval()

    return model, class_names, device



model, class_names, device = load_model_and_labels()


# ============================================================
# 4. POPUP MODAL FOR SUPPORTED FOOD CLASSES
# ============================================================

@st.dialog(title="Supported Classes Overview", width='large')
def show_classes_modal(classes):
    st.markdown(
        f"This ResNet-50 model is trained to recognize **{len(classes)}** distinct food categories. Here is the full directory:")
    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    cols = st.columns(3)
    for idx, name in enumerate(classes):
        with cols[idx % 3]:
            st.markdown(
                f"""
                <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); padding: 8px 12px; border-radius: 6px; margin-bottom: 6px; font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; color: #D1D5DB; text-transform: capitalize;">
                    {idx + 1}. {name.replace('_'," ")}
                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# 5. PAGE HEADER & ALIGNED MODAL TRIGGER
# ============================================================
st.markdown(
    """
    <div style="display: inline-flex; align-items: center; gap: 8px; padding: 4px 12px; border-radius: 6px; background: rgba(0, 229, 255, 0.08); border: 1px solid rgba(0, 229, 255, 0.2); color: #00E5FF; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; margin-bottom: 0.75rem;">
        <span>COMPUTER VISION / RESNET-101</span>
    </div>
    """,
    unsafe_allow_html=True
)

title_col, btn_col = st.columns([3.5, 1], vertical_alignment="center")

with title_col:
    st.markdown(
        """
        <h2 style="font-size: 2.2rem; font-weight: 700; margin: 0; color: #F9FAFB;">
            Leaf Disease Image Classifier
        </h2>
        """,
        unsafe_allow_html=True
    )

with btn_col:
    if st.button("View All Classes", use_container_width=True):
        show_classes_modal(class_names)

st.markdown(
    """
    <p style="color: #9CA3AF; font-size: 0.95rem; margin-top: 0.5rem; margin-bottom: 2rem;">
        Upload a leaf image of a supported class to evaluate fine-tuned ResNet-101 feature representations and probability distributions in real time.<br>
        <span style="color: rgb(0, 225, 229, 0.6)">Note : Not The Perfect Model, Can Make Mistakes & Provide Inaccurate Results.</span>
    </p>
    """,
    unsafe_allow_html=True
)


# ============================================================
# 6. SIDE-BY-SIDE EQUAL LAYOUT (UPLOAD & RENDER)
# ============================================================

col_upload, col_preview = st.columns(2, gap="large")

# --- LEFT COLUMN: File Uploader ---
with col_upload:
    st.markdown('<div class="panel-header">Upload Image</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Choose a food image...",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )

# --- RIGHT COLUMN: Rendered Image Preview ---
with col_preview:
    st.markdown('<div class="panel-header">Render Preview</div>', unsafe_allow_html=True)

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')

        # Convert Image to Base64 to render safely INSIDE the HTML div
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        st.markdown(
            f"""
            <div class="preview-card">
                <img src="data:image/jpeg;base64,{img_str}" alt="Uploaded Food" />
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <div class="placeholder-card">
                <span>Awaiting image upload...</span>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# 7. CLASSIFICATION & LIVE METRICS
# ============================================================

if uploaded_file is not None and model is not None:

    st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)

    classify_click = st.button("Classify Image", use_container_width=True)

    if classify_click:

        # Preprocess The Image
        inference_transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])
        ])

        input_tensor = inference_transform(image).unsqueeze(0).to(device)

        with torch.no_grad():

            outputs = model(input_tensor)
            probabilities = torch.nn.functional.softmax(outputs, dim=1)
            confidence, predicted_idx = torch.max(probabilities, 1)

        predicted_class = class_names[predicted_idx.item()]
        confidence_score = confidence.item() * 100
        top3_probab, top3_idx = torch.topk(probabilities, 3)

        st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)

        # Display Results
        res_col1, res_col2 = st.columns([1.1, 1], gap="large")

        with res_col1:
            st.markdown('<div class="panel-header">Top Class Prediction</div>', unsafe_allow_html=True)
            st.markdown(
                f"""
                <div class="result-badge">
                    <span style="text-transform: capitalize;">{re.sub(r'_+', '_', predicted_class).strip('_').replace('_'," ")}</span>
                    <span style="font-size: 1.1rem; color: #34D399;">{confidence_score:.1f}%</span>
                </div>
                """,
                unsafe_allow_html=True
            )

        with res_col2:
            st.markdown('<div class="panel-header">Probability Distribution (Top 3)</div>', unsafe_allow_html=True)

            for i in range(min(3, len(class_names))):
                cls = class_names[top3_idx[0][i].item()]
                prob = top3_probab[0][i].item() * 100
                st.markdown(
                    f"""
                    <div class="prob-bar-container">
                        <div class="prob-label">
                            <span style="text-transform: capitalize;">{re.sub(r'_+', '_', cls).strip('_').replace('_'," ")}</span>
                            <span>{prob:.2f}%</span>
                        </div>
                        <div class="prob-bar-bg">
                            <div class="prob-bar-fill" style="width: {prob:.2f}%;"></div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )