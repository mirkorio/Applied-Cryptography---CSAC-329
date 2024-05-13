import streamlit as st
import random

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to check if a number is a primitive root modulo p
def is_primitive_root(g, p):
    if not is_prime(p):
        return False
    primes_set = set()
    phi = p - 1
    for i in range(1, p):
        if pow(g, i, p) in primes_set:
            return False
        primes_set.add(pow(g, i, p))
    return len(primes_set) == phi

# Function to generate the public key
def generate_public_key(g, p, private_key):
    return (g ** private_key) % p

# Function to generate the shared key
def generate_shared_key(public_key, private_key, p):
    return (public_key ** private_key) % p

# Function to encrypt a message
def encrypt_message(message, key):
    encrypted_message = ""
    for char in message:
        encrypted_message += chr(ord(char) + key)
    return encrypted_message

# Function to decrypt a message
def decrypt_message(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        decrypted_message += chr(ord(char) - key)
    return decrypted_message

# Streamlit UI
def main():
    st.header("Diffie-Hellman Key Exchange")
    st.markdown("""<div style="background-color:#222831;padding:10px;border-radius:10px">
    <p style="text-align: justify; color: white;">The Diffie-Hellman key exchange algorithm, developed by Whitfield Diffie and Martin Hellman in 1976, is one of the earliest practical implementations of public-key cryptography. It allows two parties to securely establish a shared secret key over an insecure communication channel, without the need for prior shared secrets. The algorithm relies on the mathematical properties of modular exponentiation to derive a shared secret key.</p>
    </div>""", unsafe_allow_html=True)

    p = st.number_input("Enter a prime number:", value=5, step=1)
    if not is_prime(p):
        st.error("The entered number is not a prime number.")

    g = st.number_input("Enter a generator (a number less than {}):".format(p), value=3, step=1)
    if g >= p or not is_primitive_root(g, p):
        st.error("The entered number is not a primitive root of {}.".format(p))

    private_key = st.number_input("Enter your private key:", step=1)
    if private_key == 0:  # Check if private key is provided
        st.warning("Please input your private key to generate the public key.")

    public_key = generate_public_key(g, p, private_key)
    st.write("Your public key:", public_key)

    other_public_key = st.number_input("Enter the received public key:", step=1)

    shared_key = generate_shared_key(other_public_key, private_key, p)

    message_to_encrypt = st.text_input("Enter your message:", value="Hello bobby!", key="message_input")
    if st.button("Encrypt"):
        encrypted_message = encrypt_message(message_to_encrypt, shared_key)
        st.write("Ciphertext:", encrypted_message)

    received_encrypted_message = st.text_input("Enter the received ciphertext message:")
    if st.button("Decrypt"):
        decrypted_message = decrypt_message(received_encrypted_message, shared_key)
        st.write("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()