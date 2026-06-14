books = {}
landed_books = []

file = open("Python/data/library.txt", "r", encoding="utf-8")
data = file.read().split("\n")
for book in data:
    if book != "":
        name, state = book.split(";")
        if state == "True":
            books[name] = True
        else:
            books[name] = False
            landed_books.append(name    )
file.close()
if len(books) == 0:
    print("No books loaded")


while True:
    choice = int(input("Enter 1 for add a book, 2 for show books, 3 for land a book, "
    "4 for return a book, 5 for delete a book, 6 for end: "))
    if choice == 1:
        book_name = input("Enter the name of the book you would like to add: ")
        books[book_name] = True
    elif choice == 2:
        for name in books:
            if books[name] == True:
                print(f"{name} is available")
            elif books[name] == False:
                print(f"{name} is not available")
    elif choice == 3:
        name = input("Enter the name of the book you would like to land: ")
        if name in books:
            if books[name]:
                landed_books.append(name)
                books[name] = False
            else:
                print("The book you would like to land is not available")
        else:
            print("The book you would like to land does not exist")
    elif choice == 4:
        name = input("Enter the name of the book you would like to return: ")
        if name in landed_books:
            index = landed_books.index(name)
            landed_books.pop(index)
            books[name] = True
        else:
            print("The book is not landed")
    elif choice == 5:
        name = input("Enter the name of the book you would like to delete: ")
        if name in books:
            del books[name]
        else:
            print("The book you entered does not exist")
    elif choice == 6:
        break

file = open("Python/data/library.txt", "w", encoding="utf-8")
for book in books:
    state = books[book]
    state_txt = str(state)
    file.write(f"{book};{state_txt}\n")
file.close()