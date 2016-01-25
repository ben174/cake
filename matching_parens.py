

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
