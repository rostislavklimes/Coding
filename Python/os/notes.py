import os
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

choice = int(input("Enter 1 for new note, 2 for show note, 3 for delete a note: "))
while choice not in [1, 2, 3]:
    print("You did not enter 1 or 2 or 3")
    choice = int(input("Enter 1 for new note, 2 for show note, 3 for delete a note: "))
if choice == 1:
    note_name = input("Enter name of your note: ")
    cipher_index = int(input("Enter number of indexes for cipher: "))
    word = input("Enter a word: ")
    word = word.lower()
    new_word = ""
    state = True

    if not word.strip():
        print("Note can not be empty")
        state = False

    for i in word:
        if i not in abc and i != " ":
            print("You used something else than letter or space")
            state = False
            break
    if state == True:
        for i in word:
            if i == " ":
                new_word += " "
                continue
            else:
                index = abc.index(i)
                new_word += abc[(index + cipher_index) % len(abc)] 
        soubor = open(f"Python/data/{note_name}_notes.txt", "w", encoding="utf-8")
        soubor.write(new_word)
        soubor.close()
    elif state == False:
        pass
elif choice == 2:
    note_name = input("enter note name: ")
    try:
        soubor = open(f"Python/data/{note_name}_notes.txt", "r", encoding="utf-8")
        note = soubor.read()
        state = True
    except FileNotFoundError:
        state = False
    if state == True:
        cipher_index = int(input("Enter number of indexes for cipher: "))
        note_text = ""
        for i in note:
            if i == " ":
                note_text += " "
                continue
            else:
                index = abc.index(i)
                note_text += abc[(index - cipher_index) % len(abc)]
        print(note_text)
        soubor.close()
    elif state == False:
        print("File does not exist")

elif choice == 3:
    delete_name = input("Enter name of a note you would like to delete: ")
    file_path = f"Python/data/{delete_name}_notes.txt"
    if os.path.exists(file_path):
        os.remove(file_path)
        print("Note deleted")
    else:
        print("File does not exist")