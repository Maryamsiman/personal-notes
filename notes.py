# Personal Notes App

def show_menu():
    print("\n--- Personal Notes App ---")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Delete All Notes")
    print("4. Exit")

def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("✅ Note saved!")

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            if notes:
                print("\nYour Notes:")
                for i, note in enumerate(notes, 1):
                    print(f"{i}. {note.strip()}")
            else:
                print("No notes found.")
    except FileNotFoundError:
        print("No notes file exists yet.")

def delete_notes():
    open("notes.txt", "w").close()
    print("🗑️ All notes deleted.")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        delete_notes()
    elif choice == "4":
        print("👋 Exiting Notes App. Goodbye!")
        break
    else:
        print("❌ Invalid option, try again.")
