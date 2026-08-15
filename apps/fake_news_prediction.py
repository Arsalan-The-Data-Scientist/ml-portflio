import streamlit as st
import torch
import torch.nn as nn
import spacy
import re
from pathlib import Path

# --- 1. MINIMAL DARK UI STYLING ---
# Note: If you are running this via an app.py multipage setup,
# you might need to remove set_page_config if it's already set in app.py
st.set_page_config(page_title="Fake News Classifier AI", layout="centered")

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
class NewsClassifier(nn.Module):
    def __init__(self, vocab_size: int, embedding_dimensions: int, architecture_type: str = "LSTM",
                 hidden_size: int = 128, num_layers: int = 1, bidirectional: bool = True, dropout: float = 0.3):
        super().__init__()
        self.architecture_type = architecture_type.upper()
        self.bidirectional = bidirectional

        self.embedding = nn.Embedding(
            num_embeddings=vocab_size,
            embedding_dim=embedding_dimensions
        )

        if self.architecture_type == "LSTM":
            self.rnn = nn.LSTM(
                input_size=embedding_dimensions,
                hidden_size=hidden_size,
                num_layers=num_layers,
                batch_first=True,
                bidirectional=bidirectional
            )
        elif self.architecture_type == "GRU":
            self.rnn = nn.GRU(
                input_size=embedding_dimensions,
                hidden_size=hidden_size,
                num_layers=num_layers,
                batch_first=True,
                bidirectional=bidirectional
            )
        elif self.architecture_type == "RNN":
            self.rnn = nn.RNN(
                input_size=embedding_dimensions,
                hidden_size=hidden_size,
                num_layers=num_layers,
                batch_first=True,
                bidirectional=bidirectional
            )
        else:
            raise ValueError("architecture_type must be 'RNN', 'GRU' or 'LSTM'")

        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear((hidden_size * 2) if bidirectional else hidden_size, 1)

    def forward(self, x):
        x = self.embedding(x)

        if self.architecture_type == "LSTM":
            output, (hidden, cell) = self.rnn(x)
        else:
            output, hidden = self.rnn(x)

        if self.bidirectional:
            forward_hidden = hidden[-2]
            backward_hidden = hidden[-1]
            x = torch.cat((forward_hidden, backward_hidden), dim=1)
        else:
            x = hidden[-1]

        x = self.dropout(x)
        x = self.fc(x)

        return x.squeeze(1)


# --- 3. CACHE THE MODEL LOADING ---
@st.cache_resource
def load_fake_news_model():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    script_dir = Path(__file__).parent
    model_path = script_dir / 'fake_news_gru_deployment.pth'

    bundle = torch.load(model_path, map_location=device)
    vocab2idx = bundle["vocab2idx"]

    # vocab_size wasn't explicitly saved in the dict, so we derive it from the dictionary length
    vocab_size = len(vocab2idx)

    model = NewsClassifier(
        vocab_size=vocab_size,
        embedding_dimensions=bundle["embedding_dim"],
        architecture_type=bundle["architecture_type"],
        hidden_size=bundle["hidden_size"],
        num_layers=bundle["num_layers"],
        bidirectional=bundle["bidirectional"],
        dropout=bundle["dropout"]
    ).to(device)

    model.load_state_dict(bundle["model_state_dict"])
    model.eval()

    # Load Spacy tokenizer inside cache so it doesn't reload on every UI interaction
    nlp = spacy.blank("en")

    return model, vocab2idx, bundle["max_seq_len"], device, nlp


model, vocab2idx, MAX_SEQ_LEN, device, nlp = load_fake_news_model()


# --- 4. PREDICTION LOGIC ---
def predict_news(text, model, nlp, vocab2idx, device, max_seq_len):
    # 1. Preprocess + tokenize
    text = text.lower()
    text = re.sub(r'https?://\S+|www\.\S+', ' URL ', text)
    tokens = [token.text for token in nlp(text) if not token.is_space]

    # 2. Convert tokens to IDs
    # Using .get() fallback to handle out-of-vocabulary words
    unk_idx = vocab2idx.get("<UNK>", 0)
    pad_idx = vocab2idx.get("<PAD>", 0)

    encoded = [vocab2idx.get(token, unk_idx) for token in tokens]

    # 3. Pad / truncate
    if len(encoded) < max_seq_len:
        encoded += [pad_idx] * (max_seq_len - len(encoded))
    else:
        encoded = encoded[:max_seq_len]

    # 4. Convert to tensor
    input_tensor = torch.tensor(encoded, dtype=torch.long).unsqueeze(0).to(device)

    # 5. Prediction
    with torch.no_grad():
        output = model(input_tensor)
        probability = torch.sigmoid(output).item()

    # 6. Convert to class
    label = 1 if probability >= 0.5 else 0

    if label == 1:
        prediction = "Fake News"
        confidence = probability
    else:
        prediction = "True News"
        confidence = 1 - probability

    return prediction, confidence


# --- 5. STREAMLIT UI LAYOUT ---
st.title("Fake News Classification")
st.write("Powered by a custom Deep Learning GRU Architecture.")
st.write("Note: This model analyzes linguistic patterns and may not be 100% accurate. Fact-check important news.")

news_text = st.text_area("Enter the news article text to analyze:", height=200,
                         placeholder="Paste the news article here...")

if st.button("Analyze Article"):
    if not news_text.strip():
        st.warning("Please enter an article to analyze.")
    else:
        with st.spinner("Analyzing text patterns..."):
            # Run Inference
            prediction, confidence = predict_news(
                text=news_text,
                model=model,
                nlp=nlp,
                vocab2idx=vocab2idx,
                device=device,
                max_seq_len=MAX_SEQ_LEN
            )

            # Display Results
            st.markdown("---")
            if prediction == "True News":
                st.success("### Genuine News Detected")
                st.write(f"**Confidence Score:** {confidence:.1%}")
            else:
                st.error("### Fake News Detected")
                st.write(f"**Confidence Score:** {confidence:.1%}")