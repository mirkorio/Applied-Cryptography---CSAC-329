import streamlit as st

def caesar_cipher(text, shift):
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

def main():
    st.title("Caesar Cipher Encryption and Decryption")

    mode = st.sidebar.selectbox("Mode", ["Encrypt", "Decrypt"])

    if mode == "Encrypt":
        st.subheader("Encryption")
        message = st.text_area("Enter your message:")
        shift = st.number_input("Enter the shift value:", min_value=1, max_value=25, step=1)
        
        if st.button("Encrypt"):
            if message:
                encrypted_message = caesar_cipher(message, shift)
                st.success("Message encrypted successfully!")
                st.text("Encrypted Message:")
                st.text(encrypted_message)

    elif mode == "Decrypt":
        st.subheader("Decryption")
        encrypted_message = st.text_area("Enter the encrypted message:")
        shift = st.number_input("Enter the shift value used for encryption:", min_value=1, max_value=25, step=1)
        
        if st.button("Decrypt"):
            if encrypted_message:
                decrypted_message = caesar_cipher(encrypted_message, -shift)
                st.success("Message decrypted successfully!")
                st.text("Decrypted Message:")
                st.text(decrypted_message)

if __name__ == "__main__":
    main()
