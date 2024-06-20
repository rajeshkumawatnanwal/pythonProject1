def make_notes():
    speak("speak that you want to make notes")
    print("speak that you want to make notes")
    note ,_ = listen()
    if note:
        filename = f"note_by_voice.txt"
        with open(filename, 'w') as file:
            file.write(note)
        print(f"Notes saved as {filename}")
        speak(f"Notes saved as {filename}")
    else:
        print("please speak your notes.")
        speak("please speak your notes.")

# add it in main function
if "notes" in command:
  make_notes()
                        
