from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

@app.route(rule='/')
def index():
    return render_template(template_name_or_list='/index.html')

def generate():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(src=frame, flipCode=1)
        ret, buffer = cv2.imencode(ext='.jpg', img=frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def objDetection():
    imcap = cv2.VideoCapture(index=0)  # 0 for builtin webcam, 1 or -1 for the externals
    imcap.set(propId=3, value=640)  # set width as 640
    imcap.set(propId=4, value=480)  # set height as 480

    faceCascade = cv2.CascadeClassifier(
        filename=cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    while True:
        img = imcap.read()

        # converting image from color to grayscale
        imgGray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

        # Getting corners around the face
        faces = faceCascade.detectMultiScale(image=imgGray, scaleFactor=1.3, minNeighbors=5)

        # drawing bounding box around face
        for x, y, w, h in faces:
            # Print bounding box coordinates
            print(f"Face detected at (x, y) = ({x}, {y})")
            print(f"Bounding box dimensions (w, h) = ({w}, {h})")

            # Calculate center of the face
            center_x = x + w // 2
            center_y = y + h // 2
            print(f"Center of the face: ({center_x}, {center_y})")

            # Calculate area of the bounding box
            area = w * h
            print(f"Area of bounding box: {area} pixels")

            img = cv2.rectangle(img=img, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=3)

        frame = cv2.flip(src=img, flipCode=1)
        ret, buffer = cv2.imencode(ext='.jpg', img=frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route(rule='/video')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(response=objDetection(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, threaded=True, port=5000)
