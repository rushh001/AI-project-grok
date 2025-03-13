import webbrowser
import os
import glob
from voice_recognition import get_ai_response  # Import AI chat function

# Define user folder path (Update if needed)
USER_FOLDER = r"C:\Users\mohdz"

def find_file(filename, search_path=USER_FOLDER):
    """Search for a file in the given directory and return the first match."""
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

def execute_command(command):
    command = command.lower().strip()

    # Debugging: Print the received command
    print(f"Received Command: '{command}'")

    # ✅ **Open Common Windows Applications**
    if any(keyword in command for keyword in ["open brave", "start brave"]):
        print("Opening Brave browser...")
        os.system("start brave")

    elif any(keyword in command for keyword in ["open whatsapp", "start whatsapp"]):
        print("Opening WhatsApp...")
        os.system("start shell:AppsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App")
 

    elif any(keyword in command for keyword in ["open chrome", "start chrome"]):
        print("Opening Google Chrome...")
        os.system("start chrome")

    elif any(keyword in command for keyword in ["open edge", "start edge"]):
        print("Opening Microsoft Edge...")
        os.system("start msedge")

    elif any(keyword in command for keyword in ["open notepad", "open note pad"]):
        print("Opening Notepad...")
        os.system("start notepad")

    elif any(keyword in command for keyword in ["open excel", "start excel"]):
        print("Opening Excel...")
        os.system("start excel")

    elif any(keyword in command for keyword in ["open word", "start word"]):
        print("Opening Microsoft Word...")
        os.system("start winword")

    elif any(keyword in command for keyword in ["open terminal", "start terminal", "open cmd", "start command prompt"]):
        print("Opening Terminal...")
        os.system("start cmd")

    elif any(keyword in command for keyword in ["open explorer", "start file explorer", "open my computer"]):
        print("Opening File Explorer...")
        os.system("start explorer")

    # ✅ **Search Google**
    elif "search for" in command:
        query = command.replace("search for", "").strip()
        print(f"Searching Google for: {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

     # ✅ **Open Email (Gmail or Outlook)**
    elif any(keyword in command for keyword in ["open email", "check my email", "open gmail"]):
        print("Opening Gmail...")
        webbrowser.open("https://mail.google.com")

    elif any(keyword in command for keyword in ["open outlook", "check outlook mail","check outlook email","outlook email"]):
        print("Opening Outlook Mail...")
        os.system("start outlook")


    # ✅ **Open User-Specific Folders**
    elif any(keyword in command for keyword in ["open downloads", "open my downloads"]):
        print("Opening Downloads folder...")
        os.startfile(os.path.join(USER_FOLDER, "Downloads"))

    elif any(keyword in command for keyword in ["open documents", "open my documents"]):
        print("Opening Documents folder...")
        os.startfile(os.path.join(USER_FOLDER, "Documents"))

    elif any(keyword in command for keyword in ["open desktop", "open my desktop"]):
        print("Opening Desktop folder...")
        os.startfile(os.path.join(USER_FOLDER, "Desktop"))

    elif any(keyword in command for keyword in ["open pictures", "open my pictures"]):
        print("Opening Pictures folder...")
        os.startfile(os.path.join(USER_FOLDER, "Pictures"))

    elif any(keyword in command for keyword in ["open music", "open my music"]):
        print("Opening Music folder...")
        os.startfile(os.path.join(USER_FOLDER, "Music"))

    elif any(keyword in command for keyword in ["open videos", "open my videos"]):
        print("Opening Videos folder...")
        os.startfile(os.path.join(USER_FOLDER, "Videos"))

     # System Commands
    # elif any(keyword in command for keyword in ["shutdown", "turn off", "power off"]):
    #     print("Shutting down system...")
    #     os.system("shutdown /s /t 5")

    # elif any(keyword in command for keyword in ["restart", "reboot"]):
    #     print("Restarting system...")
    #     os.system("shutdown /r /t 5")

    # elif any(keyword in command for keyword in ["log off", "sign out"]):
    #     print("Logging off user...")
    #     os.system("shutdown /l")

    # elif any(keyword in command for keyword in ["sleep", "go to sleep"]):
    #     print("Putting system to sleep...")
    #     os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    # ✅ **Open a File by Name**
    elif "Open" in command:
        filename = command.replace("Open", "").strip()
        print(f"Searching for {filename}...")

        # Check if filename has extension; if not, try adding common ones
        common_extensions = ["", ".txt", ".pdf", ".docx", ".xlsx", ".jpg", ".png"]
        
        for ext in common_extensions:
            file_path = find_file(filename + ext)
            if file_path:
                print(f"Opening file: {file_path}")
                os.startfile(file_path)
                return

        print("File not found.")

    # ✅ **Fallback to AI Chat Mode**
    else:
        print("No command recognized. Switching to conversation mode.")
        ai_response = get_ai_response(command)
        print(f"AI: {ai_response}")
