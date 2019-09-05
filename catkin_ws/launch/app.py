#!/usr/bin/env python
from flask import Flask, render_template, Response
import images
import cv2
from time import sleep
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def vid_gen():
    while True:
        sleep(0.0416)
        img=images.image['color']
        if img is not None:
            frame = cv2.imencode('.jpeg', img)[1].tostring() 
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



@app.route('/video_feed')
def video_feed():
    return Response(vid_gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002, debug=False)