import speech_recognition as sr

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

def login():
    print("=== Login ===")
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]["password"] == password:
        print("Login successful!")
        return users[username]["role"]
    else:
        print("Invalid username or password")
        return None


def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        print("Sorry, I did not understand.")
        return ""


def execute_command(command, role):
    if role == "admin":
        if "shut down" in command:
            print("System is shutting down...")
        elif "status" in command:
            print("System status: Running normally")
        else:
            print("Unknown command")

    elif role == "user":
        if "status" in command:
            print("System status: Running normally")
        elif "shut down" in command:
            print("Access denied! Admin only command.")
        else:
            print("Unknown command")


# ===== Main Program =====
role = login()

if role:
    command = listen_command()
    execute_command(command, role)
