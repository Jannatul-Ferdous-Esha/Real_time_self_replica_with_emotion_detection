

# # # import cv2
# # # import mediapipe as mp
# # # from deepface import DeepFace
# # # import speech_recognition as sr
# # # import pyttsx3
# # # import multiprocessing
# # # import os
# # # import tensorflow as tf

# # # # Suppress TensorFlow logs
# # # os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# # # os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
# # # tf.get_logger().setLevel('ERROR')

# # # # Initialize MediaPipe for face detection
# # # mp_face_detection = mp.solutions.face_detection
# # # mp_drawing = mp.solutions.drawing_utils

# # # # Initialize Speech Recognition and Text-to-Speech
# # # recognizer = sr.Recognizer()
# # # engine = pyttsx3.init()

# # # def get_response(input_text):
# # #     responses = {
# # #         "hello": "Hi there!",
# # #         "how are you": "I'm a bot, but I'm doing great! How about you?",
# # #         "bye": "Goodbye! Have a great day!"
# # #     }
# # #     return responses.get(input_text.lower(), f"You said: {input_text}")

# # # def speak_text(text):
# # #     engine.say(text)
# # #     engine.runAndWait()

# # # def listen_and_respond(max_attempts=50):
# # #     attempt = 0
# # #     while attempt < max_attempts:
# # #         with sr.Microphone() as source:
# # #             recognizer.adjust_for_ambient_noise(source)
# # #             try:
# # #                 print("Listening...")
# # #                 audio = recognizer.listen(source, timeout=10)
# # #                 print("Audio received.")
                
# # #                 text = recognizer.recognize_google(audio)
# # #                 print(f"Recognized: {text}")
# # #                 response = get_response(text)
# # #                 speak_text(response)

# # #             except sr.UnknownValueError:
# # #                 print("Sorry, I did not understand that.")
# # #             except sr.RequestError as e:
# # #                 print(f"Request error: {e}")
# # #             except Exception as e:
# # #                 print(f"An error occurred: {e}")
# # #             finally:
# # #                 attempt += 1
# # #                 print(f"Attempt {attempt} of {max_attempts}")

# # #     print("Max attempts reached. Stopping the speech recognition.")

# # # def face_emotion_detection():
# # #     cap = cv2.VideoCapture(0)
# # #     with mp_face_detection.FaceDetection(min_detection_confidence=0.2) as face_detection:
# # #         while cap.isOpened():
# # #             success, image = cap.read()
# # #             if not success:
# # #                 print("Failed to capture image")
# # #                 break

# # #             image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# # #             results = face_detection.process(image_rgb)
# # #             image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

# # #             if results.detections:
# # #                 for detection in results.detections:
# # #                     mp_drawing.draw_detection(image_bgr, detection)

# # #                 try:
# # #                     result = DeepFace.analyze(image_bgr, actions=['emotion'], enforce_detection=False)
# # #                     dominant_emotion = result[0]['dominant_emotion']
# # #                     cv2.putText(image_bgr, f'Emotion: {dominant_emotion}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
# # #                 except Exception as e:
# # #                     print(f"Emotion detection error: {e}")

# # #             cv2.imshow('Real-Time Face and Emotion Detection', image_bgr)

# # #             if cv2.waitKey(5) & 0xFF == 27:
# # #                 break

# # #     cap.release()
# # #     cv2.destroyAllWindows()

# # # if __name__ == "__main__":
# # #     # Creating separate processes for speech recognition and face emotion detection
# # #     speech_process = multiprocessing.Process(target=listen_and_respond)
# # #     emotion_process = multiprocessing.Process(target=face_emotion_detection)

# # #     # Start both processes
# # #     speech_process.start()
# # #     emotion_process.start()

# # #     # Wait for both processes to complete
# # #     speech_process.join()
# # #     emotion_process.join()


# # import cv2
# # import mediapipe as mp
# # from deepface import DeepFace
# # import speech_recognition as sr
# # import pyttsx3
# # import multiprocessing
# # import os
# # import tensorflow as tf

# # # Suppress TensorFlow logs
# # os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# # os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
# # tf.get_logger().setLevel('ERROR')

# # # Initialize MediaPipe for face detection and face mesh (for landmarks)
# # mp_face_detection = mp.solutions.face_detection
# # mp_face_mesh = mp.solutions.face_mesh
# # mp_drawing = mp.solutions.drawing_utils

# # # Initialize Speech Recognition and Text-to-Speech
# # recognizer = sr.Recognizer()
# # engine = pyttsx3.init()

# # # Improved NLP for more dynamic responses
# # def get_response(input_text):
# #     responses = {
# #         "hello": "Hi there!",
# #         "how are you": "I'm a bot, but I'm doing great! How about you?",
# #         "bye": "Goodbye! Have a great day!"
# #     }
# #     return responses.get(input_text.lower(), f"You said: {input_text}")

# # def speak_text(text):
# #     engine.say(text)
# #     engine.runAndWait()

