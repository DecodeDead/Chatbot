import streamlit as st
import requests

st.title("Document Q&A Chatbot")


uploaded_file = st.file_uploader("Upload a document", type=["txt"])
if uploaded_file is not None:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post("http://localhost:8000/upload/", files=files)
    if response.status_code == 200:
        st.success(f"Uploaded {uploaded_file.name}")
    else:
        st.error("Failed to upload file")


question = st.text_input("Ask a question about the document")
if question:
    response = requests.post("http://localhost:8000/chat/", json={"question": question})
    if response.status_code == 200:
        answer = response.json().get("response")
        st.write(f"Answer: {answer}")
    else:
        st.error(response.json().get("error"))