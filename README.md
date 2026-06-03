# 🎓 Smart Classroom Automation System

## Overview

The Smart Classroom Automation System is an IoT and AI-powered solution designed to automate classroom management and reduce energy consumption. The system uses computer vision techniques to detect human presence in real time and automatically controls classroom lighting through Arduino-based automation.

## Features

* Real-Time Person Detection using YOLOv8
* Multi-Person Tracking with ByteTrack
* Automatic Light ON/OFF Control
* Arduino Integration via Serial Communication
* Firebase Cloud Data Logging
* Telegram Notifications and Alerts
* Live Video Streaming Dashboard
* Occupancy Monitoring
* Real-Time Classroom Status Updates

## Working Diagram

Webcam → YOLOv8 Detection → ByteTrack Tracking → Person Count

↓

Arduino Light Control (ON/OFF)

↓

Firebase Logging + Telegram Alerts

↓

Flask Web Dashboard

## Technology Stack

### Artificial Intelligence & Computer Vision

* YOLOv8
* ByteTrack
* OpenCV

### Backend

* Python
* Flask

### Hardware

* Arduino
* Serial Communication

### Cloud Services

* Firebase Firestore
* Telegram Bot API

### Frontend

* HTML
* CSS
* JavaScript

## Project Objective

To automate classroom lighting and monitoring using AI-based occupancy detection, reducing energy wastage while providing real-time tracking, notifications, and cloud-based logging.

## System Workflow

1. Webcam captures live classroom video.
2. YOLOv8 detects people in real time.
3. ByteTrack tracks individuals and counts occupants.
4. If people are detected, lights turn ON.
5. If the classroom is empty, lights turn OFF.
6. Occupancy data is stored in Firebase.
7. Telegram alerts notify status changes.
8. Flask dashboard displays the live video feed.

## Applications

* Smart Classrooms
* Smart Buildings
* Energy Management Systems
* Occupancy Monitoring
* IoT Automation Projects

