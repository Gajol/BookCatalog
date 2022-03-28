import csv
import pprint

book_str_simple = """title,author,rating,publisher,pages,category,language
Title1,Author1,1,Pub-1,10,Category 1,Language 1
Title3,Author3,3,Pub-3,30,Category 3,Language 1
Title2,Author2,2,Pub-2,20,Category 2,Language 2"""

book_str_basic = """title,author,rating,publisher,pages,category,language
After Anna,Alex Lake,4.1,HarperCollins UK,416,Fiction,English
The Joker,Brian Azzarello,4.4,DC,130,Comics,English
Venomized,Cullen Bunn,4.5,Marvel Entertainment,136,Comics,English
Bring Me Back,B A Paris,3.8,HarperCollins UK,368,Crime,English"""

# choose which book-csv to test
book_str = book_str_simple
#book_str = book_str_basic
#book_str = book_str_google

# book_dict_reader = csv.DictReader(io.StringIO(book_str))  // needs: import io
book_dict_reader = csv.DictReader(book_str.splitlines())

print(book_dict_reader.fieldnames)

# Convert DictReader object to a list of dictionaries
book_list_of_dict = list(book_dict_reader)

print ("\nBook Dict Unsorted")
#print (book_list_of_dict)
pprint.pprint(book_list_of_dict)
print ("\n")

# create a list sorted by publisher
for j in range(len(book_list_of_dict)):
  swapped = False
  i = 0
  while i < len(book_list_of_dict) - 1 :
    if book_list_of_dict[i]['publisher'] >  book_list_of_dict[i+1]['publisher'] :
      # swap
      # print("swapping")
      book_list_of_dict[i],   book_list_of_dict[i+1] = \
      book_list_of_dict[i+1], book_list_of_dict[i]
      swapped = True
    i = i + 1

  # break if list is sorted
  if swapped == False :
    #print("...breaking, list is sorted")
    break


print ("\nBook Dict Sorted")
pprint.pprint(book_list_of_dict)
print ("\=================")
print ("\n")
