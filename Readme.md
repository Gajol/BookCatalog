A few Python programs to look at a a CSV file of books.

The books can be read from a file, or, you can use the string parameter.

[books.category.py](books-category.py): Reads in the google CSV file, and creates the books_category_dictionary collection.  This is a dictionary of a list of books (dict of lists of dicts).   This file also converts the books_category_dictionary to a simple list of books sorted by publisher and title.

- TODO : The book_list has duplicate items (the only difference in the item is the category).   To correct this, more functionality should be added to :
  1. Loop through the book_list
  1. ...follow logic in [books-publisher-category.py][books-publisher-category.py]
