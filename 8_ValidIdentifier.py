lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
under_score = '_'
digit = '1234567890'

def valid_first_character(string):
    return (string[0] in lower) or (string[0] in upper) or (string[0] == '_')

def valid_Nonfirst_character(kar):
    return (kar in lower) or (kar in upper) or (kar in digit) or (kar == under_score)

def valid_identifier(string):
    
    if valid_first_character(string):
        
        i = 1 
        while (i < len(string)):
            if valid_Nonfirst_character(string[i]):
                i = i+1 
            else:
                break;
        return (i == len(string))
    else:
        return False
    
print(valid_identifier("Akash_Babu"))
print(valid_identifier("babushata"))