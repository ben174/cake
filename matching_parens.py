

def matching_parens(sentence, pindex):
    stack = []
    for index, char in enumerate(sentence):
        if char == '(':
            if index == pindex:
                stack.append('*')
            else:
                stack.append('(')
        elif char == ')':
            if stack.pop() == '*':
                print index
                return index



sentence = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
assert matching_parens(sentence, 10) == 79

def validate_parens(sentence):
    openers = ['{', '[', '(']
    closers = ['}', ']', ')']
    stack = []
    for index, char in enumerate(sentence):
        if char in openers:
            stack.append(char)
        elif char in closers:
            if not stack.pop() == openers[closers.index(char)]:
                return False
    return True


assert validate_parens("{ [ ] ( ) }")
assert not validate_parens("{ [ ( ] ) }")
assert not validate_parens("{ [ }")
