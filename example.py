import math

A = 0 # number of signed up libraries
Output = []

def score(lib, D, S):
    return (D-lib.signup_days) * sum([S[i] for i in lib.book_ids]) / math.ceil(lib.num_books/lib.shipping_per_day)

def best_lib(libraries, D, S):
    highest_score = 0
    best_lib = None
    for lib in libraries:
        score = score(lib, D, S)
        if score > highest_score:
            highest_score = score
            best_lib = lib
    return(best_lib)

scanned = set() # scanned books
while D > 0 and libraries != []:
    # calculate overall_score for each lib
    # choose lib with max overall_score
    
    # process:
        # update score
        # update scanned books
        # update output
        # update D
        # remove this lib
        