### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ["Brandon Sanderson", "Joe Abercrombie", "Frank Herbert", "Patrick Rothfuss", "George R.R. Martin", "Erik Larson", "Bill Bryson", "Robert Jordan"]

# Now let's add a new author to the end with the .append() method. Type your code below.
my_authors.append("Dale Carnegie")
# Code here
# Example: my_authors.append("H.G. Wells")


# Now let's remove an element in the list

# Code here
my_authors.remove("Dale Carnegie")
# Example: my_authors.remove("H.G. Wells")


# Now access an element by it's index. (Remember it indexes start at 0.)

# Code here
# Example: my_authors[2]
my_authors[3]

# Now slice the list.

# Code here
# Example: my_authors[1:4]
my_authors[:-1]



### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

# Code here
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")

my_author_tuple = tuple(my_authors)

### Step 3 - Sets ###

# Create a set with your authors.

# Code here
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}

my_auther_set = set(my_authors)
print(my_auther_set)
# Add a new author to your set.

# Code here
# Example: my_author_set.add("J.R.R. Tolkien")

my_auther_set.add("Andy Weir")

# Try adding the same author again, and be sure to print your set.

# Code here
# Example: my_author_set.add("J.R.R. Tolkien")
my_auther_set.add("Andy Weir")
print(my_auther_set)
### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

for book in my_auther_set:
    print(book)

for book in my_author_tuple:
    print(book)

for book in my_authors:
    print(book)

# Code here
# Example:

# for book in my_authors:
    # print(book)

# for book in my_authors_tuple:
    # print(book)

# for book in my_authors_set:
    # print(book)

