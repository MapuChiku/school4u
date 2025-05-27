import streamlit as st
from sklearn.metrics import precision_score

st.title("🎯 Precision Score Example")

y_true = [1, 0, 1, 1, 0, 1, 0]
y_pred = [1, 0, 1, 0, 0, 1, 1]

st.write("✅ Actual Labels:", y_true)
st.write("📌 Predicted Labels:", y_pred)

precision = precision_score(y_true, y_pred)
st.success(f"🔍 Precision Score: {precision:.2f}")