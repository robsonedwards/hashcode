#python 3.6

INPUT = "a_example.txt"

f = open(INPUT, "r")

line = f.readline()
B, L, D = line.split(" ") # number of books, libraries, and days, respectively

line = f.readline()
S = line.split(" ") # array of book scores (books 0 to B-1)

line = f.readLine()
while line is not None:
    # read in info on each of the L libraries 0 to L-1
    line = f.readLine()
    pass

