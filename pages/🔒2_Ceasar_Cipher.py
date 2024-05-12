import streamlit as st

def caesar_cipher(text, shifts):
    encrypted_text = ""
    decoded_details = []
    shifts = list(map(int, shifts.split()))
    shift_index = 0
    for char in text:
        if char.isalpha():
            original_char = char
            shift = shifts[shift_index]
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
            shift_index = (shift_index + 1) % len(shifts)
        else:
            encrypted_text += char
            decoded_details.append((char, "N/A", char))
    return encrypted_text, decoded_details

def main():
    st.title("Caesar Cipher Encryption and Decryption")
    option = st.radio("Choose mode:", ["Encryption", "Decryption"])

    if option == "Encryption":
        text = st.text_input("Enter text to encrypt:")
        shifts = st.text_input("Enter shift values separated by space:")
        if st.button("Encrypt"):
            encrypted_text, decoded_details = caesar_cipher(text, shifts)
            st.success("Encryption Successful!")
            st.write("### Encryption Results")
            st.write("Original Text:")
            st.write(text)
            st.write("Shift Values:")
            st.write(shifts)
            st.write("Encrypted Text:")
            st.write(encrypted_text)
            st.write("Decoded Details:")
            decoded_table = [["Original Character", "Shift", "Decoded Character"]] + decoded_details
            st.table(decoded_table)
    elif option == "Decryption":
        text = st.text_input("Enter text to decrypt:")
        shifts = st.text_input("Enter shift values separated by space:")
        if st.button("Decrypt"):
            decrypted_text, decoded_details = caesar_cipher(text, shifts)
            st.success("Decryption Successful!")
            st.write("### Decryption Results")
            st.write("Encrypted Text:")
            st.write(text)
            st.write("Shift Values:")
            st.write(shifts)
            st.write("Decrypted Text:")
            st.write(decrypted_text)
            st.write("Decoded Details:")
            decoded_table = [["Encrypted Character", "Shift", "Decoded Character"]] + decoded_details
            st.table(decoded_table)

if __name__ == "__main__":
    main()
