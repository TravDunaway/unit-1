### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.


from pyparsing import line_end


def adding_new_book(newbook):
    title = input("What is the name of your book? ")
    author = input("Who wrote the book? ")
    try:
        year = int(input("When was this book published? (year?) "))
    except:
        year = int(input("Accepted format example (1998). "))
    try:
        rating = float(input("What rating out of 5 would you give this book?  "))
    except:
        rating = int(input("Must be a number. "))
    try:
        pages = int(input("How many pages are in your book?  "))
    except:
        pages = int(input("Must be a number. "))

    with open(newbook, "a") as file:
        file.write(f"{title}, {author}, {year}, {rating}, {pages}\n")


### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

def total_book_listr(newbook):
    # return ("All book in catalogue:")
    print("All books in current Catalogue: n/")
    with open(newbook, "r") as f:
        file = f.readlines()

        for line in file:
            title, author, year, rating, pages = line_end()

            # return (f"Title: {title"}, )
            print(f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")




### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

