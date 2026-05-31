# 🎨 Pencil Sketch Generator

A Python-based image processing project that converts normal images into realistic pencil sketch artwork using OpenCV techniques. This project demonstrates fundamental computer vision concepts in a simple and beginner-friendly way.

---

# 📌 Project Overview

The Pencil Sketch Generator is a computer vision application built using Python and OpenCV. It allows users to select any image from their system and automatically converts it into a pencil sketch.

The project focuses on understanding key image processing operations such as:

Grayscale conversion
Image inversion
Gaussian blur
Image blending (dodging technique)

A simple Tkinter-based file picker is used for easy image selection, making the tool user-friendly and interactive.

---

# 🚀 Features

✅ Convert normal images into pencil sketches

✅ Simple and beginner-friendly project

✅ Supports multiple image formats:

* JPG
* JPEG
* PNG
* BMP
* WEBP

✅ Automatic sketch image generation

✅ Lightweight and fast execution

✅ GUI-based image selection using Tkinter

✅ Realistic sketch effect using OpenCV

---

# 🛠️ Technologies Used

| Technology | Purpose              |
| ---------- | -------------------- |
| Python     | Programming Language |
| OpenCV     | Image Processing     |
| Tkinter    | GUI File Selection   |
| Pathlib    | File Path Management |

---

# 📂 Project Structure

```bash
pencil-sketch-generator/
│
├── sketch.py
├── README.md
├── requirements.txt
├── sample_input.jpg
├── Output_sketch.png
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/pencil-sketch-generator.git
cd pencil-sketch-generator
```

---

## 2️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# ▶️ How to Run

Run the project using:

```bash
python sketch.py
```

### Steps:

1. Open the application
2. Select any image from your computer
3. The image gets converted into a pencil sketch
4. The sketch output is saved automatically

---

# 🧠 Image Processing Workflow

The sketch effect is generated using the following steps:

* Read Image
* Convert Image to Grayscale
* Invert the Grayscale Image
* Apply Gaussian Blur
* Invert the Blurred Image
* Blend Images using Division Technique

These operations together create a realistic pencil drawing appearance.

---

# 📸 Output Examples

---

# Example 1 — Virat Kohli Image

## 🖼️ Original Image

<p align="center">
 <img width="500" height="500" alt="Screenshot 2026-05-31 112342" src="https://github.com/user-attachments/assets/a473cdc3-af75-4334-ab4e-7bd4657f0ca8"width="250" />

</p>

## ✏️ Pencil Sketch Output

<p align="center">
<img width="500" height="500" alt="Screenshot 2026-05-31 112342_sketch" src="https://github.com/user-attachments/assets/5d78676b-def6-4217-9a62-f8040a621db4"width="250"/>

</p>

---

# Example 2 — Anime Character Image

## 🖼️ Original Image -----------------> ✏️Pencil Sketch Output

<p align="center">
  <img width="500" height="500" alt="Screenshot 2026-05-28 225819" src="https://github.com/user-attachments/assets/843d1b0d-ca08-4247-90ab-f0d87bc94134"width="250/>



</p>

---


## ✏️ Pencil Sketch Output

<p align="center">
  <img width="500" height="500" alt="Screenshot 2026-05-28 225819_sketch" src="https://github.com/user-attachments/assets/867fad67-2995-4fc3-a7b7-8bc655bc15e1"width="250"/>


</p>

---

# 📚 Learning Outcomes

This project helps in understanding:

* OpenCV basics
* Image preprocessing techniques
* Grayscale transformations
* Gaussian blur operations
* Image blending methods
* File handling in Python
* GUI integration using Tkinter

---

# 🔮 Future Improvements

🚀 Add real-time webcam sketch generation

🚀 Create a desktop GUI application

🚀 Add multiple artistic filters

🚀 Export sketches in different resolutions

🚀 Build a web version using Flask or Streamlit

---

# 🤝 Contributing

Contributions are welcome!

To contribute:

1. Fork the repository
2. Create a new branch
3. Make changes
4. Submit a pull request

---

# 📜 License

This project is open-source and available under the MIT License.

---

# 👨‍💻 Author

## Ritesh Deshmukh


---
