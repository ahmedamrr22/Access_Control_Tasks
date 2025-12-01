import speech_recognition as sr
from datetime import datetime

def listen_to_user():
    r = sr.Recognizer()

    with sr.Microphone() as mic:
        print("\n Waiting for your voice...")

        r.adjust_for_ambient_noise(mic, duration=1)

        try:
            audio_data = r.listen(mic, timeout=5)
            print(" Converting speech to text...")
            spoken_text = r.recognize_google(audio_data)
            return spoken_text.lower()

        except sr.WaitTimeoutError:
            print("No voice detected. Try again.")
            return None
        except sr.UnknownValueError:
            print("I couldn't catch what you said.")
            return None
        except sr.RequestError:
            print("Speech service unavailable. Check your internet.")
            return None


def voice_assistant():
    print("=== Voice Assistant Program Activated ===")
    print("Say one of these to stop: 'stop', 'end', 'close'")

    active = True

    while active:
        user_input = listen_to_user()

        if not user_input:
            continue

        print(f" You said: {user_input}")

        # Exit conditions
        if any(word in user_input for word in ["stop", "end", "close"]):
            print("Assistant: Ending session. Goodbye!")
            active = False

        elif "hey" in user_input or "hello" in user_input:
            print("Assistant: Hi! What can I do for you today?")

        elif "who are you" in user_input or "name" in user_input:
            print("Assistant: I'm ahemd's simple Python voice assistant built for testing.")

        elif "how's life" in user_input or "how are you" in user_input:
            print("Assistant: Running smoothly! Thanks for asking.")

        elif "what's the time" in user_input or "current time" in user_input:
            now = datetime.now().strftime("%H:%M")
            print(f"Assistant: It's currently {now}.")

        else:
            print("Assistant: Hmm, interesting... tell me more!")

if _name_ == "_main_":
    voice_assistant()
