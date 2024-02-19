class Library:
    def __init__(self):
        self.books_file = open("books.txt", "a+")

    def __del__(self):
        self.books_file.close()

    def list_books(self):
        self.books_file.seek(0)
        lines = self.books_file.read().splitlines()
        if len(lines) == 0:
            print("No books found.")
        else:
            for line in lines:
                print()
                book_info = line.split(',')
                print("Book: {}, Author: {}".format(book_info[0], book_info[1]))


    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")
        self.books_file.write(f"{title},{author},{release_year},{num_pages}\n")
        print("Book added.")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to delete: ")

        self.books_file.seek(0)
        lines = self.books_file.read().splitlines()

        flag = -1
        for i, line in enumerate(lines):
            if title_to_remove in line:
                flag = i
                break

        if flag != -1:
            del lines[flag]

            self.books_file.seek(0)
            self.books_file.truncate()

            for line in lines:
                self.books_file.write(line + '\n')

            print("Book removed.")
        else:
            print("Book not found.")


lib = Library()


while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("Q) Exit")
    choice = input("Enter your choice (1-3 or Q): ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "q" or choice == "Q":
        print("Exiting the program. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
