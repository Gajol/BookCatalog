import csv
import pprint
def bubbleSort( theSeq ):
    n = len( theSeq )
    for i in range( n - 1 ) :
        flag = 0
        for j in range(n - 1) :
            if theSeq[j] > theSeq[j + 1] :
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
                flag = 1
        if flag == 0:
            break
    return theSeq

el = [21,6,9,33,3]
result = bubbleSort(el)
print (result)

# ------------------------------
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
book_str = book_str_nano
#book_str = book_str_simple
#book_str = book_str_basic
#book_str = book_str_google

# book_dict_reader = csv.DictReader(io.StringIO(book_str))  // needs: import io
book_dict_reader = csv.DictReader(book_str.splitlines())

print(book_dict_reader.fieldnames)

# Convert DictReader object to a list of dictionaries
book_list_of_dict = list(book_dict_reader)


def bubbleSortListofDict( theSeq, sortBy ):
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

book_list_of_dict = bubbleSortListofDict(book_list_of_dict, 'title')
book_list_of_dict = bubbleSortListofDict(book_list_of_dict, 'publisher')

print ("\nBook Dict Sorted")
pprint.pprint(book_list_of_dict)
print ("\n")
