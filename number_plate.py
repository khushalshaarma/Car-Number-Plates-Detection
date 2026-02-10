import cv2
import pytesseract
import requests
import re
import json

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# RoadAPI credentials
CLIENT_ID = "AC0h09J1XL_NYg26AG"
CLIENT_KEY = "533b4c2330323ffb642cb2bc19b51ff0"
API_URL = "https://api.roadapi.in/vehicle/reg/details"

# Function: extract plate-like region and run OCR
def extract_plate_text(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(gray, 30, 200)

    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    plate_img = None
    for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * peri, True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            plate_img = img[y:y+h, x:x+w]
            break

    if plate_img is None:
        return None

    text = pytesseract.image_to_string(plate_img, config='--psm 8')
    match = re.search(r'[A-Z]{2}\d{1,2}[A-Z]{1,3}\d{3,4}', text.replace(" ", "").upper())
    return match.group(0) if match else None

# Function: call vehicle detail API
def get_vehicle_details(plate_number):
    headers = {
        "Client-ID": CLIENT_ID,
        "Client-Key": CLIENT_KEY,
        "Content-Type": "application/json"
    }
    body = {"reg_no": plate_number}
    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(body), timeout=5)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Start camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not access webcam.")
    exit()

print("[INFO] Starting plate detection... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    plate_number = extract_plate_text(frame)
    if plate_number:
        print(f"\n[Plate]: {plate_number}")
        details = get_vehicle_details(plate_number)
        print("[Vehicle Details]:", json.dumps(details, indent=2))
        cv2.putText(frame, plate_number, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Draw preview
    resized = cv2.resize(frame, (800, 600))
    cv2.imshow("Live Plate Detection", resized)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
