import streamlit as st
import hashlib
import io

def hash_text(text, hash_type):
    if hash_type == "MD5":
        return hashlib.md5(text.encode()).hexdigest()
    elif hash_type == "SHA-1":
        return hashlib.sha1(text.encode()).hexdigest()
    elif hash_type == "SHA-256":
        return hashlib.sha256(text.encode()).hexdigest()
    elif hash_type == "SHA-512":
        return hashlib.sha512(text.encode()).hexdigest()

def hash_file(file, hash_type):
    if hash_type == "MD5":
        hasher = hashlib.md5()
    elif hash_type == "SHA-1":
        hasher = hashlib.sha1()
    elif hash_type == "SHA-256":
        hasher = hashlib.sha256()
    elif hash_type == "SHA-512":
        hasher = hashlib.sha512()

    file_contents = file.read()
    hasher.update(file_contents)
    return hasher.hexdigest()

# Streamlit app
st.header("Hashing Functions")

# Choose hashing technique
hash_type = st.selectbox("Choose a hash function:", ("MD5", "SHA-1", "SHA-256", "SHA-512"))

if hash_type:
    st.header(f"{hash_type} Hashing")

    # Ask for input method
    input_method = st.radio("Choose input method:", ("Text", "File"))

    if input_method == "Text":
        text = st.text_input("Enter text to hash:")
        if text:
            hashed_text = hash_text(text, hash_type)
            st.write("Hash value:", hashed_text)

    elif input_method == "File":
        file = st.file_uploader("Upload a file to hash:", type=["txt", "pdf", "docx", "csv", "xlsx"])
        if file:
            hashed_file = hash_file(io.BytesIO(file.read()), hash_type)
            st.write("Hash value:", hashed_file)
