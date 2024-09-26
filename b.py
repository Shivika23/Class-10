class library:
    def __init__(self, list_of_books, name):
        self.booklist = list_of_books
        self.name = name
        self.lendDict = {}

    def display_books(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.booklist:
            print(book)

    def lend_book(self, user, book):
        if book not in self.booklist:
            print("Sorry we don't have that book.")
        
        elif book in self.lendDict:
            print(f"This book is already being used, by {self.lendDict[book]}")

        else:
            self.lendDict[book] = user
            print("Database updated you can take the book.")

    def add_book(self,book):
        self.booklist.append(book)
        print(f"{book} has been added to book list")

    def return_book(self,book):
        if book in self.lendDict:
            del self.lendDict[book]
            print("Book has been returned")

        else:
            print("The book wasn't borrowed from us.")

if __name__ == "__main__":
    books = library(
        [
            "Python",
            "Rich Dad Poor Dad",
            "Harry Potter",
            "C++ Basics",
            "Algorithms by CLRS",
        ],
        "Let's Upskill",
    )
    user_name = input("Welcome to our library! Please enter your name: ")

    while True:
        print(
            f"\nHello {user_name}, welcome to the {books.name} library. Please choose an option:"
        )
        print(
            "1. Display Books\n2. Lend a Book\n3. Add a Book\n4. Return a Book\n5. Quit"
        )
        user_choice = input("Enter your choice to continue: ")

        if user_choice not in ["1", "2", "3", "4", "5"]:
            print("Please enter a valid option.")
            continue

        if user_choice == "1":
            books.display_books()
        elif user_choice == "2":
            book = input("Enter the name of the book you want to lend: ")
            books.lend_book(user_name, book)
        elif user_choice == "3":
            book = input("Enter the name of the book you want to add: ")
            books.add_book(book)
        elif user_choice == "4":
            book = input("Enter the name of the book you want to return: ")
            books.return_book(book)
        elif user_choice == "5":
            print(f"Thank you for using the library, {user_name}. Goodbye!")
            break

    


        

        
