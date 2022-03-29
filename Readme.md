A few Python programs to look at a a CSV file of books.

The books can be read from a file, or, you can use the string parameter.

[books.category.py](books-category.py): Reads in the [google CSV file](google_books_dataset.csv), and creates the books_category_dictionary collection.  This is a dictionary of a list of books (dict of lists of dicts).   This file also converts the books_category_dictionary to a simple list of books sorted by publisher and title.

- TODO : Filter/Delete Duplicate Titles
  The book_list has duplicate items (the only difference in the item is the category).   To correct this, more functionality should be added to :
  1. Loop through the book_list
  1. ...follow logic in [books-publisher-category.py](books-publisher-category.py).  This has errors, as the 'category' value is a string, and it looks like the assignment wants this to be an array.   The functions / code that creates the lists would have to change the dict-value for category to be an array (it is currently a string)  
  1. This logic is wrong, simple comma-separated string.  

```
book_unique_title_list_of_dict[-1]['category'] += ", " + next_book['category']
```


- TODO : Logging : Should us the [Python Logging](https://realpython.com/python-logging/) library to output debug statements based on configuration.  Remove the pritns and replace with logging calls. 
