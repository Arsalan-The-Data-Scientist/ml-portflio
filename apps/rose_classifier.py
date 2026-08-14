import streamlit as st
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
from pathlib import Path

# ==========================================
# 1. PAGE CONFIGURATION & STYLES
# ==========================================
st.set_page_config(page_title="CNN Rose Classifier", layout="centered")

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
    min-height: 450px !important;
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

/* Placeholder */
.placeholder-box {
    height: 300px;
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

[data-testid="stImage"] {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 350px;
}

[data-testid="stImage"] img {
    border-radius: 16px;
    max-width: 100% !important;
    max-height: 350px !important;
    width: auto !important;
    height: auto !important;
    object-fit: contain !important;
}

.block-container {
    padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# 2. MODEL ARCHITECTURE DEFINITION
# ==========================================
class FlowerDetector(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(128, 256, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )

        self.classifier = nn.Sequential(
            nn.AdaptiveAvgPool2d((1, 1)),
            nn.Flatten(),

            nn.Linear(256, 64),
            nn.ReLU(),

            nn.Linear(64, 4)
        )

    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x


# ==========================================
# 3. CACHE MODEL & SETUP TRANSFORMS
# ==========================================
@st.cache_resource
def load_rose_model():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    script_dir = Path(__file__).parent
    model_path = script_dir / 'best_rose_color_model.pth'

    # Load state dictionary weights safely
    state_dict = torch.load(model_path, map_location=device)

    # Instantiate architecture, send to device, and load weights
    model = FlowerDetector().to(device)
    model.load_state_dict(state_dict)
    model.eval()

    return model, device


model, device = load_rose_model()

# Defined test/validation transforms
val_test_transform = transforms.Compose([
    transforms.Resize((244, 244)),
    transforms.ToTensor()
])

# Update class labels to match your exact training dataset order (4 classes)
CLASS_LABELS = ["Red", "Pink", "White", "Yellow"]

# ==========================================
# 4. PAGE HEADER
# ==========================================
st.markdown("""
<div class="page-title">
    CNN Rose Classifier
</div>
<div class="page-subtitle" style="font-size:15px;">
    Upload a rose image and let the deep learning model classify its category.
    <br>
    Not the perfect model, may give inaccurate results, specially for 'Pink' flowers.
</div>
""", unsafe_allow_html=True)

# ==========================================
# 5. TWO COLUMN LAYOUT
# ==========================================
left_col, right_col = st.columns([1, 1])

with left_col:
    with st.container(border=True):
        uploaded_file = st.file_uploader(
            "",
            type=["jpg", "jpeg", "png"],
            label_visibility="collapsed"
        )

with right_col:
    with st.container(border=True):
        if uploaded_file is not None:
            image = Image.open(uploaded_file).convert('RGB')
            st.image(image)
        else:
            st.markdown("""
            <div class="placeholder-box">
                Upload an image to see preview
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# 6. MODEL INFERENCE SECTION
# ==========================================
if uploaded_file is not None:
    st.markdown("<br>", unsafe_allow_html=True)

    with st.spinner("Processing tensors through CNN..."):
        # Apply transforms and move tensor to device
        input_tensor = val_test_transform(image).unsqueeze(0).to(device)

        with torch.no_grad():
            outputs = model(input_tensor)
            probabilities = torch.nn.functional.softmax(outputs, dim=1)
            confidence, predicted_idx = torch.max(probabilities, 1)

            predicted_label = CLASS_LABELS[predicted_idx.item()] if predicted_idx.item() < len(
                CLASS_LABELS) else f"Class {predicted_idx.item()}"
            confidence_score = confidence.item()

    # Display Results Card
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Predicted Rose Type", value=predicted_label)
    with col2:
        st.metric(label="Confidence Score", value=f"{confidence_score:.1%}")