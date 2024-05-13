import streamlit as st

st.header("XOR Cipher")

mode = st.radio("Mode", ["Encrypt", "Decrypt"])

if mode == "Encrypt":
    input_text = st.text_area("Plain Text: ")
    plaintext = bytes(input_text.encode())

    key = st.text_input("Key: ")
    key = bytes(key.encode())

    if st.button("Encrypt"):
        def xor_encrypt(plaintext, key):
            """Encrypts plaintext using XOR cipher with the given key, printing bits involved."""
            ciphertext = bytearray()
            output_details = []
            for i in range(len(plaintext)):
                plaintext_byte = plaintext[i]
                key_byte = key[i % len(key)]
                encrypted_byte = plaintext_byte ^ key_byte
                ciphertext.append(encrypted_byte)
                
                output_details.append({
                    "Plaintext byte": format(plaintext_byte,'08b') + f" = {chr(plaintext_byte)}",
                    "Key byte": format(key_byte, '08b') + f" = {chr(key_byte)}",
                    "XOR result": format(encrypted_byte, '08b') + f" = {chr(encrypted_byte)}"
                })

            return ciphertext, output_details

        if plaintext.decode() == key.decode():
            st.write("Plaintext should not be equal to the key")
        elif not plaintext or not key:
            st.write("Invalid, Enter your key!")
        elif len(plaintext.decode()) < len(key.decode()):
            st.write("Plaintext length should be equal or greater than the length of key")
        else:
            encrypted_text, output_details = xor_encrypt(plaintext, key)
            st.write("Ciphertext:", encrypted_text.decode())
            
            st.subheader("Output:")
            st.table(output_details)

elif mode == "Decrypt":
    input_text = st.text_area("Encrypted Text: ")
    ciphertext = bytes(input_text.encode())

    key = st.text_input("Key: ")
    key = bytes(key.encode())

    if st.button("Decrypt"):
        def xor_decrypt(ciphertext, key):
            """Decrypts ciphertext using XOR cipher with the given key"""
            return xor_encrypt(ciphertext, key)  # XOR decryption is the same as encryption

        def xor_encrypt(ciphertext, key):
            """Encrypts plaintext using XOR cipher with the given key"""
            plaintext = bytearray()
            output_details = []
            for i in range(len(ciphertext)):
                ciphertext_byte = ciphertext[i]
                key_byte = key[i % len(key)]
                decrypted_byte = ciphertext_byte ^ key_byte
                plaintext.append(decrypted_byte)
                
                output_details.append({
                    "Ciphertext byte": format(ciphertext_byte,'08b') + f" = {chr(ciphertext_byte)}",
                    "Key byte": format(key_byte, '08b') + f" = {chr(key_byte)}",
                    "XOR result": format(decrypted_byte, '08b') + f" = {chr(decrypted_byte)}"
                })

            return plaintext, output_details

        if not ciphertext or not key:
            st.write("Invalid, Enter your key!")
        else:
            decrypted_text, output_details = xor_decrypt(ciphertext, key)
            st.write("Decrypted:", decrypted_text.decode())
            
            st.write("Details:")
            st.table(output_details)


