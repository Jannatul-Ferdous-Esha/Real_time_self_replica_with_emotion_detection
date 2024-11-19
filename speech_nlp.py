# import speech_recognition as sr
# import pyttsx3

# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# def get_response(input_text):
#     responses = {
#         "hello": "Hi there!",
#         "how are you": "I'm a bot, but I'm doing great! How about you?",
#         "bye": "Goodbye! Have a great day!"
#     }
#     return responses.get(input_text.lower(), "Sorry, I didn't understand that.")

# def speak_text(text):
#     engine.say(text)
#     engine.runAndWait()

# with sr.Microphone() as source:
#     print("Listening...")
#     while True:
#         audio = recognizer.listen(source)
#         try:
#             text = recognizer.recognize_google(audio)
#             print(f"Recognized: {text}")
#             response = get_response(text)
#             speak_text(response)
#         except sr.UnknownValueError:
#             print("Sorry, I did not understand that.")
#         except sr.RequestError:
#             print("Sorry, my speech service is down.")

# import speech_recognition as sr

# recognizer = sr.Recognizer()

# with sr.Microphone() as source:
#     print("Please say something")
#     audio = recognizer.listen(source)

#     try:
#         print("You said: " + recognizer.recognize_google(audio))
#     except sr.UnknownValueError:
#         print("Could not understand audio")
#     except sr.RequestError as e:
#         print("Could not request results; {0}".format(e))


# import speech_recognition as sr
# import pyttsx3
# import time 

# # Initialize recognizer and text-to-speech engine
# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# def get_response(input_text):
#     responses = {
#         "hello": "Hi there!",
#         "how are you": "I'm a bot, but I'm doing great! How about you?",
#         "bye": "Goodbye! Have a great day!"
#     }
#     return responses.get(input_text.lower(), "Sorry, I didn't understand that.")

# def speak_text(text):
#     engine.say(text)
#     engine.runAndWait()

# def listen_and_respond():
#     try:
#         with sr.Microphone() as source:
#             print("Listening...")
#             recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
#             audio = recognizer.listen(source, timeout=10)  # Listen once with a 10 second timeout
#             print("Audio received.")
            
#             # Debugging: Print raw audio data
#             print(f"Raw audio data: {audio.frame_data[:100]}...")  # Print first 100 bytes
            
#             # Recognize speech using Google Web Speech API
#             text = recognizer.recognize_google(audio)
#             print(f"Recognized: {text}")
#             response = get_response(text)
#             speak_text(response)
            
#     except sr.UnknownValueError:
#         print("Sorry, I did not understand that.")
#     except sr.RequestError as e:
#         print(f"Request error: {e}")
#     except Exception as e:
#         print(f"An error occurred: {e}")


# if __name__ == "__main__":
#     listen_and_respond()

# import speech_recognition as sr
# import pyttsx3
# import time

# # Initialize Speech Recognition and Text-to-Speech
# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

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

# def listen_and_respond():
#     with sr.Microphone() as source:
#         recognizer.adjust_for_ambient_noise(source, duration=1)  # Increase the adjustment duration
#         while True:
#             try:
#                 print("Listening...")
#                 audio = recognizer.listen(source, timeout=10)
#                 print("Audio received.")
                
#                 text = recognizer.recognize_google(audio)
#                 print(f"Recognized: {text}")
#                 response = get_response(text)
#                 print(f"Responding: {response}")
#                 speak_text(response)
                
#             except sr.UnknownValueError:
#                 print("Sorry, I did not understand that.")
#             except sr.RequestError as e:
#                 print(f"Request error: {e}")
#             except Exception as e:
#                 print(f"An error occurred: {e}")
#             # Adding a delay for debugging purposes
#             time.sleep(1)

# if __name__ == "__main__":
#     listen_and_respond()

# import speech_recognition as sr

# recognizer = sr.Recognizer()

# # with sr.Microphone() as source:
# #     recognizer.adjust_for_ambient_noise(source)
# #     print("Please say something")
# #     audio = recognizer.listen(source)
# with sr.Microphone() as source:
#     recognizer.adjust_for_ambient_noise(source, duration=1)  # Increase duration for better adjustment
#     print("Please say something")
#     audio = recognizer.listen(source)
# print(audio.get_raw_data())

# try:
#     print("You said: " + recognizer.recognize_google(audio))
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))


import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Please say something")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print(f"Recognized: {text}")
except sr.UnknownValueError:
    print("Sorry, I did not understand that.")
except sr.RequestError as e:
    print(f"Could not request results; {e}")
except Exception as e:
    print(f"An error occurred: {e}")
