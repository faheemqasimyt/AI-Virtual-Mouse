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
