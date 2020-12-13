import secrets

# generates passwords using the Python secrets module
def genPass(n = 8, final = ""):
    
    # recursive base case, returns the password if the final string is longer than 8 characters
    if (len(final) > 8):
        return final
    
    out = ""
    
    # a list of special characters
    specs = "#,$,%,&,',(,),*,+,-,.,/,:,;,<,=,>,?,@,[,\,],^,_,`,{,|,},~"
    
    # generates the number of special characters to be added
    r = secrets.randbelow(int(n * 4/5))
    
    # ensures there is at least one special character
    if (r == 0):
        r = 1
    
    # adds the special character(s) to the token
    for item in range(r):
        out += secrets.choice(specs.split(","))
    
    # generates the password token
    pas = secrets.token_urlsafe(secrets.randbelow(n)) + out + secrets.token_urlsafe(secrets.randbelow(n))
    
    # recursive call to add characters to the final password string
    return genPass(n, final + pas)

# printing the password
print("\n")
print(genPass(5))
print("\n")
