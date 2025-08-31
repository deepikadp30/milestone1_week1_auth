import streamlit as st

st.title("📂 Drag and Drop Demo")

# Drag-and-drop file uploader
uploaded_file = st.file_uploader("Drag and drop a file here", type=["txt", "csv", "jpg", "png"])

if uploaded_file is not None:
    st.success(f"File uploaded: {uploaded_file.name}")

    # Example: Read and display file content if it's text
    if uploaded_file.type == "text/plain":
        content = uploaded_file.read().decode("utf-8")
        st.text_area("File Content", content, height=200)
