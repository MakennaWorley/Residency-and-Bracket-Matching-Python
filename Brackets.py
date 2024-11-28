'''
Brackets.py

Makenna Worley

'''

def Brackets(s):
    stack = []

    for c in s:
        match c:
            case '(':
                stack.append(c)
            case ')':
                if stack:
                    if '(' != stack.pop():
                        return False
                else:
                    return False
            case '[':
                stack.append(c)
            case ']':
                if stack:
                    if '[' != stack.pop():
                        return False
                else:
                    return False
            case '{':
                stack.append(c)
            case '}':
                if stack:
                    if '{' != stack.pop():
                        return False
                else:
                    return False

    if stack:
        return False

    return True



print(Brackets(''))
print(Brackets('([{}])'))
print(Brackets('(())[]{}'))

print(Brackets(')'))
print(Brackets('(()))'))
print(Brackets('[]{)'))
