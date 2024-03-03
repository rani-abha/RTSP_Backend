from flask import Blueprint, request, jsonify, Response, render_template, current_app
from models import Overlay 
import cv2
import atexit
from flask_pymongo import PyMongo


mongo = PyMongo()


overlay_bp = Blueprint('overlay', __name__)

@overlay_bp.route('/overlay', methods=['POST'])
def create_overlay():
    data = request.json
    overlay = Overlay.from_dict(data)
    dictt = overlay.to_dict()
    print("Overlay dict: ", dictt)
    print(mongo.db, " ttttttttttttt", mongo.db.list_collection_names())
    mongo.db.overlays.insert_one(overlay.to_dict())
    return jsonify({'message': 'Overlay created successfully'}), 201

@overlay_bp.route('/overlay', methods=['GET'])
def get_overlays():
    overlays = mongo.db.overlays.find()
    if overlays:
        return jsonify([overlay for overlay in overlays]), 200
    return jsonify({'message': 'Overlay not found'}), 404

@overlay_bp.route('/overlay/<overlay_id>', methods=['GET'])
def get_overlay(overlay_id):
    overlay = mongo.db.overlays.find_one({"_id": overlay_id})
    if overlay:
        return jsonify(overlay), 200
    return jsonify({'message': 'Overlay not found'}), 404

@overlay_bp.route('/overlay/<overlay_id>', methods=['PUT'])
def update_overlay(overlay_id):
    data = request.json
    mongo.db.overlays.update_one({"_id": overlay_id}, {"$set": data})
    return jsonify({'message': 'Overlay updated successfully'}), 200

@overlay_bp.route('/overlay/<overlay_id>', methods=['DELETE'])
def delete_overlay(overlay_id):
    mongo.db.overlays.delete_one({"_id": overlay_id})
    return jsonify({'message': 'Overlay deleted successfully'}), 200




livestream_bp = Blueprint('livestream', __name__)
camera = None  
paused = False  
rtsp_url = "" 

print("RTSP URL init: ", rtsp_url)

def generate_frames():
    global camera, paused, rtsp_url
    if rtsp_url != "":
        camera = cv2.VideoCapture(rtsp_url)
    else:
        camera = cv2.VideoCapture(0)
    while True:
        if not paused and camera is not None:
            success, frame = camera.read()
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@livestream_bp.route('/')
def index():
    return current_app.send_static_file('index.html')
    # return render_template('index.html')

@livestream_bp.route('/livestream')
def livestream():
    print("RTSP URL livestream: ", rtsp_url)
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
    # return render_template('livestream.html', rtsp_url=rtsp_url)

@livestream_bp.route('/livestream/set_url', methods=['POST'])
def set_rtsp_url():
    global rtsp_url
    data = request.json
    rtsp_url = data['url']
    return jsonify({'message': 'RTSP URL set successfully'}), 200

def cleanup():
    global camera
    if camera is not None:
        camera.release() 

atexit.register(cleanup)
