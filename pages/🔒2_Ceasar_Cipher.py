import streamlit as st
import io

def caesar_cipher(text, shifts):
    encrypted_text = ""
    decoded_details = []
    shifts = list(map(int, shifts.split()))
    shift_index = 0
    
    for char in text:
        if char.isalnum():
            original_char = char
            shift = shifts[shift_index % len(shifts)]
            shift_index += 1
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

def caesar_decipher(text, shifts):
    decrypted_text = ""
    decoded_details = []
    shift_index = 0
    shifts = list(map(int, shifts.split()))
    
    for char in text:
        if char.isalnum():
            shift = shifts[shift_index % len(shifts)]
            shift_index += 1
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
                elif shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                elif shifted > ord('Z'):
                    shifted -= 26
            decrypted_char = chr(shifted)
            decoded_details.append((char, shift, decrypted_char))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
            decoded_details.append((char, "N/A", char))
    return decrypted_text, decoded_details

def encrypt_text():
    text = st.text_area("Enter text to encrypt:")
    shifts = st.text_input("Enter shift values separated by space: (ex. 1 2 3)")
    if st.button("Encrypt"):
        encrypted_text, encoded_details = caesar_cipher(text, shifts)
        st.success("Encryption Successful!")
        st.write("### Encryption Results")
        st.write("Original Text:")
        st.write(text)
        st.write("Shift Values:")
        st.write(shifts)
        st.write("Encrypted Text:")
        st.write(encrypted_text)
        st.write("Encoded Details:")
        encoded_table = [["Original Character", "Shift", "Encoded Character"]] + encoded_details
        st.table(encoded_table)

def decrypt_text():
    text = st.text_area("Enter text to decrypt:")
    shifts = st.text_input("Enter shift values separated by space: (ex. 1 2 3)")
    if st.button("Decrypt"):
        decrypted_text, decoded_details = caesar_decipher(text, shifts)
        st.success("Decryption Successful!")
        st.write("### Decryption Results")
        st.write("Encrypted Text:")
        st.write(text)
        st.write("Shift Values:")
        st.write(shifts)
        st.write("Decrypted Text:")
        st.write(decrypted_text)
        st.write("Decoded Details:")
        decoded_table = [["Encrypted Character", "Shift", "Decrypted Character"]] + decoded_details
        st.table(decoded_table)

def encrypt_file(file):
    shifts = st.text_input("Enter shift values separated by space: (ex. 1 2 3)")
    if st.button("Encrypt File"):
        try:
            # Read file contents
            file_contents = file.getvalue().decode("utf-8")
            encrypted_text, _ = caesar_cipher(file_contents, shifts)
            st.success("File Encryption Successful!")
            st.write("### Encrypted File Contents:")
            st.code(encrypted_text)

            # Download the encrypted file
            encrypted_file = io.BytesIO(encrypted_text.encode())
            st.download_button(label="Download Encrypted File", data=encrypted_file, file_name="encrypted_file.txt")
        except Exception as e:
            st.error(f"Error: {e}")

def decrypt_file(file):
    shifts = st.text_input("Enter shift values separated by space: (ex. 1 2 3)")
    if st.button("Decrypt File"):
        try:
            # Read file contents
            file_contents = file.getvalue().decode("utf-8")
            decrypted_text, _ = caesar_decipher(file_contents, shifts)
            st.success("File Decryption Successful!")
            st.write("### Decrypted File Contents:")
            st.code(decrypted_text)

            # Download the decrypted file
            decrypted_file = io.BytesIO(decrypted_text.encode())
            st.download_button(label="Download Decrypted File", data=decrypted_file, file_name="decrypted_file.txt")
        except Exception as e:
            st.error(f"Error: {e}")

def main():
    st.header("Caesar Cipher - Encryption and Decryption")
    st.markdown("""<div style="background-color:#222831;padding:10px;border-radius:10px">
    <p style="text-align: justify; color: white;">The Caesar cipher, also known as Caesar’s code, is a monoalphabetic substitution cipher. In this technique, each letter in the plaintext is replaced by another letter located a fixed number of positions down the alphabet. For example, with a left shift of 3, “D” becomes “A,” “E” becomes “B,” and so on. The method is named after Julius Caesar, who used it in his private correspondence.</p>
    </div>""", unsafe_allow_html=True)
    st.write("---")

    option = st.radio("Choose mode:", ["Text Encryption", "Text Decryption", "File Encryption", "File Decryption"])

    if option == "Text Encryption":
        encrypt_text()
    elif option == "Text Decryption":
        decrypt_text()
    elif option == "File Encryption":
        st.write("Upload a file to encrypt:")
        file = st.file_uploader("File uploader")
        if file is not None:
            encrypt_file(file)
    elif option == "File Decryption":
        st.write("Upload a file to decrypt:")
        file = st.file_uploader("File uploader")
        if file is not None:
            decrypt_file(file)

if __name__ == "__main__":
    main()
