# 🚁 Gesture Controlled Drone Simulation

A real-time drone simulation controlled using **hand gestures** detected by **OpenCV** and **MediaPipe**. This project demonstrates how computer vision can be used as a natural user interface for controlling a virtual drone without a keyboard or joystick.
---

## 📸 Demo

> Add a GIF or screenshot here.

```
demo.gif
```

---

## ✨ Features

- 🖐️ Real-time hand tracking using MediaPipe
- 📷 Live webcam input with OpenCV
- 🎮 Gesture-based drone control
- 🚁 Simple drone simulation using Pygame
- ⚡ Low latency and real-time performance
- 🧩 Modular project structure

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core Programming |
| OpenCV | Webcam & Image Processing |
| MediaPipe | Hand Landmark Detection |
| Pygame | Drone Simulation |
| NumPy | Numerical Operations |

---

## 📂 Project Structure

```
Gesture-Controlled-Drone/
│
├── main.py                # Main simulation
├── hand_tracking.py       # MediaPipe hand detection
├── gesture.py             # Gesture recognition logic
├── requirements.txt
├── README.md
└── screenshots/
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/gesture-controlled-drone.git
```

Go to the project

```bash
cd gesture-controlled-drone
```

Install dependencies

```bash
pip install opencv-python mediapipe pygame numpy
```

---

## ▶️ Run

```bash
python main.py
```

---

## 🎮 Gesture Controls

| Gesture | Action |
|---------|--------|
| ☝️ Index Finger Up | Move Up |
| 👇 Index Finger Down | Move Down |
| 👈 Index Finger Left | Move Left |
| 👉 Index Finger Right | Move Right |
| ✋ No Movement | Hover |

---

## 🧠 How It Works

1. OpenCV captures frames from the webcam.
2. MediaPipe detects 21 hand landmarks.
3. The gesture recognition module analyzes landmark positions.
4. Commands are generated based on the index finger location.
5. Pygame updates the drone position in real time.

```
Webcam
   │
   ▼
OpenCV
   │
   ▼
MediaPipe Hand Tracking
   │
   ▼
Gesture Recognition
   │
   ▼
Drone Controller
   │
   ▼
Pygame Simulation
```

---

## 📦 Dependencies

- Python 3.10+
- OpenCV
- MediaPipe
- Pygame
- NumPy

---

## 🌟 Planned Features

- ✅ Better gesture recognition
- 🚁 Realistic drone physics
- 🌍 Open-world environment using Three.js
- 🎥 First-person (FPV) camera
- 🎮 Drone takeoff and landing gestures
- 🤖 AI-powered object detection (YOLO)
- 🛰️ GPS and waypoint navigation
- 🌤️ Weather effects
- 🌙 Day/Night cycle
- 🏢 3D buildings and terrain
- 🌐 Web dashboard with FastAPI
- 📱 Mobile gesture control
- 🧭 Autonomous flight mode
- 🎯 Mission system
- ☁️ Cloud data logging

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Devraj**

- GitHub: https://github.com/devv2308

---

### ⭐ If you found this project useful, consider giving it a Star!
