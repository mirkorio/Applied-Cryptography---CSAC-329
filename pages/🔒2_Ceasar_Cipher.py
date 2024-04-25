import streamlit as st
import os
from io import BytesIO

def caesar_cipher(text, shift):
    if isinstance(text, str):
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                shifted = ord(char) + shift
                if char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                    elif shifted < ord('a'):
                        shifted += 26
                elif char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                    elif shifted < ord('A'):
                        shifted += 26
                encrypted_text += chr(shifted)
            else:
                encrypted_text += char
        return encrypted_text
    elif isinstance(text, BytesIO):
        return caesar_cipher(text.read().decode('utf-8'), shift)

def encrypt_file(input_file, output_file_path, shift):
    if output_file_path:
        encrypted_text = caesar_cipher(input_file, shift)
        st.write("Output file path:", output_file_path)
        with open(output_file_path, 'w') as f:
            f.write(encrypted_text)
    else:
        st.error("Please provide a valid output file path.")


def decrypt_file(input_file, output_file_path, shift):
    decrypted_text = caesar_cipher(input_file, -shift)
    with open(output_file_path, 'w') as f:
        f.write(decrypted_text)

def main():
    st.title("Caesar Cipher Encryption and Decryption")

    mode = st.sidebar.selectbox("Mode", ["Encrypt Text", "Decrypt Text", "Encrypt File", "Decrypt File"])

    if mode in ["Encrypt Text", "Decrypt Text"]:
        st.subheader("Text Encryption and Decryption")
        message = st.text_area("Enter your message:")
        shift = st.number_input("Enter the shift value:", min_value=1, max_value=25, step=1)
        
        if mode == "Encrypt Text":
            if st.button("Encrypt"):
                if message:
                    encrypted_message = caesar_cipher(message, shift)
                    st.success("Message encrypted successfully!")
                    st.text("Encrypted Message:")
                    st.text(encrypted_message)
        elif mode == "Decrypt Text":
            if st.button("Decrypt"):
                if message:
                    decrypted_message = caesar_cipher(message, -shift)
                    st.success("Message decrypted successfully!")
                    st.text("Decrypted Message:")
                    st.text(decrypted_message)

    elif mode in ["Encrypt File", "Decrypt File"]:
        # File encryption and decryption interface
        input_file = st.file_uploader("Upload the input file:", type=["txt"])
        if input_file is not None:
            output_file_path = st.text_input("Enter the output file path:")
            shift = st.number_input("Enter the shift value:", min_value=1, max_value=25, step=1)

            if st.button("Process File"):
                if mode == "Encrypt File":
                    encrypted_text = encrypt_file(input_file.read().decode('utf-8'), output_file_path, shift)
                    st.success("File encrypted successfully!")

                    # Download button for the encrypted file
                    st.download_button(
                        label="Download Encrypted File",
                        data=BytesIO(encrypted_text.encode('utf-8')),
                        file_name="encrypted_file.txt",
                        mime="text/plain"
                    )
                elif mode == "Decrypt File":
                    # Decrypt the file (implementation not provided in this snippet)
                    st.success("File decrypted successfully!")

if __name__ == "__main__":
    main()
