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

# Hash function descriptions
hash_descriptions = {
    "MD5": """<div style="background-color:#222831;padding:10px;border-radius:10px">
    <p style="text-align: justify; color: white;">MD5 is a widely used cryptographic hash function that produces a 128-bit hash value. It was designed by Ronald Rivest in 1991 as a replacement for the earlier MD4 hash function. Historically, MD5 was used for cryptographic purposes, but it has been found to have extensive vulnerabilities. It remains suitable for non-cryptographic purposes, such as data integrity verification.</p>
    </div>
    """,
    "SHA-1": """<div style="background-color:#222831;padding:10px;border-radius:10px">
    <p style="text-align: justify; color: white;">The Secure Hash Algorithm 1 (SHA-1) is a cryptographic computer security algorithm. It was created by the US National Security Agency in 1995, after the SHA-0 algorithm in 1993, and it is part of the Digital Signature Algorithm or the Digital Signature Standard (DSS). SHA-1 is commonly used in cryptographic applications and environments where the need for data integrity is high. It is also used to index hash functions and identify data corruption and checksum errors.</p>
    </div>""",
    "SHA-256": """<div style="background-color:#222831;padding:10px;border-radius:10px">
    <p style="text-align: justify; color: white;">Secure Hash Algorithm 256-bit, also known as SHA-256, is a cryptographic hash function that converts text of any length to an almost-unique alphanumeric string of 256 bits. The output is known as a hash value or hash. It provides better collision resistance than its predecessors. SHA-256 is crucial for security applications, including TLS, SSL, and blockchain technology.</p>
    </div>""",
    "SHA-512": """<div style="background-color:#222831;padding:10px;border-radius:10px">
    <p style="text-align: justify; color: white;">
SHA-512 is part of the SHA-2 family and produces a 512-bit hash value. It offers even greater collision resistance than SHA-256. SHA-512 is used in various security protocols, ensuring data integrity and authenticity. It’s commonly employed in TLS, SSL, and other cryptographic applications.</p>
    </div>"""
}
# Choose hashing technique
hash_type = st.selectbox("Choose a hash function:", ("MD5", "SHA-1", "SHA-256", "SHA-512"))

if hash_type:
    st.header(f"{hash_type} Hashing")
    st.markdown(hash_descriptions[hash_type], unsafe_allow_html=True)
    
    st.write("---")
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
