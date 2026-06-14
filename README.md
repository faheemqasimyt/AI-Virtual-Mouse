# AI Virtual Mouse

A virtual mouse controlled by hand gestures using computer vision. The project uses MediaPipe for hand tracking and PyAutoGUI to simulate mouse actions.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Download the Model](#download-the-model)
- [Usage](#usage)
- [Gestures](#gestures)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)

## Features

- Move the cursor with a single finger.
- Left click by pinching thumb and index finger.
- Right click by pinching thumb and middle finger.
- Scroll by raising index and middle fingers and moving them up or down.
- Smooth cursor movement with configurable smoothing.
- Works with the latest MediaPipe Tasks API.

## Requirements

- Python 3.8 or higher
- OpenCV
- MediaPipe (latest)
- PyAutoGUI
- NumPy

## Installation

1. Clone the repository or download the source files.

2. Install the required Python packages:

   ```bash
   pip install opencv-python mediapipe pyautogui numpy uv 