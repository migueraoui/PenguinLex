from PenguinLex import penguin_lex

def lookup_term(term):
    term = term.lower()  
    if term in penguin_lex:
        return penguin_lex[term]
    else:
        return f"Sorry, the term '{term}' is not in the dictionary."

def add_term(term, definition):
    term = term.lower() 
    penguin_lex[term] = definition
    return f"Term '{term}' has been added to the dictionary."

print(lookup_term('Linux'))  
print(lookup_term('bash'))  


