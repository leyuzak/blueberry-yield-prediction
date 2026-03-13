import os
import pickle
import pandas as pd
import streamlit as st

PORT = int(os.getenv("PORT", 7860))
MODEL_PATH = "blueberry_model.pkl"

st.set_page_config(page_title="Blueberry Yield Prediction", layout="wide")

@st.cache_resource
def load_model():
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

model = load_model()

st.title("🍇 Blueberry Yield Prediction")

uploaded = st.file_uploader("CSV yükle", type="csv")

if uploaded:
    df = pd.read_csv(uploaded)
    st.write("Girdi verisi")
    st.dataframe(df.head())

    try:
        preds = model.predict(df)
        out = pd.DataFrame({"yield": preds})
        st.success("Tahmin tamamlandı")

        st.dataframe(out.head())

        st.download_button(
            "📥 submission.csv indir",
            out.to_csv(index=False),
            file_name="submission.csv",
            mime="text/csv"
        )
    except Exception as e:
        st.error(f"Hata: {e}")
