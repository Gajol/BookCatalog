import csv
import pprint


# P1 Task 3 - Case 1 function definition
def book_category_dictionary(filename: str):
    """Returns a dictionary of book information indexed by its genre category by passing through a filename in CSV format
    as an input argument.
    -> Dict[str, List[Dict[str, Union[str, int, float]]]]:
    """

    book_category_dict = {}

    book_str_nano = """title,publisher
    TitleB,Pub-1
    Title3,Pub-3
    Title2,Pub-2
    TitleA,Pub-1"""

    book_str_simple = """title,author,rating,publisher,pages,category,language
    TitleB,Author1,1,Pub-1,10,Category 1,Language 1
    Title3,Author3,3,Pub-3,30,Category 3,Language 1
    Title2,Author2,2,Pub-2,20,Category 2,Language 2
    TitleA,Author3,3,Pub-1,30,Category 3,Language 1"""

    book_str_basic = """title,author,rating,publisher,pages,category,language
    After Anna,Alex Lake,4.1,HarperCollins UK,416,Fiction,English
    The Joker,Brian Azzarello,4.4,DC,130,Comics,English
    Venomized,Cullen Bunn,4.5,Marvel Entertainment,136,Comics,English
    Bring Me Back,B A Paris,3.8,HarperCollins UK,368,Crime,English"""

    # choose which book-csv to test
    #book_str = book_str_nano
    #book_str = book_str_simple
    #book_str = book_str_basic
    #book_str = book_str_google
    book_str = ""

    if (not book_str) :
      # read from google CSV file
      book_dict_reader = csv.DictReader(open("google_books_dataset.csv"))
    else:
      book_dict_reader = csv.DictReader(book_str.splitlines())

    print(book_dict_reader.fieldnames)
    # ------------------------------

    """
    With a list of all books, iterate through list, creating a new category if cateogry
    does not exist in dictionary
    """
    book_list_of_dict = list(book_dict_reader)
    print("In Category Function: Number of Books: ", len(list(book_list_of_dict)))

    for book in book_list_of_dict :
        if book['category'] in book_category_dict.keys():
          # book category is a key in the dictionary
          # the values in the dictionary is a "list of books"
          # i.e., for each category, there is a value of "list of books"
          # title,author,rating,publisher,pages,category,language
          book_category_dict[book['category']].append(  { \
                            'title' : book['title'],\
                            'author' : book['author'], \
                            'rating' : book['rating'], \
                            'publisher' : book['publisher'], \
                            'pages' : book['pages'], \
                            'language' : book['language']  }
          )
          # print ("Added book to category", book['category'])
        else:
          # create new category
          book_category_dict[book['category']] = []
          book_category_dict[book['category']].append(  { \
                            'title' : book['title'],\
                            'author' : book['author'], \
                            'rating' : book['rating'], \
                            'publisher' : book['publisher'], \
                            'pages' : book['pages'], \
                            'language' : book['language']  }
          )

    return book_category_dict

def summarize_book_category_dictionary(book_cat_list: dict):
    for category in book_cat_list.keys():
        print (category, ":\t\t ", len(book_cat_list[category]), " books")


def bubbleSortListofDict( theSeq, sortBy ):
    """ Bubble sort of List of Dictionaries
    sortBy: dictionary key to sort list by
    """

    n = len( theSeq )
    for i in range( n - 1 ) :
        swapped = False
        for j in range(n - 1) :
            if theSeq[j][sortBy] > theSeq[j + 1][sortBy] :
                theSeq[j], theSeq[j + 1] = \
                theSeq[j + 1], theSeq[j]
                flag = True
        if flag == False:
            break
    return theSeq


# Convert DictReader object to a list of dictionaries
books_by_category = book_category_dictionary("google_books_dataset.csv")
pprint.pprint(books_by_category)
#book_list_of_dict = bubbleSortListofDict(book_list_of_dict, 'title')
#summarize_book_category_dictionary(books_by_category)


# books_by_category is a dict of lists of dicts...
# to get a sorted list of all books (alphabetical by publisher), but also
# sorted by title, the logic will be to:
# 1. flatten books_by_category to be a list of books
# 2. sort the list by title
# 3. sort the list by publisher
# 1. Flatten:
#    Loop through categories, and make a list of book_str
book_list = []
for book_category in books_by_category.keys():
    for books in books_by_category[book_category]:
        new_book = {
                        'category' : book_category, \
                        'title' : books['title'],\
                        'author' : books['author'], \
                        'rating' : books['rating'], \
                        'publisher' : books['publisher'], \
                        'pages' : books['pages'], \
                        'language' : books['language']
        }
        book_list.append(new_book)

# sort list by title, then publisher
book_list = bubbleSortListofDict(book_list, 'title')
book_list = bubbleSortListofDict(book_list, 'publisher')
pprint.pprint(book_list)

# # TODO: There are duplicate titles (as the CSV has a row for each category
# and a book can be in more than one category

# loop through books to check it is sorted by publisher then title.
# book_list is a list of books
for book in book_list:
    print ("pub:", book['publisher'], "title: ", book['title'][:20])
