from flask import Flask, render_template, Response
from ultralytics import YOLO
import cv2
import serial
import time
import requests

# ==========================================
# FIREBASE
 # ==========================================

try:

    from firebase_config import save_to_firebase

    FIREBASE_ENABLED = True

    print("Firebase Connected")

except Exception as e:

    FIREBASE_ENABLED = False

    print("Firebase Disabled:", e)

# ==========================================
# TELEGRAM CONFIG
# ==========================================

BOT_TOKEN = "8358528115:AAGQJPh03W7hM6Iu-MpziQYdyglhjwQQ2m8"

CHAT_ID = "6119059969"

def send_telegram(message):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {

        "chat_id": CHAT_ID,

        "text": message
    }

    try:

        requests.post(
            url,
            data=payload,
            timeout=5
        )

        print("Telegram Sent")

    except Exception as e:

        print("Telegram Error:", e)

# ==========================================
# ARDUINO CONNECTION
# ==========================================

try:

    arduino = serial.Serial('COM5', 9600)

    time.sleep(2)

    arduino_connected = True

    print("Arduino Connected")

except Exception as e:

    arduino_connected = False

    print("Arduino Not Connected:", e)

# ==========================================
# LOAD YOLO MODEL
# ==========================================

model = YOLO("yolov8n.pt")

print("YOLO Model Loaded")

# ==========================================
# CAMERA
# ==========================================

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():

    print("Camera Not Opened")

    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

cap.set(cv2.CAP_PROP_FPS, 30)

print("Camera Started Successfully")

# ==========================================
# FLASK APP
# ==========================================

app = Flask(__name__)

# ==========================================
# MEMORY VARIABLES
# ==========================================

last_status = ""

last_person_count = -1

# ==========================================
# VIDEO GENERATOR
# ==========================================

def generate_frames():

    global last_status
    global last_person_count

    while True:

        success, frame = cap.read()

        if not success:
            continue

        # ==========================================
        # IMAGE IMPROVEMENT
        # ==========================================

        frame = cv2.convertScaleAbs(
            frame,
            alpha=1.1,
            beta=10
        )

        # ==========================================
        # YOLO DETECTION
        # ==========================================

        results = model.track(

            frame,

            conf=0.35,

            imgsz=640,

            classes=[0],

            persist=True,

            tracker="bytetrack.yaml",

            verbose=False
        )

        person_count = 0

        counted_ids = set()

        # ==========================================
        # PROCESS DETECTIONS
        # ==========================================

        for r in results:

            if r.boxes is None:
                continue

            for box in r.boxes:

                cls = int(box.cls[0])

                confidence = float(box.conf[0])

                if cls != 0:
                    continue

                x1, y1, x2, y2 = map(
                    int,
                    box.xyxy[0]
                )

                # ==========================================
                # FILTER FALSE DETECTIONS
                # ==========================================

                w = x2 - x1

                h = y2 - y1

                area = w * h

                frame_area = frame.shape[0] * frame.shape[1]

                # REMOVE SMALL FALSE DETECTIONS
                if area < 2500:
                    continue

                # REMOVE HUGE FALSE DETECTIONS
                if area > frame_area * 0.70:
                    continue

                # ==========================================
                # TRACK ID
                # ==========================================

                if box.id is not None:

                    track_id = int(box.id[0])

                else:

                    continue

                # COUNT UNIQUE IDS
                if track_id not in counted_ids:

                    counted_ids.add(track_id)

                    person_count += 1

                # ==========================================
                # DRAW BOX
                # ==========================================

                cv2.rectangle(

                    frame,

                    (x1, y1),

                    (x2, y2),

                    (0,255,0),

                    2
                )

                cv2.putText(

                    frame,

                    "PERSON",

                    (x1, y1 - 10),

                    cv2.FONT_HERSHEY_SIMPLEX,

                    0.7,

                    (0,255,0),

                    2
                )

                cv2.putText(

                    frame,

                    f"{confidence:.2f}",

                    (x1, y2 + 20),

                    cv2.FONT_HERSHEY_SIMPLEX,

                    0.5,

                    (255,255,0),

                    2
                )

        # ==========================================
        # LIGHT STATUS
        # ==========================================

        if person_count > 0:

            status = "LIGHT ON"

            status_color = (0,255,0)

            if arduino_connected:

                arduino.write(b'1')

        else:

            status = "LIGHT OFF"

            status_color = (0,0,255)

            if arduino_connected:

                arduino.write(b'0')

        # ==========================================
        # TELEGRAM + FIREBASE
        # ==========================================

        if status != last_status or person_count != last_person_count:

            message = f"""
SMART CLASSROOM UPDATE

People Present : {person_count}

Status : {status}
"""

            send_telegram(message)

            if FIREBASE_ENABLED:

                save_to_firebase(
                    person_count,
                    status
                )

            last_status = status

            last_person_count = person_count

        # ==========================================
        # DASHBOARD
        # ==========================================

        cv2.rectangle(

            frame,

            (0,0),

            (150,50),

            (20,20,20),

            -1
        )

        cv2.putText(

            frame,

            f"TOTAL PERSONS : {person_count}",

            (8,20),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.45,

            (0,255,255),

            2
        )

        cv2.putText(

            frame,

            status,

            (8,40),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.45,

            status_color,

            1
        )

        # ==========================================
        # CONVERT FRAME
        # ==========================================

        ret, buffer = cv2.imencode(
            '.jpg',
            frame
        )

        frame = buffer.tobytes()

        yield (

            b'--frame\r\n'

            b'Content-Type: image/jpeg\r\n\r\n' +

            frame +

            b'\r\n'
        )

# ==========================================
# HOME PAGE
# ==========================================

@app.route('/')

def index():

    return render_template('index.html')

# ==========================================
# VIDEO FEED
# ==========================================

@app.route('/video_feed')

def video_feed():

    return Response(

        generate_frames(),

        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

# ==========================================
# MAIN
# ==========================================

if __name__ == '__main__':

    print("================================")

    print("SMART CLASSROOM STARTED")

    print("Open Browser:")

    print("http://127.0.0.1:5000")

    print("================================")

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=False

      
    )