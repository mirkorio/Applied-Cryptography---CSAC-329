import streamlit as st
import io

st.header("XOR Cipher - Encryption and Decryption")
st.markdown("""<div style="background-color:#222831;padding:10px;border-radius:10px">
    <p style="text-align: justify; color: white;">The XOR cipher is commonly used as a component in more complex ciphers. When using a constant repeating key, a simple XOR cipher can be easily broken through frequency analysis. However, its simplicity and computational efficiency make it useful for hiding information when strong security isn’t required. The XOR cipher is often employed in computer malware to hinder reverse engineering. If the key is random and at least as long as the message, the XOR cipher becomes more secure.</p>
    </div>""", unsafe_allow_html=True)

def xor_encrypt(plaintext, key):
    """Encrypts plaintext using XOR cipher with the given key"""
    ciphertext = bytearray()
    output_details = []
    for i in range(len(plaintext)):
        plaintext_byte = plaintext[i]
        key_byte = key[i % len(key)]
        encrypted_byte = plaintext_byte ^ key_byte
        ciphertext.append(encrypted_byte)
        
        output_details.append({
            "Plaintext byte": format(plaintext_byte,'02X') + f" = {chr(plaintext_byte)}",
            "Key byte": format(key_byte, '02X') + f" = {chr(key_byte)}",
            "XOR result": format(encrypted_byte, '02X') + f" = {chr(encrypted_byte)}"
        })

    return ciphertext, output_details

def xor_decrypt(ciphertext, key):
    """Decrypts ciphertext using XOR cipher with the given key"""
    return xor_encrypt(ciphertext, key)  

def encrypt_text():
    input_text = st.text_area("Plain Text: ")
    plaintext = input_text.encode('utf-8')  # Encode using UTF-8

    key = st.text_input("Key: ")
    key = key.encode('utf-8')  # Encode using UTF-8

    if st.button("Encrypt"):
        if plaintext == key:
            st.write("Plaintext should not be equal to the key")
        elif not plaintext or not key:
            st.write("Invalid, Enter your plaintext and key!")
        elif len(plaintext) < len(key):
            st.write("Plaintext length should be equal or greater than the length of key")
        else:
            encrypted_text, output_details = xor_encrypt(plaintext, key)
            st.write("Ciphertext:", encrypted_text.hex())
            
            st.subheader("Encryption Details:")
            st.table(output_details)

def decrypt_text():
    input_text = st.text_area("Encrypted Text: ")
    ciphertext = bytes.fromhex(input_text)  # Convert hex string back to bytes

    key = st.text_input("Key: ")
    key = key.encode('utf-8')  # Encode using UTF-8

    if st.button("Decrypt"):
        if not ciphertext or not key:
            st.write("Invalid, Enter your ciphertext and key!")
        else:
            decrypted_text, output_details = xor_decrypt(ciphertext, key)
            st.write("Decrypted:", decrypted_text.decode('utf-8'))
            
            st.write("Decryption Details:")
            st.table(output_details)

def encrypt_file():
    file = st.file_uploader("Upload File to Encrypt", type=["txt", "pdf", "docx"])
    if file is not None:
        file_contents = file.read()
        key = st.text_input("Key: ")
        key = key.encode('utf-8')  # Encode using UTF-8

        if st.button("Encrypt File"):
            encrypted_text, _ = xor_encrypt(file_contents, key)
            st.write("Encryption Successful!")

            # Download the encrypted file
            st.download_button(label="Download Encrypted File", data=io.BytesIO(encrypted_text), file_name=file.name)

def decrypt_file():
    file = st.file_uploader("Upload File to Decrypt", type=["txt", "pdf", "docx"])
    if file is not None:
        file_contents = file.read()
        key = st.text_input("Key: ")
        key = key.encode('utf-8')  # Encode using UTF-8

        if st.button("Decrypt File"):
            decrypted_text, _ = xor_decrypt(file_contents, key)
            st.write("Decryption Successful!")

            # Download the decrypted file
            st.download_button(label="Download Decrypted File", data=io.BytesIO(decrypted_text), file_name=file.name)

mode = st.radio("Choose mode:", ["Text Encryption", "Text Decryption", "File Encryption", "File Decryption"])

if mode == "Text Encryption":
    encrypt_text()
elif mode == "Text Decryption":
    decrypt_text()
elif mode == "File Encryption":
    encrypt_file()
elif mode == "File Decryption":
    decrypt_file()
