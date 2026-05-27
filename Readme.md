# 🔢 MNIST Handwritten Digit Classification App

An interactive web application built with Deep Learning and Streamlit to recognize handwritten digits (0–9) from the classic MNIST dataset. The project features full model inference, modular helper utilities, and containerization support using Docker.

---

# 🚀 Features

* ✍️ **Real-time Canvas Drawing:** Draw digits directly on the screen for instant prediction.
* 📈 **Probability Breakdown:** Visualized confidence bars showing the model's top predictions.
* 🛠️ **Modular Architecture:** Clean separation between the core ML logic and the Streamlit UI presentation layer.
* 🐳 **Dockerized Deployment:** Fully containerized setup for easy multi-platform shipping and execution.

---

# 🧠 Tech Stack

* Python
* Streamlit (Frontend User Interface)
* PyTorch / Keras (Deep Learning Backbone)
* NumPy & OpenCV / Pillow (Image Preprocessing)
* Docker

---

# 📂 Project Structure

```bash
Minst_ML/
│
├── model/            # Directory containing the saved weights/architecture (e.g., .pt, .h5, or .keras)
├── app.py            # Streamlit application (UI configuration, controls, and layout)
├── Dockerfile        # Containerization instructions
├── Readme.md         # Project documentation
├── requirements.txt  # Python environment dependencies
└── utils.py          # Core helper functions (image preprocessing, model loading, and inference)