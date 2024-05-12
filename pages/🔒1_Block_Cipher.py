import streamlit as st

st.header("Block Cipher - XOR")

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
    encrypted_data = b''
    padded_plaintext = pad(plaintext, block_size)
    for x, i in enumerate(range(0, len(padded_plaintext), block_size)):
        plaintext_block = padded_plaintext[i:i+block_size]
        encrypted_block = xor_encrypt_block(plaintext_block, key)
        encrypted_data += encrypted_block
    return encrypted_data                               


def xor_decrypt(ciphertext, key, block_size):
    decrypted_data = b''
    for x, i in enumerate(range(0, len(ciphertext), block_size)):
        ciphertext_block = ciphertext[i:i+block_size]
        decrypted_block = xor_decrypt_block(ciphertext_block, key)
        decrypted_data += decrypted_block
    try:
        unpadded_decrypted_data = unpad(decrypted_data)
        return unpadded_decrypted_data
    except ValueError:
        return b"Decryption failed due to invalid padding"

if __name__ == "__main__":
    mode = st.radio("Choose mode:", ("Encryption", "Decryption"))
    
    if mode == "Encryption":
        plaintext = st.text_input("Enter plaintext:")
        key = st.text_input("Enter key:")
        block_size = st.number_input("Enter block size", value=8, step=8)
        
        if st.button("Encrypt"):
            if block_size not in [8, 16, 32, 64, 128]:
                st.error("Block size must be one of 8, 16, 32, 64, or 128 bytes")
            else:
                plaintext = bytes(plaintext.encode())
                key = bytes(key.encode())
                key = pad(key, block_size)
                ciphertext = xor_encrypt(plaintext,key,block_size)
                st.write("Encrypted data:", ciphertext.hex())
    
    elif mode == "Decryption":
        ciphertext = st.text_input("Enter ciphertext (in hexadecimal format):")
        key = st.text_input("Enter key:")
        block_size = st.number_input("Enter block size", value=8, step=8)
        
        if st.button("Decrypt"):
            try:
                ciphertext = bytes.fromhex(ciphertext)
                key = bytes(key.encode())
                decrypted_data = xor_decrypt(ciphertext,key,block_size)
                st.write("Decrypted data:", decrypted_data.decode())
            except ValueError as e:
                st.error(str(e))
