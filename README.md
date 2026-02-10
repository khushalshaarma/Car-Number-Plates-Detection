Live Number Plate Detection & Vehicle Details (Python)

A real-time system that detects vehicle number plates from a webcam feed using OpenCV, extracts text with Tesseract OCR, and fetches vehicle details using RoadAPI.

📌 Overview

This project captures live video from your camera, detects the number plate region, performs OCR to read the plate number, and retrieves vehicle information via an external API.
It’s useful for smart parking, traffic monitoring, and basic surveillance demos.

✨ Features

Real-time webcam capture

Number plate detection using contours

OCR text extraction (Tesseract)

Regex validation for Indian plate format

Vehicle details fetched using RoadAPI

Live display of detected plate on screen

🧰 Tech Stack

Language: Python

Computer Vision: OpenCV

OCR: Tesseract

API: RoadAPI

HTTP Client: Requests

Pattern Matching: Regex

💻 Requirements

Python 3.8 or higher

Webcam

Internet connection

Tesseract OCR installed

📥 Installation

Clone the repository:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name


Install dependencies:

pip install opencv-python pytesseract requests


Install Tesseract OCR (Windows):

https://github.com/UB-Mannheim/tesseract/wiki

⚙️ Configuration

Set Tesseract path in your Python file:

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


Add your RoadAPI credentials:

CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_KEY = "YOUR_CLIENT_KEY"

▶️ How to Run
python main.py


Controls:

Press q to quit the webcam window

🔁 Workflow
Webcam Feed
     ↓
Image Preprocessing (Gray + Blur + Edges)
     ↓
Contour Detection (Plate Region)
     ↓
OCR (Tesseract)
     ↓
Regex Validation
     ↓
RoadAPI Request
     ↓
Display Vehicle Details

📤 Output

Live video window

Detected number plate shown on screen

Vehicle details printed in terminal

⚠️ Limitations

OCR accuracy depends on lighting and camera angle

API free tier has request limits

Not optimized for high-speed moving vehicles

🚀 Future Improvements

Deep learning-based plate detection

Save detected vehicles to database

Web dashboard (Flask/React)

Mobile camera integration
