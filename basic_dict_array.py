book_str_nano = """title,publisher
TitleB,Pub-1
Title3,Pub-3
Title2,Pub-2
TitleA,Pub-1"""

book_dict_reader = csv.DictReader(book_str_nano.splitlines())
