import speech_recognition as sr
from datetime import datetime

def capture_voice():
    recognizer = sr.Recognizer()

    with sr.Microphone() as mic:
        print("\n Speak any time...")

        recognizer.adjust_for_ambient_noise(mic)

        try:
            audio_data = recognizer.listen(mic, timeout=5)
            text_output = recognizer.recognize_google(audio_data)
            return text_output.lower()

        except Exception:
            return None


def run_assistant():
    print("=== Interactive Voice Assistant ===")
    print("Say 'stop', 'goodbye', or 'end' to finish the session.")

    running = True

    while running:
        user_voice = capture_voice()

        if not user_voice:
            continue

        print(f"User said: {user_voice}")

      
        if "hey" in user_voice or "hello" in user_voice:
            print("Assistant: Hello! How can I support you today?")


        elif "who are you" in user_voice or "name" in user_voice:
            print("Assistant: I'm your custom-made Python voice helper.")


        elif "how are you" in user_voice:
            print("Assistant: I'm operating smoothly. Thanks for asking!")


        elif "time" in user_voice or "clock" in user_voice:
            now = datetime.now().strftime("%H:%M %p")
            print(f"Assistant: The time right now is {now}.")


        elif "where are you" in user_voice or "location" in user_voice:
            print("Assistant: I'm running inside your system's memory.")


        elif "joke" in user_voice or "funny" in user_voice:
            print("Assistant: Why was the computer cold? Because it forgot to close its Windows!")


        elif "study" in user_voice or "school" in user_voice:
            print("Assistant: Education opens the door to creating programs like me!")


        elif any(exit_word in user_voice for exit_word in ["stop", "end", "goodbye"]):
            print("Assistant: Ending program. See you soon!")
            running = False


        else:
            print("Assistant: Hmm, I'm not sure what that means.")

if _name_ == "_main_":
    run_assistant()
