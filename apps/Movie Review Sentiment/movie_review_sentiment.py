import streamlit as st
import torch
import torch.nn as nn
import spacy
import re
import os
from pathlib import Path

# --- 1. MINIMAL DARK UI STYLING ---
st.set_page_config(page_title="Review Sentiment AI", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0f0f 0%, #2d2d2d 100%);
        color: #f1f1f1;
    }
    h1 {
        font-weight: 300;
        letter-spacing: 1px;
    }
    .stTextArea textarea {
        background-color: #1e1e1e !important;
        color: #ffffff !important;
        border: 1px solid #444 !important;
        border-radius: 8px;
    }
    .stButton>button {
        background-color: #333333;
        color: white;
        border-radius: 8px;
        border: 1px solid #555;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #555555;
        border-color: #777;
    }
    </style>
""", unsafe_allow_html=True)


# --- 2. MODEL ARCHITECTURE DEFINITION ---
class ReviewSentimentClassifier(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, cell_type='GRU', num_layers=1, dropout=0.2):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)

        if cell_type == 'LSTM':
            self.rnn = nn.LSTM(embed_dim, hidden_dim, num_layers=num_layers, batch_first=True,
                               dropout=dropout if num_layers > 1 else 0)
        elif cell_type == 'GRU':
            self.rnn = nn.GRU(embed_dim, hidden_dim, num_layers=num_layers, batch_first=True,
                              dropout=dropout if num_layers > 1 else 0)
        else:
            self.rnn = nn.RNN(embed_dim, hidden_dim, num_layers=num_layers, batch_first=True)

        self.fc = nn.Linear(hidden_dim, 1)
        self.cell_type = cell_type

    def forward(self, x):
        embedded = self.embedding(x)
        if self.cell_type == 'LSTM':
            out, (hidden, cell) = self.rnn(embedded)
        else:
            out, hidden = self.rnn(embedded)
        last_hidden = hidden[-1]
        logits = self.fc(last_hidden)
        return logits.squeeze(1)


# --- 3. CACHE THE MODEL LOADING ---
# @st.cache_resource ensures the model only loads once when the app starts
@st.cache_resource
def load_deployment_bundle():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # --- FIX: Resolve the absolute path based on this script's location ---
    script_dir = Path(__file__).parent
    model_path = script_dir / 'deployment_ready_sentiment_model.pth'

    bundle = torch.load(model_path, map_location=device)

    configs = bundle['configs']
    vocab2idx = bundle['vocab2idx']

    model = ReviewSentimentClassifier(
        vocab_size=configs['vocab_size'],
        embed_dim=configs['embed_dim'],
        hidden_dim=configs['hidden_dim'],
        cell_type=configs['cell_type']
    ).to(device)

    model.load_state_dict(bundle['model_state_dict'])
    model.eval()

    return model, vocab2idx, configs['max_seq_len'], device

model, vocab2idx, MAX_SEQ_LEN, device = load_deployment_bundle()

# --- 4. PREPROCESSING PIPELINE ---
nlp = spacy.blank("en")


def clean_and_tokenize(text):
    text = re.sub(r"<br\s*/?>", " ", text)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    return [token.text for token in nlp(text.lower()) if not token.is_space]


def encode_and_pad(tokens):
    encoded = [vocab2idx.get(word, 1) for word in tokens]
    if len(encoded) < MAX_SEQ_LEN:
        encoded = encoded + [0] * (MAX_SEQ_LEN - len(encoded))
    else:
        encoded = encoded[:MAX_SEQ_LEN]
    return encoded


# --- 5. STREAMLIT UI LAYOUT ---
st.title("Sentiment Analysis Engine")
st.write("Powered by a custom Deep Learning GRU Architecture.")
st.write("Note : Not The Perfect Model, Can Make Mistakes & Provide Inaccurate Results.")

user_review = st.text_area("Enter a movie review to analyze:", height=150, placeholder="Type your review here...")

if st.button("Analyze Sentiment"):
    if not user_review.strip():
        st.warning("Please enter some text to analyze.")
    else:
        with st.spinner("Processing tensors..."):

            # Run Inference
            with torch.no_grad():
                tokens = clean_and_tokenize(user_review)
                encoded = encode_and_pad(tokens)
                input_tensor = torch.tensor(encoded, dtype=torch.long).unsqueeze(0).to(device)

                logit = model(input_tensor)
                probability = torch.sigmoid(logit).item()

            # Display Results
            st.markdown("---")
            if logit.item() > 0:
                st.success(f"### Positive Sentiment Detected")
                st.write(f"**Confidence Score:** {probability:.1%}")
            else:
                st.error(f"### Negative Sentiment Detected")
                st.write(f"**Confidence Score:** {(1 - probability):.1%}")