# ### Step 1 - Input function
# ## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# print("Welcome to your personal book-collection-cataloger")
# print("an app that gathers information about the books you own") 


# def add_another_book():
#     title = input("What is the name of your book? ")
#     author = input("Who is the writer of the book? ")
#     year = int(input("Regarding your book, what year was it written? "))
#     rating = int(input("From one to five how is your book rated? "))
#     pages = int(input("How many pages does your book have? "))
#     price = float(input("How much does the book cost? "))
 

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages,
#         "price": price
#     }

#     return book_dictionary

# def adding_a_new_book():
#     title = input("What is the name of your book? ")
#     author = input("Who is the writer of the book? ")
#     year = int(input("Regarding your book, what year was it written? "))
#     rating = int(input("From one to five how is your book rated? "))
#     pages = int(input("How many pages does your book have? "))
#     price = float(input("How much does the book cost? "))
 

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages,
#         "price": price
#     }
#     counter += 1
# #     return book_dictionary  

# contquestion = input("Would you like to add a book? (Yes/No) ")
# if contquestion == "Yes" or "yes":
#     adding_a_new_book()








# # x = adding_a_new_book()

# # print(x)
# # print(y)



# # adding_a_new_book()

# ### Step 2 - Type conversion

# ## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# # Code here



# ### Step 3 - Error handling

# ## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# try:
#     year = int(input("Regarding your book, what year was it written? "))
# except:
#     year = int(input("With a number, please tell us what year your book was written? "))

# try:
#     pages = int(input("How many pages does your book have? "))
# except:
#     pages = int(input("With a number, please tell us ow many pages your book has? "))
# try:
#     price = float(input("How much does the book cost? "))
# except:
#     price = float(input("Please tell use how much your book costs with this numerical format 1.00. "))
# ### Step 4 - if/elif/else
# ## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.


















# ### Step 5 - while loops

# ## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# # Code here


counter = 0
x = []
def review_catalogue():
    print(x)













def add_another_book():
    counter = +1
    title = input("2What is the name of your book? ")
#     author = input("2Who is the writer of the book? ")
#     year = int(input("2Regarding your book, what year was it written? "))
#     rating = int(input("2From one to five how is your book rated? "))
#     pages = int(input("2How many pages does your book have? "))
#     price = float(input("2How much does the book cost? "))
 

    book_dictionary = {
        "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages,
#         "price": price
    }

    x.append(book_dictionary) 
    print(f"{counter} at end of add another book, thats function 2")
    counter
    print(f"{counter} at end of add another book, second print")
    prompt_question_adding_another_book = input("Would you like to add another book? yes/no ")
    if prompt_question_adding_another_book == "yes" or "Yes" or "y" or "Y":
        print(f"{counter} within first functionfunction" )
        x.append(book_dictionary)
        add_another_book()
    if prompt_question_adding_another_book == "no" or "NO" or "nO" or "No":
        next_step = input("Would you like to review your current library? ")
        if next_step = "yes", or "YES", or "Yes":




def adding_a_new_book():

    title = input("What is the name of your book? ")
    # author = input("Who is the writer of the book? ")
    # year = int(input("Regarding your book, what year was it written? "))
    # rating = int(input("From one to five how is your book rated? "))
    # pages = int(input("How many pages does your book have? "))
    # price = float(input("How much does the book cost? "))
 

    book_dictionary = {
        "title": title,
        # "author": author,
        # "year": year,
        # "rating": rating,
        # "pages": pages,
        # "price": price
    }
    
    prompt_question_adding_another_book = input("Would you like to add another book? yes/no ")
    if prompt_question_adding_another_book == "yes" or "Yes" or "y" or "Y":
        print(f"{counter} within first functionfunction" )
        x.append(book_dictionary)
        add_another_book()
   
   

print("Welcome to your personal book-collection-cataloger")
print("an app that gathers information about the books you own") 

for i in range(1):
    print(f"{counter} within for loop")
    if counter == 0:
        adding_a_new_book()
        if counter == 1:
            add_another_book()
