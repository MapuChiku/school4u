import streamlit as st
from sklearn.metrics import recall_score

st.title("📢 Recall Score Example")

# Predefined labels
y_true = [1, 0, 1, 1, 0, 1, 0]
y_pred = [1, 0, 1, 0, 0, 1, 1]

# Show data
st.write("✅ Actual Labels:", y_true)
st.write("📌 Predicted Labels:", y_pred)

# Calculate recall
recall = recall_score(y_true, y_pred)
st.success(f"🎯 Recall Score: {recall:.2f}")