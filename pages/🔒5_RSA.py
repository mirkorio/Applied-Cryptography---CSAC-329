import streamlit as st

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# RSA Algorithm functions
 
def gcd(a, b):
    gcd_val = 0
    for i in range(1, min(a, b) + 1):
        if (a % i == 0) and (b % i == 0):
            gcd_val = i
    return gcd_val

def e_value(fin):
    e_val = 0 
    for i in range(2, fin):
        if gcd(i, fin) == 1:
            e_val = i
            break
    return e_val

def d_value(phi_n_val, e_val):
    d_val = 0
    for i in range(1, 10000):
        if e_val != 0:  # Add a check to avoid division by zero
            d_val = int((1 + i * phi_n_val) / e_val)
            if 1 < d_val < phi_n_val and (e_val * d_val) % phi_n_val == 1:
                break
    return d_val

def encrypt_message(message, e, n):
    encrypted_chars = [(ord(char) ** e) % n for char in message]
    return encrypted_chars

def decrypt_message(encrypted_message, d, n):
    decrypted_chars = [chr((char ** d) % n) for char in encrypted_message]
    return ''.join(decrypted_chars)

# Streamlit app
st.header("RSA - Encryption and Decryption")
st.markdown("""<div style="background-color:#222831;padding:10px;border-radius:10px">
    <p style="text-align: justify; color: white;">RSA (Rivest-Shamir-Adleman) is one of the first public-key cryptosystems and is widely used for secure data transmission. It was invented by Ron Rivest, Adi Shamir, and Leonard Adleman in 1977 while they were at MIT. The RSA algorithm involves generating a public-private key pair, where the public key can be freely distributed and used for encryption, while the private key is kept secret and used for decryption. The security of RSA relies on the practical difficulty of factoring the product of two large prime numbers, the “factoring problem”.</p>
    </div>""", unsafe_allow_html=True)
st.write("---")

p = st.number_input("Enter Value of p (Large Prime Number):", min_value=2, step=1)
q = st.number_input("Enter Value of q (Large Prime Number):", min_value=2, step=1)

if not is_prime(p):
    st.error(f"p: {p} is not a prime number!")
if not is_prime(q):
    st.error(f"q: {q} is not a prime number!")

if is_prime(p) and is_prime(q):
    message = st.text_input("Enter Message:", value="Hello world!", key="message_input")

    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = e_value(phi_n)
    d = d_value(phi_n, e)

    public_key = "Public Key: ("'e = ' + str(e) + ","'n = ' + str(n) + ")"
    private_key = "Private Key: ("'d = ' + str(d) + ","'n = ' + str(n) + ")"

    st.write(public_key)
    st.write(private_key)

    if st.button("Encrypt Message"):
        encrypted_message = encrypt_message(message, e, n)
        st.write("Encrypted Text:", encrypted_message)

    private_key_input = st.text_input("Enter the private key to decrypt the message (format: d,n)")
    private_key_parts = private_key_input.split(",")

    if len(private_key_parts) == 2:
        if st.button("Decrypt Message"):
            private_key_d = int(private_key_parts[0])
            private_key_n = int(private_key_parts[1])

            if private_key_d == d and private_key_n == n:
                encrypted_message = encrypt_message(message, e, n)
                decrypted_message = decrypt_message(encrypted_message, d, n)
                st.write("Plain text:", decrypted_message)
            else:
                st.error("Invalid private key!") 