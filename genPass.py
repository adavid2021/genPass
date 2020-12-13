import secrets

# generates passwords using secrets module
def genPass(n = 8, final = ""):
    if (len(final) > 8):
        return final
    
    out = ""
    specs = "#,$,%,&,',(,),*,+,-,.,/,:,;,<,=,>,?,@,[,\,],^,_,`,{,|,},~"
    r = secrets.randbelow(int(n * 4/5))
    
    if (r == 0):
        r = 1
    
    for item in range(r):
        out += secrets.choice(specs.split(","))
        
    pas = secrets.token_urlsafe(secrets.randbelow(n)) + out + secrets.token_urlsafe(secrets.randbelow(n))
    
    return genPass(n, final + pas)

print("\n")
print(genPass(5))
print("\n")