# # def listen_and_respond(max_attempts=20):
# #     attempt = 0
# #     while attempt < max_attempts:
# #         with sr.Microphone() as source:
# #             recognizer.adjust_for_ambient_noise(source)
# #             try:
# #                 print("Listening...")
# #                 audio = recognizer.listen(source, timeout=10)
# #                 print("Audio received.")
                
# #                 text = recognizer.recognize_google(audio)
# #                 print(f"Recognized: {text}")
# #                 response = get_response(text)
# #                 speak_text(response)

# #             except sr.UnknownValueError:
# #                 print("Sorry, I did not understand that.")
# #             except sr.RequestError as e:
# #                 print(f"Request error: {e}")
# #             except Exception as e:
# #                 print(f"An error occurred: {e}")
# #             finally:
# #                 attempt += 1
# #                 print(f"Attempt {attempt} of {max_attempts}")

# #     print("Max attempts reached. Stopping the speech recognition.")

# # def face_emotion_detection():
# #     cap = cv2.VideoCapture(0)
# #     with mp_face_detection.FaceDetection(min_detection_confidence=0.2) as face_detection, \
# #          mp_face_mesh.FaceMesh(min_detection_confidence=0.2, max_num_faces=1) as face_mesh:
        
# #         while cap.isOpened():
# #             success, image = cap.read()
# #             if not success:
# #                 print("Failed to capture image")
# #                 break

# #             image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
# #             # Face detection
# #             detection_results = face_detection.process(image_rgb)
# #             mesh_results = face_mesh.process(image_rgb)
# #             image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

# #             if detection_results.detections:
# #                 for detection in detection_results.detections:
# #                     mp_drawing.draw_detection(image_bgr, detection)

# #             # Facial landmarks detection
# #             if mesh_results.multi_face_landmarks:
# #                 for face_landmarks in mesh_results.multi_face_landmarks:
# #                     mp_drawing.draw_landmarks(
# #                         image=image_bgr,
# #                         landmark_list=face_landmarks,
# #                         connections=mp_face_mesh.FACEMESH_TESSELATION,
# #                         landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
# #                         connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 255), thickness=1, circle_radius=1)
# #                     )

# #             # Emotion detection
# #             try:
# #                 result = DeepFace.analyze(image_bgr, actions=['emotion'], enforce_detection=False)
# #                 dominant_emotion = result[0]['dominant_emotion']
# #                 cv2.putText(image_bgr, f'Emotion: {dominant_emotion}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
# #             except Exception as e:
# #                 print(f"Emotion detection error: {e}")

# #             cv2.imshow('Real-Time Face, Emotion and Landmark Detection', image_bgr)

# #             if cv2.waitKey(5) & 0xFF == 27:
# #                 break

# #     cap.release()
# #     cv2.destroyAllWindows()

# # if __name__ == "__main__":
# #     # Creating separate processes for speech recognition and face emotion detection
# #     speech_process = multiprocessing.Process(target=listen_and_respond)
# #     emotion_process = multiprocessing.Process(target=face_emotion_detection)

# #     # Start both processes
# #     speech_process.start()
# #     emotion_process.start()

# #     # Wait for both processes to complete
# #     speech_process.join()
# #     emotion_process.join()

# import cv2
# import mediapipe as mp
# from deepface import DeepFace
# import speech_recognition as sr
# import pyttsx3
# import multiprocessing
# import os
# import tensorflow as tf

# # Suppress TensorFlow logs
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
# tf.get_logger().setLevel('ERROR')

# # Initialize MediaPipe for face detection and face mesh (for landmarks)
# mp_face_detection = mp.solutions.face_detection
# mp_face_mesh = mp.solutions.face_mesh
# mp_drawing = mp.solutions.drawing_utils

# # Initialize Speech Recognition and Text-to-Speech
# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# # Improved NLP for more dynamic responses
# def get_response(input_text):
#     responses = {
#         "hello": "Hi there!",
#         "how are you": "I'm a bot, but I'm doing great! How about you?",
#         "bye": "Goodbye! Have a great day!"
#     }
#     return responses.get(input_text.lower(), f"You said: {input_text}")

# def speak_text(text):
#     engine.say(text)
#     engine.runAndWait()

# def listen_and_respond(max_attempts=20):
#     attempt = 0
#     while attempt < max_attempts:
#         with sr.Microphone() as source:
#             recognizer.adjust_for_ambient_noise(source)
#             try:
#                 print("Listening...")
#                 audio = recognizer.listen(source, timeout=10)
#                 print("Audio received.")
                
#                 text = recognizer.recognize_google(audio)
#                 print(f"Recognized: {text}")
#                 response = get_response(text)
#                 speak_text(response)

#             except sr.UnknownValueError:
#                 print("Sorry, I did not understand that.")
#             except sr.RequestError as e:
#                 print(f"Request error: {e}")
#             except Exception as e:
#                 print(f"An error occurred: {e}")
#             finally:
#                 attempt += 1
#                 print(f"Attempt {attempt} of {max_attempts}")

