# Smart Classroom Automation System

## 1. Overview

The Smart Classroom Automation System is an AI and IoT-based solution designed to automate classroom monitoring and energy management. The system uses computer vision techniques to detect classroom occupancy in real time and automatically controls lighting through Arduino-based automation.

By combining artificial intelligence, cloud services, and embedded hardware, the system reduces energy consumption while providing real-time monitoring, notifications, and historical occupancy records.

---

## 2. Features

### 2.1 Occupancy Detection

* Real-Time Person Detection
* Multi-Person Tracking
* Occupancy Monitoring
* Live Person Counting

### 2.2 Automation Features

* Automatic Light ON/OFF Control
* Arduino-Based Device Automation
* Serial Communication Integration
* Energy Consumption Reduction

### 2.3 Monitoring and Alerts

* Live Video Streaming Dashboard
* Real-Time Classroom Status Monitoring
* Telegram Notifications
* Event-Based Alerts

### 2.4 Cloud Integration

* Firebase Firestore Integration
* Occupancy Data Logging
* Classroom Activity Records
* Cloud-Based Storage

---

## 3. Technology Stack

### 3.1 Artificial Intelligence and Computer Vision

* YOLOv8
* ByteTrack
* OpenCV

### 3.2 Backend

* Python
* Flask

### 3.3 Hardware

* Arduino
* USB Serial Communication

### 3.4 Cloud Services

* Firebase Firestore
* Telegram Bot API

### 3.5 Frontend

* HTML
* CSS
* JavaScript

---

## 4. Project Structure

```text
classroom/
│
├── main.py
├── firebase_config.py
├── firebase_key.json
├── yolov8n.pt
├── yolov8s.pt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── .venv/
```

---

## 5. AI Model Used

### 5.1 Model

YOLOv8 Nano (yolov8n.pt)

### 5.2 Purpose

The YOLOv8 model is used for real-time person detection from classroom video streams.

### 5.3 Why YOLOv8?

* High detection accuracy
* Real-time processing capability
* Lightweight and efficient
* Suitable for CPU-based deployment
* Low latency for live monitoring systems

### 5.4 Tracking Algorithm

ByteTrack is used to track detected individuals and assign unique IDs, preventing duplicate counting and improving occupancy accuracy.

---

## 6. System Workflow

### Step 1

The webcam captures live classroom video.

### Step 2

YOLOv8 processes each frame and detects people present in the classroom.

### Step 3

ByteTrack tracks individuals and calculates the total occupancy count.

### Step 4

The system evaluates classroom occupancy status.

### Step 5

If one or more people are detected:

* Lights are turned ON through Arduino.

### Step 6

If no people are detected:

* Lights are turned OFF automatically.

### Step 7

Occupancy information is stored in Firebase Firestore.

### Step 8

Telegram notifications are sent whenever classroom status changes.

### Step 9

The processed video stream is displayed on the Flask web dashboard.

---

## 7. Core Modules

### 7.1 Video Processing Module

* Webcam Integration
* Frame Processing
* Object Detection
* Person Counting

### 7.2 Automation Module

* Arduino Communication
* Light Control Logic
* Serial Port Management

### 7.3 Cloud Module

* Firebase Connectivity
* Data Logging
* Historical Record Management

### 7.4 Notification Module

* Telegram Bot Integration
* Status Change Alerts
* Event Notifications

### 7.5 Dashboard Module

* Live Video Streaming
* Occupancy Display
* System Status Monitoring

---

## 8. Installation and Setup

### 8.1 Clone the Repository

```bash
git clone <repository-url>
cd classroom
```

### 8.2 Create Virtual Environment

```bash
python -m venv .venv
```

### 8.3 Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

### 8.4 Install Dependencies

```bash
pip install -r requirements.txt
```

### 8.5 Hardware Setup

* Connect the webcam.
* Connect the Arduino board.
* Verify the configured serial port in the application.

### 8.6 Run the Application

```bash
python main.py
```

---

## 9. Dashboard Access

After starting the application, open the following URL in your browser:

```text
http://127.0.0.1:5000
```

The dashboard displays:

* Live Video Feed
* Person Count
* Occupancy Status
* Light Status

---

## 10. Applications

1. Smart Classrooms
2. Educational Institutions
3. Smart Buildings
4. Energy Management Systems
5. Occupancy Monitoring Solutions
6. IoT Automation Projects
7. Office Space Monitoring

---

## 11. Benefits

* Reduces Energy Consumption
* Automates Classroom Management
* Provides Real-Time Monitoring
* Improves Resource Utilization
* Generates Occupancy Analytics
* Enables Remote Notifications

---

## 12. Future Enhancements

1. Multi-Classroom Monitoring
2. Mobile Application Integration
3. Attendance Management System
4. Cloud Dashboard Analytics
5. HVAC Automation
6. Face Recognition-Based Attendance
7. Advanced Occupancy Prediction

---

## 13. Developed Using

* Python
* Flask
* OpenCV
* YOLOv8
* ByteTrack
* Arduino
* Firebase Firestore
* Telegram Bot API

---<img width="1787" height="870" alt="Screenshot 2026-05-22 121212" src="https://github.com/user-attachments/assets/100d57e1-0eb3-4a55-be0d-52b02bfc0a6c" />
<img width="1533" height="950" alt="Screenshot 2026-05-22 122756" src="https://github.com/user-attachments/assets/605daeed-f6e3-4f13-abf3-842310c40c55" />
<img width="1280" height="960" alt="image" src="https://github.com/user-attachments/assets/4e49e3e8-7faf-4189-a3d7-e8162ea33c33" />





