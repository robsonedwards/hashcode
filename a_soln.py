#python 3.6
class Library:
    def __init__(self, num_books = 0, signup_days = 0, shipping_per_day = 0,
                 book_ids = set(), id = -1):
        self.num_books = num_books
        self.signup_days = signup_days
        self.shipping_per_day = shipping_per_day
        self.book_ids = book_ids
        self.id

    def __str__(self):
        return "Library: TODO"

INPUT = "a_example.txt"

with open(INPUT, "r") as f:
    lines = f.read().splitlines() # removes \n, probably better way to do this

B, L, D = (int(x) for x in lines[0].split(" ")) # number of books, libraries, and days, respectively
S = [int(x) for x in lines[1].split(" ")] # list of book scores (books 0 to B-1)

libraries = []
i = 2
while i < len(lines):
    # read in info on each of the L libraries 0 to L-1
    line = lines[i]
    library = Library()
    library.num_books, library.signup_days, library.shipping_per_day = (
        int(x) for x in line.split(" "))
    library.id = i - 2
    
    i += 1
    line = lines[i]
    library.book_ids = {int(x) for x in line.split(" ")}
    
    libraries.append(library)

    i += 1
    
# debugging
print("B: ", B, ", D: ", D, ", S: ", S, sep = "")
for library in libraries:
    print(library.num_books, library.signup_days, library.shipping_per_day,
          library.book_ids, library.id)
