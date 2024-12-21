class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author 
        self.is_borrowed = False


class Library:
    def __init__(self):
        self.books = []


    def add_book(self,book):
        self.books.append(book)
        print(f"'{book.title}' by {book.author} added to the library")

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            if not book.is_borrowed:
                print(f"-{book.title} by{book.author}")

        print()


    def borrow_book(self,title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True 
                print(f"You borrowed: {book.title}")


            print("Sorry, '{title}' is not available")


    def return_book(self,title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False 
                print(f"{book.title} has been returned!")

            print(f"Sorry! '{title}' was not borrowed.")


library = Library()

library.add_book(Book("The Great Gatsby","F.Scott Fitzgerald"))
library.add_book(Book("1984","George Orwell"))

library.display_books()


library.borrow_book("The Great Gatsby")
library.display_books()


library.return_book("The Great Gatsby")
library.display_books()



# Advanced
# Write a function to remove all duplicate elements from a list while maintaining the order.
ordered_list = [23,2,2,345,765,43,23,3,4,32,223,34,345,64,45,65,65,65]
result = []
for i in ordered_list:
    if i not in result:
        result.append(i)
print(sorted(result))

# using Comprehensions 
result =sorted({i for i in ordered_list})
print(result)



# Merge two sorted lists into a single sorted list.
l1 = [1,2,3,4,5,6,7,8,9]
l2  = [4,33,4,64,3,2,345,5]
l1.extend(l2)
print(sorted(l1))

# Write a Python program to find the second largest number in a list.
l1 = [34,43,2,2,3,454]
result = 0
for i in l1:
    if i>result:
        result = i 
print(result)
