import math

def score(lib, D, S):
    return (D-lib.signup_days) * sum([S[i] for i in lib.book_ids]) / math.ceil(lib.num_books/lib.shipping_per_day)

def best_lib(libraries, D, S):
    highest_score = 0
    best_lib = None
    for lib in libraries:
        scor = score(lib, D, S)
        if scor > highest_score:
            highest_score = scor
            best_lib = lib
    return(best_lib)

def solution(libraries, D, S):
    A = 0 # number of signed up libraries
    Output = []
    
    scanned = set() # scanned books
    while D > 0 and len(libraries)!=0 and sum(S)>0:
        print('*')
        # calculate overall_score for each lib
        # choose lib with max overall_score
        lib = best_lib(libraries, D, S)
        # update output
        A += 1 # increment library counter
        Output.append([lib.id]) # append output
        
        scanned_books = sorted([id for id in list(lib.book_ids) if S[id]!=0], key = lambda id: S[id])[:min((D-lib.signup_days)*lib.shipping_per_day, len(lib.book_ids))]
        
        # update book scores
        for book in scanned_books: 
            S[book] = 0
        Output[-1].append(len(scanned_books))
        Output[-1].append(scanned_books)
        
        # update scanned books
        scanned.update(scanned_books)

        # update D
        D -= lib.signup_days
        
        # remove this lib
        libraries.discard(lib)
        
    return(A, Output)
        
def make_output(A, Output, filename):
    with open(filename, "w") as file:
        file.write(A)
    