import streamlit as st

def xor_cipher(text, key):
    encrypted_text = ""
    for char in text:
        encrypted_text += chr(ord(char) ^ key)
    return encrypted_text

def main():
    st.title("XOR Cipher Encryption and Decryption")

    mode = st.sidebar.selectbox("Mode", ["Encrypt", "Decrypt"])

    if mode == "Encrypt":
        st.subheader("Encryption")
        message = st.text_area("Enter your message:")
        key = st.number_input("Enter the encryption key (an integer):", min_value=0, step=1)
        
        if st.button("Encrypt"):
            if message:
                encrypted_message = xor_cipher(message, key)
                st.success("Message encrypted successfully!")
                st.text("Encrypted Message:")
                st.text(encrypted_message)

    elif mode == "Decrypt":
        st.subheader("Decryption")
        encrypted_message = st.text_area("Enter the encrypted message:")
        key = st.number_input("Enter the decryption key used:", min_value=0, step=1)
        
        if st.button("Decrypt"):
            if encrypted_message:
                decrypted_message = xor_cipher(encrypted_message, key)
                st.success("Message decrypted successfully!")
                st.text("Decrypted Message:")
                st.text(decrypted_message)

if __name__ == "__main__":
    main()