#     print("Max attempts reached. Stopping the speech recognition.")

# def face_emotion_detection():
#     cap = cv2.VideoCapture(0)
#     with mp_face_detection.FaceDetection(min_detection_confidence=0.2) as face_detection, \
#          mp_face_mesh.FaceMesh(min_detection_confidence=0.2, max_num_faces=1) as face_mesh:
        
#         while cap.isOpened():
#             success, image = cap.read()
#             if not success:
#                 print("Failed to capture image")
#                 break

#             image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
#             # Face detection
#             detection_results = face_detection.process(image_rgb)
#             mesh_results = face_mesh.process(image_rgb)
#             image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

#             if detection_results.detections:
#                 for detection in detection_results.detections:
#                     mp_drawing.draw_detection(image_bgr, detection)

#             # Facial landmarks detection
#             if mesh_results.multi_face_landmarks:
#                 for face_landmarks in mesh_results.multi_face_landmarks:
#                     mp_drawing.draw_landmarks(
#                         image=image_bgr,
#                         landmark_list=face_landmarks,
#                         connections=mp_face_mesh.FACEMESH_TESSELATION,
#                         landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
#                         connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 255), thickness=1, circle_radius=1)
#                     )

#             # Emotion detection
#             try:
#                 result = DeepFace.analyze(image_bgr, actions=['emotion'], enforce_detection=False)
#                 dominant_emotion = result[0]['dominant_emotion']
#                 cv2.putText(image_bgr, f'Emotion: {dominant_emotion}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
#             except Exception as e:
#                 print(f"Emotion detection error: {e}")

#             cv2.imshow('Real-Time Face, Emotion and Landmark Detection', image_bgr)

#             if cv2.waitKey(5) & 0xFF == 27:
#                 break

#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     # Creating separate processes for speech recognition and face emotion detection
#     speech_process = multiprocessing.Process(target=listen_and_respond)
#     emotion_process = multiprocessing.Process(target=face_emotion_detection)

#     # Start both processes
#     speech_process.start()
#     emotion_process.start()

#     # Wait for both processes to complete
#     speech_process.join()
#     emotion_process.join()

import cv2
import mediapipe as mp
from deepface import DeepFace
import speech_recognition as sr
import pyttsx3
import multiprocessing
import os
import tensorflow as tf

# Suppress TensorFlow logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
tf.get_logger().setLevel('ERROR')

# Initialize MediaPipe for face detection and face mesh (for landmarks)
mp_face_detection = mp.solutions.face_detection
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# Initialize Speech Recognition and Text-to-Speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Improved NLP for more dynamic responses
def get_response(input_text):
    responses = {
        "hello": "Hi there!",
        "how are you": "I'm a bot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a great day!"
    }
    return responses.get(input_text.lower(), f"You said: {input_text}")

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def listen_and_respond(max_attempts=20):
    attempt = 0
    while attempt < max_attempts:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            try:
                print("Listening...")
                audio = recognizer.listen(source, timeout=15)  # Increased timeout
                print("Audio received.")
                
                text = recognizer.recognize_google(audio)
                print(f"Recognized: {text}")
                response = get_response(text)
                speak_text(response)

            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
            except sr.RequestError as e:
                print(f"Request error: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                attempt += 1
                print(f"Attempt {attempt} of {max_attempts}")

    print("Max attempts reached. Stopping the speech recognition.")

def face_emotion_detection():
    cap = cv2.VideoCapture(0)
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
            mesh_results = face_mesh.process(image_rgb)
            image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

            if detection_results.detections:
                for detection in detection_results.detections:
                    mp_drawing.draw_detection(image_bgr, detection)

            # Facial landmarks detection
            if mesh_results.multi_face_landmarks:
                for face_landmarks in mesh_results.multi_face_landmarks:
                    mp_drawing.draw_landmarks(
                        image=image_bgr,
                        landmark_list=face_landmarks,
                        connections=mp_face_mesh.FACEMESH_TESSELATION,
                        landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
                        connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 255), thickness=1, circle_radius=1)
                    )

            # Emotion detection
            try:
                result = DeepFace.analyze(image_bgr, actions=['emotion'], enforce_detection=False)
                dominant_emotion = result[0]['dominant_emotion']
                cv2.putText(image_bgr, f'Emotion: {dominant_emotion}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            except Exception as e:
                print(f"Emotion detection error: {e}")

            cv2.imshow('Real-Time Face, Emotion and Landmark Detection', image_bgr)

            if cv2.waitKey(5) & 0xFF == 27:
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        # Creating separate processes for speech recognition and face emotion detection
        speech_process = multiprocessing.Process(target=listen_and_respond)
        emotion_process = multiprocessing.Process(target=face_emotion_detection)

        # Start both processes
        speech_process.start()
        emotion_process.start()

        # Wait for both processes to complete
        speech_process.join()
        emotion_process.join()
    except KeyboardInterrupt:
        print("Processes interrupted.")
    finally:
        speech_process.terminate()
        emotion_process.terminate()

