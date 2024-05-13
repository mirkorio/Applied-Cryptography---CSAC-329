import streamlit as st

st.header("XOR Cipher")

# Define xor_encrypt function outside the blocks to make it accessible to both modes
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

mode = st.radio("Mode", ["Encrypt", "Decrypt"])

if mode == "Encrypt":
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
            
            st.subheader("Output:")
            st.table(output_details)

elif mode == "Decrypt":
    input_text = st.text_area("Encrypted Text: ")
    ciphertext = bytes.fromhex(input_text)  # Convert hex string back to bytes

    key = st.text_input("Key: ")
    key = key.encode('utf-8')  # Encode using UTF-8

    if st.button("Decrypt"):
        def xor_decrypt(ciphertext, key):
            """Decrypts ciphertext using XOR cipher with the given key"""
            return xor_encrypt(ciphertext, key)  

        if not ciphertext or not key:
            st.write("Invalid, Enter your ciphertext and key!")
        else:
            decrypted_text, output_details = xor_decrypt(ciphertext, key)
            st.write("Decrypted:", decrypted_text.decode('utf-8'))
            
            st.write("Details:")
            st.table(output_details)
