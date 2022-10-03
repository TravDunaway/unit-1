my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

all_books_list = [
    { 
    "title": "red rising",
    "author": "pierce brown",
    "year": 2014,
    "rating": 5,
    "pages": 374
    },
    { 
    "title": "red",
    "author": "saoidnf",
    "year": 2098,
    "rating": 4.32,
    "pages": 374
    },
    { 
    "title": "Themes",
    "author": "Suollins",
    "year": 200,
    "rating": 4,
    "pages": 34
    },
    {
    "title": "Then Hun Games",
    "author": "Suzanne Collins",
    "year": 200,
    "rating": 4.3,
    "pages": 37
    },
    {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
    }

]

def get_set_of_authors(book_dictionary_list):
    author_set = set()

    for book_dictionary in book_dictionary_list:
        author_set.add(book_dictionary["author"])

    return author_set
# print(all_books_list["author"])
# def print():
#     for authors_books in all_books_list:
#         if all_books_list["author"] == "Suzanne Collins":
#             print(all_books_list)

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.
# def book_referencer(book_dictionary):`
#     book_info = f"{book_dictionary['title']} is the title of a {book_dictionary['pages']} paged book, written by {book_dictionary['author']}, in the year {book_dictionary['year']}, and has a user-rating of {book_dictionary['rating']}"
#     return book_info

# print(book_referencer(my_book))



# # Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# def a_book_title(book_dictionary):
#     book_title = f"{book_dictionary['title']} is the title of the book."
#     return book_title
# def a_book_author(book_dictionary):
#     book_author = f"{book_dictionary['author']} is the author."
#     return book_author
# def a_book_rating(book_dictionary):
#     book_rating = f"{book_dictionary['rating']} is the book's rating."
#     return book_rating
# def a_book_pages(book_dictionary):
#     book_page_count = f"{book_dictionary['pages']} is the book's page count."
#     return book_page_count

# print(a_book_author(my_book))
# print(a_book_title(my_book))
# print(a_book_pages(my_book))
# print(a_book_rating(my_book))


# # Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.


# def get_all_books_in_list(dictionary_list_name):
#     for book_dictionary in dictionary_list_name:
#         print(book_referencer(book_dictionary))

# get_all_books_in_list(all_books_list)



# def get_authors_in_list(dictionary_list_name):
#     for book_dictionary in dictionary_list_name:
#         print(a_book_author(book_dictionary))

# get_authors_in_list(all_books_list)

# def get_books_by_authors_name(dictionary_list_name, author_name):
#     for book_dictionary in dictionary_list_name:
#         if {book_dictionary['author']} = author_name:
#             return`

x = {}

def highest_rated_books(books):
    {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}

def books_alphabetical(dictionaries_of_books):
    dict(sorted(x.items(), key=lambda item: item[1]))