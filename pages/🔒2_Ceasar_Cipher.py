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
    option = st.radio("Choose an option:", ["Encrypt", "Decrypt"])

    if option == "Encrypt":
        text = st.text_input("Enter text to encrypt:")
        shift = st.number_input("Enter the shift value:", min_value=1, max_value=25, value=3)
        if st.button("Encrypt"):
            encrypted_text, decoded_details = caesar_cipher(text, shift)
            st.success("Encryption Successful!")
            st.write("### Encryption Results")
            st.write("Original Text:")
            st.write(text)
            st.write("Shift Value:")
            st.write(shift)
            st.write("Encrypted Text:")
            st.write(encrypted_text)
            st.write("Decoded Details:")
            decoded_table = [["Original Character", "Shift", "Decoded Character"]] + decoded_details
            st.table(decoded_table)
    elif option == "Decrypt":
        text = st.text_input("Enter text to decrypt:")
        shift = st.number_input("Enter the shift value:", min_value=1, max_value=25, value=3)
        if st.button("Decrypt"):
            decrypted_text, decoded_details = caesar_cipher(text, -shift)
            st.success("Decryption Successful!")
            st.write("### Decryption Results")
            st.write("Encrypted Text:")
            st.write(text)
            st.write("Shift Value:")
            st.write(shift)
            st.write("Decrypted Text:")
            st.write(decrypted_text)
            st.write("Decoded Details:")
            decoded_table = [["Encrypted Character", "Shift", "Decoded Character"]] + decoded_details
            st.table(decoded_table)

if __name__ == "__main__":
    main()
