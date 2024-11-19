# import cv2
# import mediapipe as mp
# from deepface import DeepFace

# mp_face_detection = mp.solutions.face_detection
# mp_drawing = mp.solutions.drawing_utils

# cap = cv2.VideoCapture(0)

# with mp_face_detection.FaceDetection(min_detection_confidence=0.2) as face_detection:
#     while cap.isOpened():
#         success, image = cap.read()
#         if not success:
#             break

#         image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         results = face_detection.process(image_rgb)
#         image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

#         if results.detections:
#             for detection in results.detections:
#                 mp_drawing.draw_detection(image_bgr, detection)

#             try:
#                 result = DeepFace.analyze(image_bgr, actions=['emotion'])
#                 dominant_emotion = result['dominant_emotion']
#                 cv2.putText(image_bgr, f'Emotion: {dominant_emotion}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
#             except Exception as e:
#                 pass

#         cv2.imshow('Face and Emotion Detection', image_bgr)

#         if cv2.waitKey(5) & 0xFF == 27:
#             break

# cap.release()
# cv2.destroyAllWindows()

# import cv2
# import mediapipe as mp
# from deepface import DeepFace

# # Initialize MediaPipe face detection
# mp_face_detection = mp.solutions.face_detection
# mp_drawing = mp.solutions.drawing_utils

# # Load the DeepFace emotion model once outside the loop
# try:
#     emotion_model = DeepFace.build_model("Emotion")
#     print("Emotion model loaded successfully.")
# except Exception as e:
#     print(f"Failed to load emotion model: {e}")
#     emotion_model = None

# def face_emotion_detection():
#     cap = cv2.VideoCapture(0)

#     with mp_face_detection.FaceDetection(min_detection_confidence=0.2) as face_detection:
#         while cap.isOpened():
#             success, image = cap.read()
#             if not success:
#                 print("Failed to capture image")
#                 break

#             image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#             results = face_detection.process(image_rgb)
#             image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

#             if results.detections:
#                 for detection in results.detections:
#                     mp_drawing.draw_detection(image_bgr, detection)

#                 if emotion_model:
#                     try:
#                         result = DeepFace.analyze(image_bgr, actions=['emotion'], models={"emotion": emotion_model}, enforce_detection=False)
#                         dominant_emotion = result[0]['dominant_emotion']
#                         cv2.putText(image_bgr, f'Emotion: {dominant_emotion}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
#                     except Exception as e:
#                         print(f"Emotion detection error: {e}")

#             cv2.imshow('Real-Time Face and Emotion Detection', image_bgr)

#             if cv2.waitKey(5) & 0xFF == 27:
#                 break

#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     face_emotion_detection()
import cv2
import mediapipe as mp
from deepface import DeepFace
import socket
import json

# Initialize MediaPipe for face detection and face mesh (for landmarks)
mp_face_detection = mp.solutions.face_detection
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

def face_emotion_detection():
    cap = cv2.VideoCapture(0)
    # Set up a socket connection to Unity
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 65432))  # Ensure this matches the Unity server settings

    with mp_face_detection.FaceDetection(min_detection_confidence=0.2) as face_detection, \
         mp_face_mesh.FaceMesh(min_detection_confidence=0.2, max_num_faces=1) as face_mesh:
        
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Failed to capture image")
                break

            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # Face detection
            detection_results = face_detection.process(image_rgb)
            image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

            if detection_results.detections:
                for detection in detection_results.detections:
                    mp_drawing.draw_detection(image_bgr, detection)

            # Emotion detection
            try:
                result = DeepFace.analyze(image_bgr, actions=['emotion'], enforce_detection=False)
                dominant_emotion = result[0]['dominant_emotion']
                # Send emotion data to Unity
                emotion_data = json.dumps({"emotion": dominant_emotion})
                sock.sendall(emotion_data.encode('utf-8'))
                cv2.putText(image_bgr, f'Emotion: {dominant_emotion}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            except Exception as e:
                print(f"Emotion detection error: {e}")

            cv2.imshow('Real-Time Face and Emotion Detection', image_bgr)

            if cv2.waitKey(5) & 0xFF == 27:
                break

    cap.release()
    cv2.destroyAllWindows()
    sock.close()

if __name__ == "__main__":
    face_emotion_detection()
