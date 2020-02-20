INPUT = "a_example.txt"

f = open(INPUT, "r")

line = f.readline()
B, L, D = line.split(" ")
print(B, L, D)
#while line is not None:
#    pass
