import cv2
import numpy as np
import os
import tkinter as tk
from tkinter import ttk, messagebox

def int_to_bits(num, bit_length):
    return [int(b) for b in format(num, f'0{bit_length}b')]

def str_to_bits(s):
    bits = []
    for char in s:
        bits.extend([int(b) for b in format(ord(char), '08b')])
    return bits

def embed_data(image, data_bits):
    flat = image.flatten()
    if len(data_bits) > len(flat):
        raise ValueError("Data too large to embed in this image!")
    for i in range(len(data_bits)):
        flat[i] = (flat[i] & 254) | data_bits[i]
        flat[i] = np.clip(flat[i], 0, 255)
    return flat.reshape(image.shape)

def encrypt():
    img_path = "wallpaper.png"
    if not os.path.exists(img_path):
        messagebox.showerror("Error", "Input image 'wallpaper.png' not found!")
        return
    image = cv2.imread(img_path)
    if image is None:
        messagebox.showerror("Error", "Failed to load 'wallpaper.png'.")
        return

    secret_message = secret_message_entry.get()
    passcode = passcode_entry.get()
    if not secret_message or not passcode:
        messagebox.showerror("Error", "Secret message and passcode cannot be empty!")
        return

    header_bits = []
    header_bits.extend(int_to_bits(len(passcode), 16))
    header_bits.extend(str_to_bits(passcode))
    header_bits.extend(int_to_bits(len(secret_message), 32))
    header_bits.extend(str_to_bits(secret_message))

    try:
        encoded_image = embed_data(image, header_bits)
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return

    output_path = "encrypted.png"
    cv2.imwrite(output_path, encoded_image)
    messagebox.showinfo("Success", f"Encryption complete! Saved as '{output_path}'.")

root = tk.Tk()
root.title("Steganography - Encrypt")
root.geometry("400x300")
style = ttk.Style(root)
style.theme_use('clam')

frame = ttk.Frame(root, padding="20")
frame.pack(expand=True)

ttk.Label(frame, text="Enter Secret Message:").grid(row=0, column=0, sticky="w", pady=5)
secret_message_entry = ttk.Entry(frame, width=40)
secret_message_entry.grid(row=1, column=0, pady=5)

ttk.Label(frame, text="Enter Passcode:").grid(row=2, column=0, sticky="w", pady=5)
passcode_entry = ttk.Entry(frame, width=40, show="*")
passcode_entry.grid(row=3, column=0, pady=5)

encrypt_button = ttk.Button(frame, text="Encrypt", command=encrypt)
encrypt_button.grid(row=4, column=0, pady=20)

root.mainloop()