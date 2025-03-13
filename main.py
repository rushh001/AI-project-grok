from voice_recognition import record_and_transcribe
from command_handler import execute_command

def main():
    print("Listening for voice commands...")
    command = record_and_transcribe()
    if command:
        print(f"Recognized Command: {command}")
        execute_command(command)
    else:
        print("No command recognized.")

if __name__ == "__main__":
    main()
