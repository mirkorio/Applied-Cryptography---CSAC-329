import streamlit as st

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

def main():
    st.header("Caesar Cipher Encryption and Decryption")
    option = st.radio("Choose mode:", ["Encryption", "Decryption"])

    if option == "Encryption":
        text = st.text_input("Enter text to encrypt:")
        shifts = st.text_input("Enter shift values separated by space:")
        if st.button("Encryption"):
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
    elif option == "Decryption":
        text = st.text_input("Enter text to decrypt:")
        shifts = st.text_input("Enter shift values separated by space:")
        if st.button("Decryption"):
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
            decoded_table = [["Encrypted Character", "Shift", "Decoded Character"]] + decoded_details
            st.table(decoded_table)


if __name__ == "__main__":
    main()
