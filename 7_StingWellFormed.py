def String_is_Well_Formed(exp):
    
    left = '{[('
    right = '}])'
    stack = []
    
    for char in exp:
        if char in left:
            stack.append(char)
        elif char in right:
            if len(stack) == 0:
                return False
            else:
                top = stack.pop()
                if left.index(top) != right.index(char):
                    return False
    
    return len(stack) == 0

print(String_is_Well_Formed('{[(([{a+b}]+c))]}'))
print(String_is_Well_Formed("}{"))