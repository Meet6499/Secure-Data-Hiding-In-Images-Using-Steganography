# 🔐 Image Steganography Tool  

## 📌 Overview  
This project is a **Python-based steganography tool** that allows users to **hide and retrieve secret messages** inside images using **Least Significant Bit (LSB) steganography**. It provides a **password-protected encryption** mechanism to ensure **secure communication** and a **Tkinter GUI** for an easy-to-use interface.  

---

## ✨ Features  
✔️ **Secure Message Hiding** – Uses **LSB steganography** to embed hidden text inside images.  
✔️ **Password Protection** – Only users with the correct password can retrieve the hidden message.  
✔️ **Undetectable Data Concealment** – The image appears unchanged after encryption.  
✔️ **Supports PNG & JPEG** – Works with common image formats.  
✔️ **User-Friendly GUI** – Built with **Tkinter** for a simple and interactive experience.  

---

## 🛠️ Technologies Used  
🔹 **Python 3** – Core programming language  
🔹 **OpenCV** – Image processing and manipulation  
🔹 **NumPy** – Handling pixel data efficiently  
🔹 **Tkinter** – GUI for user interaction  

---

## 📥 Installation  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Meet6499/Secure-Data-Hiding-In-Images-Using-Steganography
cd Secure-Data-Hiding-In-Images-Using-Steganography
```

2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

3️⃣ Run the Encryption Script
```bash
python src/ToEncrypt.py
```

4️⃣ Run the Decryption Script
```bash
python src/ToDecrypt.py
```

---
## 🚀 How It Works?

### 🔹 Encryption Process  
1. **Load an input image** (e.g., `wallpaper.png`).  
2. **Enter a secret message and password** in the GUI.  
3. **The message is converted into binary** and embedded using LSB steganography.  
4. **The modified image is saved** as `encrypted.png`, containing the hidden message.  

### 🔹 Decryption Process  
1. **Open `encrypted.png`** using the decryption tool.  
2. **Enter the correct password** to extract the hidden message.  
3. **The hidden message is retrieved** and displayed securely.  

---

## 📜 License  
This project is licensed under the **MIT License** – free to use and modify!  

---

## 📌 Contributing  
Want to improve this project? Contributions are welcome!  

1. **Fork the repository**  
2. **Create a new branch**  
3. **Make changes & commit**  
4. **Submit a Pull Request**  

---

## 📩 Contact & Support  
📧 For any questions, feel free to open an **issue** or reach out via GitHub!  

