import streamlit as st

def caesar_cipher(text, shift):
    encrypted_text = ""
    decoded_details = []
    for char in text:
        if char.isalpha():
            original_char = char
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
            encrypted_char = chr(shifted)
            decoded_details.append((original_char, shift, encrypted_char))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
            decoded_details.append((char, "N/A", char))
    return encrypted_text, decoded_details

def main():
    st.title("Caesar Cipher Encryption and Decryption")
    option = st.selectbox("Choose an option:", ["Encrypt", "Decrypt"])

    if option == "Encrypt":
        text = st.text_input("Enter text to encrypt:")
        shift = st.number_input("Enter the shift value:", min_value=1, max_value=25, value=3)
        if st.button("Encrypt"):
            encrypted_text, decoded_details = caesar_cipher(text, shift)
            st.write("Original Text:", text)
            st.write("Shift Value:", shift)
            st.write("Encrypted Text:", encrypted_text)
            st.write("Decoded Details:")
            for original_char, shift, encrypted_char in decoded_details:
                st.write(f"Original Character: {original_char}, Shift: {shift}, Decoded Character: {encrypted_char}")
    elif option == "Decrypt":
        text = st.text_input("Enter text to decrypt:")
        shift = st.number_input("Enter the shift value:", min_value=1, max_value=25, value=3)
        if st.button("Decrypt"):
            decrypted_text, decoded_details = caesar_cipher(text, -shift)
            st.write("Encrypted Text:", text)
            st.write("Shift Value:", shift)
            st.write("Decrypted Text:", decrypted_text)
            st.write("Decoded Details:")
            for original_char, shift, encrypted_char in decoded_details:
                st.write(f"Encrypted Character: {encrypted_char}, Shift: {shift}, Decoded Character: {original_char}")

if __name__ == "__main__":
    main()
