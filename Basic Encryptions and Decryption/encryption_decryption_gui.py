import tkinter as tk
from tkinter import messagebox
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# Encryption and Decryption Functions
def generate_key_iv():
    key = os.urandom(32)  # AES-256 key
    iv = os.urandom(16)   # AES block size
    return key, iv

def encrypt_message(key, iv, plaintext):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext.encode()) + padder.finalize()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    return ciphertext

def decrypt_message(key, iv, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext.decode()

# GUI Application
class EncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Encryption and Decryption App")

        self.key, self.iv = generate_key_iv()

        # Input for plaintext
        self.plaintext_label = tk.Label(root, text="Plaintext:")
        self.plaintext_label.pack(pady=5)
        self.plaintext_entry = tk.Entry(root, width=50)
        self.plaintext_entry.pack(pady=5)

        # Encrypt button
        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt)
        self.encrypt_button.pack(pady=5)

        # Encrypted output
        self.encrypted_label = tk.Label(root, text="Encrypted Text:")
        self.encrypted_label.pack(pady=5)
        self.encrypted_output = tk.Entry(root, width=50)
        self.encrypted_output.pack(pady=5)

        # Decrypt button
        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt)
        self.decrypt_button.pack(pady=5)

        # Decrypted output
        self.decrypted_label = tk.Label(root, text="Decrypted Text:")
        self.decrypted_label.pack(pady=5)
        self.decrypted_output = tk.Entry(root, width=50)
        self.decrypted_output.pack(pady=5)

    def encrypt(self):
        plaintext = self.plaintext_entry.get()
        if not plaintext:
            messagebox.showerror("Input Error", "Please enter plaintext to encrypt.")
            return

        ciphertext = encrypt_message(self.key, self.iv, plaintext)
        self.encrypted_output.delete(0, tk.END)
        self.encrypted_output.insert(0, ciphertext.hex())

    def decrypt(self):
        encrypted_text = self.encrypted_output.get()
        if not encrypted_text:
            messagebox.showerror("Input Error", "Please encrypt some text first.")
            return

        try:
            ciphertext = bytes.fromhex(encrypted_text)
            decrypted_message = decrypt_message(self.key, self.iv, ciphertext)
            self.decrypted_output.delete(0, tk.END)
            self.decrypted_output.insert(0, decrypted_message)
        except Exception as e:
            messagebox.showerror("Decryption Error", f"An error occurred: {e}")

# Main Function
if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionApp(root)
    root.mainloop()
