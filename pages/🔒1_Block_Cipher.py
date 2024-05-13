import streamlit as st
import io

st.header("Block Cipher - XOR Encryption and Decryption")

def pad(data, block_size):
    padding_length = block_size - len(data) % block_size
    padding = bytes([padding_length] * padding_length)
    return data + padding

def unpad(data):
    padding_length = data[-1]
    if padding_length == 0 or padding_length > len(data):
        raise ValueError("Invalid padding")
    padding = data[-padding_length:]
    if not all(p == padding_length for p in padding):
        raise ValueError("Invalid padding")
    return data[:-padding_length]

def xor_encrypt_block(plaintext_block, key):
    encrypted_block = b''
    for i in range(len(plaintext_block)):
        encrypted_block += bytes([plaintext_block[i] ^ key[i % len(key)]])
    return encrypted_block

def xor_decrypt_block(ciphertext_block, key):
    return xor_encrypt_block(ciphertext_block, key)

def xor_encrypt(plaintext, key, block_size):
    if isinstance(plaintext, str):
        plaintext = plaintext.encode()
    elif isinstance(plaintext, int):
        plaintext = str(plaintext).encode()
    padded_plaintext = pad(plaintext, block_size)
    padded_key = pad(key, block_size)
    encrypted_data = b''
    for i in range(0, len(padded_plaintext), block_size):
        plaintext_block = padded_plaintext[i:i+block_size]
        encrypted_block = xor_encrypt_block(plaintext_block, padded_key)
        encrypted_data += encrypted_block
        st.write(f"Block {i//block_size+1} Encryption Details:")
        st.write("Plaintext Block:", plaintext_block.hex())
        st.write("Key Block:", padded_key.hex())
        st.write("Encrypted Block:", encrypted_block.hex())
    return encrypted_data

def xor_decrypt(ciphertext, key, block_size):
    decrypted_data = b''
    for i in range(0, len(ciphertext), block_size):
        ciphertext_block = ciphertext[i:i+block_size]
        decrypted_block = xor_decrypt_block(ciphertext_block, key)
        decrypted_data += decrypted_block
        st.write(f"Block {i//block_size+1} Decryption Details:")
        st.write("Ciphertext Block:", ciphertext_block.hex())
        st.write("Key Block:", key.hex())
        st.write("Decrypted Block:", decrypted_block.hex())
    try:
        unpadded_decrypted_data = unpad(decrypted_data)
        return unpadded_decrypted_data
    except ValueError:
        return b"Decryption failed due to invalid padding"

def main():
    mode = st.radio("Choose mode:", ("Encrypt Text", "Decrypt text", "Encrypt File", "Decrypt File"))
    
    if mode == "Encrypt Text":
        plaintext = st.text_input("Enter plaintext:")
        key = st.text_input("Enter key:")
        block_size = st.number_input("Enter block size", value=8, step=8)
        
        if st.button("Encrypt Text"):
            if block_size not in [8, 16, 32, 64, 128]:
                st.error("Block size must be one of 8, 16, 32, 64, or 128 bytes")
            else:
                key = bytes(key.encode())
                ciphertext = xor_encrypt(plaintext, key, block_size)
                st.write("Encrypted data:", ciphertext.hex())
    
    elif mode == "Decrypt text":
        ciphertext = st.text_input("Enter ciphertext (in hexadecimal format):")
        key = st.text_input("Enter key:")
        block_size = st.number_input("Enter block size", value=8, step=8)
        
        if st.button("Decrypt text"):
            try:
                key = bytes(key.encode())
                ciphertext = bytes.fromhex(ciphertext)
                decrypted_data = xor_decrypt(ciphertext, key, block_size)
                st.write("Decrypted data:", decrypted_data.decode())
            except ValueError as e:
                if str(e) == "Invalid padding":
                    st.error("Decryption failed due to invalid padding. Make sure the key and ciphertext are correct.")
                else:
                    st.error(str(e))
    
    elif mode == "Encrypt File":
        file = st.file_uploader("Upload File")
        if file is not None:
            file_contents = io.BytesIO(file.read())
            key = st.text_input("Enter key:")
            block_size = st.number_input("Enter block size", value=8, step=8)
            if st.button("Encrypt File"):
                if block_size not in [8, 16, 32, 64, 128]:
                    st.error("Block size must be one of 8, 16, 32, 64, or 128 bytes")
                else:
                    key = bytes(key.encode())
                    encrypted_data = xor_encrypt(file_contents.read(), key, block_size)
                    st.write("Encryption successful!")
                    st.write("Download the encrypted file below.")
                    st.download_button("Download Encrypted File", encrypted_data, file_name="encrypted_file.bin", mime="application/octet-stream")
    
    elif mode == "Decrypt File":
        file = st.file_uploader("Upload Encrypted File")
        if file is not None:
            file_contents = io.BytesIO(file.read())
            key = st.text_input("Enter key:")
            block_size = st.number_input("Enter block size", value=8, step=8)
            if st.button("Decrypt File"):
                try:
                    key = bytes(key.encode())
                    decrypted_data = xor_decrypt(file_contents.read(), key, block_size)
                    st.write("Decryption successful!")
                    st.write("Download the decrypted file below.")
                    st.download_button("Download Decrypted File", decrypted_data, file_name="decrypted_file.bin", mime="application/octet-stream")
                except ValueError as e:
                    if str(e) == "Invalid padding":
                        st.error("Decryption failed due to invalid padding. Make sure the key and ciphertext are correct.")
                    else:
                        st.error(str(e))

if __name__ == "__main__":
    main()
