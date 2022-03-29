import csv
import pprint

# iterate through books and find duplicate titles...
# assumption if "Titles are same" then all other fields are the same.
#   - only category can be the list of categories

# ------------------------------
book_str_nano = """title,publisher
TitleB,Pub-1
Title3,Pub-3
Title2,Pub-2
TitleA,Pub-1"""

book_str_simple = """title,author,rating,publisher,pages,category,language
TitleB,Author1,1,Pub-1,10,Category 1,Language 1
TitleB,Author3,3,Pub-3,30,Category 9,Language 1
TitleB,Author2,2,Pub-2,20,Category 2,Language 2
TitleA,Author3,3,Pub-1,30,Category 3,Language 1"""

book_str_dup_title = """title,author,rating,publisher,pages,category,language
TitleB,Author1,1,Pub-1,10,Category 1,Language 1
Title3,Author3,3,Pub-3,30,Category 3,Language 1
TitleB,Author2,2,Pub-2,20,Category 2,Language 2
TitleB,Author3,3,Pub-1,30,Category 3,Language 1"""


book_str_basic = """title,author,rating,publisher,pages,category,language
After Anna,Alex Lake,4.1,HarperCollins UK,416,Fiction,English
The Joker,Brian Azzarello,4.4,DC,130,Comics,English
Venomized,Cullen Bunn,4.5,Marvel Entertainment,136,Comics,English
Bring Me Back,B A Paris,3.8,HarperCollins UK,368,Crime,English"""

# choose which book-csv to test
#book_str = book_str_nano
book_str = book_str_simple
#book_str = book_str_basic
#book_str = book_str_google
#book_str = ""

if (not book_str) :
  # read from google CSV file
  book_dict_reader = csv.DictReader(open("google_books_dataset.csv"))
else:
  book_dict_reader = csv.DictReader(book_str.splitlines())

print(book_dict_reader.fieldnames)
# ------------------------------


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
book_list_of_dict = list(book_dict_reader)

# sort list by title, then publisher
book_list_of_dict = bubbleSortListofDict(book_list_of_dict, 'title')

# merge same titled book's categories
# list is sorted by "book's title"
# ideas:
#  1) double-loop : take an item from list and compare to all other items
#  2) but we know list is sorted, so take item, & compare while matching, once
#     it is not matching, we know the title has changed.
pprint.pprint(book_list_of_dict)

print("\n1. Merging matching Titles - Category list []\n")
print("Type: ",type(book_list_of_dict))
for book in book_list_of_dict[:-1]:
  print (book)

book_unique_title_list_of_dict = []
print("\n2. Merging matching Titles - Category list []\n")
last_title = ""
for index, book in enumerate(book_list_of_dict[:-1]):
  print (index, book['title'])
  print ("Category is of type: ", type(book['category']))

  if book['title'] != last_title:
      # found a new book title, add to our new unique list of books
      last_title = book['title']
      book_unique_title_list_of_dict.append(book)

      # see if the next books have the same title
      # iterate throught a slice of the book_list
      # slice [ initial : end : jump ]
      #   inital = where we are currently in list = index
      #   end = entire list no need to speciy
      #   jump = 1 = no need to specify
      # while book['title'] == book_list_of_dict[index+no_matching_titles]['title']:
      # for loop iteration (break, pass, continue) - break out if titles are not matching
      for next_book in book_list_of_dict[index+1:]:
        # del book_list_of_dict[index+no_matching_titles]
        print ("......category", book['category'])
        if book['title'] == next_book['title']:
            print ("Removed a duplicate book titled", book['title'])
            # [-1] accesses last element added to the list
            # This is not at all the assignment, but I thought it was cute...
            book_unique_title_list_of_dict[-1]['category'] += ", " + next_book['category']
        else:
            print ("Titles don't match")
            break
  else:
        # Books' category has been added in the above loop
        print ("skipping - title already exists")

  # pprint
  pprint.pprint(book_unique_title_list_of_dict)
