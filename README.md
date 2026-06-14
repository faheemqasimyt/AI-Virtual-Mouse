# AI Virtual Mouse - Hand Gesture Controlled Computer Vision Project

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5%2B-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-latest-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Build](https://img.shields.io/badge/build-passing-brightgreen)

Control your computer mouse cursor using only hand gestures – no physical mouse required! This AI-powered system uses a standard webcam, real-time hand tracking with MediaPipe, and custom deep learning models (Keras/PyTorch) to translate hand poses into mouse actions.

---

##  Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [System Architecture](#-system-architecture)
- [Tech Stack & Libraries](#-tech-stack--libraries)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [Gesture Mapping](#-gesture-mapping)
- [Configuration](#-configuration)
- [Custom Model Training (Optional)](#-custom-model-training-optional)
- [Troubleshooting](#-troubleshooting)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)

---

##  Overview

The **AI Virtual Mouse** enables hands‑free control of the computer by interpreting finger and hand gestures captured from a live camera feed. It combines:

- **Real‑time hand landmark detection** (MediaPipe)
- **Gesture classification** using deep learning (Keras / PyTorch)
- **System‑level mouse control** via `pynput`
- **Data analysis & visualisation** for gesture statistics (NumPy, Pandas, Matplotlib)

The project is designed to be modular: you can use the pre‑trained gesture model or train your own with your custom gestures.

---

## Features

- **Mouse movement** – move the cursor by moving your hand  
- **Left click, right click, double click, drag & drop**  
- **Scroll up / scroll down**  
- **Volume / brightness control** (optional)  
- **Multi‑hand support**  
- **Calm, silent, non‑contact control**  
- **Custom gesture training pipeline** (Keras / PyTorch)  
- **Live visualization** of landmarks and recognised gesture  
- **Configurable sensitivity & gesture cooldown**  
- **Cross‑platform** (Windows, macOS, Linux)

---

## Demo

> _Add your own GIF / screenshot / video link here_

*Example:*  
![virtual-mouse-demo](https://user-images.githubusercontent.com/your_demo.gif)

---

## System Architecture
┌──────────┐     ┌────────────┐     ┌────────────┐     ┌──────────┐
│  Webcam  │────▶│  MediaPipe │────▶│  Gesture   │────▶│  pynput  │
│ (Camera) │     │   Hands    │     │ Classifier │     │ (Mouse)  │
└──────────┘     └────────────┘     └────────────┘     └──────────┘
│                   ▲
│    Key‑point      │
▼    extraction     │
┌────────────┐            │
│  numpy/    │───────►────┘
│  pandas    │
└────────────┘


1. **Capture**: Frames are grabbed from the webcam using OpenCV.
2. **Landmarks**: MediaPipe Hands detects 21 3D hand landmarks.
3. **Feature Engineering**: Relative angles/distances are computed (NumPy).
4. **Classification**: A deep neural network (Keras or PyTorch) predicts the current gesture.
5. **Execution**: `pynput` translates the gesture into a mouse event (move, click, etc.).
6. **Monitoring**: Optional logging and analytics with Pandas / Matplotlib.

---

## 🛠️ Tech Stack & Libraries

| Library           | Purpose                                                       |
|-------------------|---------------------------------------------------------------|
| `opencv-python`   | Video capture, image processing, window rendering             |
| `mediapipe`       | Real‑time hand landmark detection                             |
| `pynput`          | Cross‑platform mouse and keyboard control                     |
| `numpy`           | Numerical operations, feature extraction                      |
| `pandas`          | Data handling, gesture logging, CSV export                    |
| `matplotlib`      | Visualising landmark data, gesture statistics                 |
| `python-dotenv`   | Environment variable management for API keys/config           |
| `tensorflow/keras`| Building, training, and loading gesture classification model  |
| `torch` (PyTorch) | Alternative deep learning framework for gesture models        |

> **Why both Keras and PyTorch?**  
> The project supports interchangeable back‑ends. A pre‑trained Keras model is provided for quick start, while a PyTorch implementation is available for researchers who prefer that ecosystem.

---

##  Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/faheemqasimyt/Ai-Virtual-Mouse.git
cd Ai-Virtual-Mouse
