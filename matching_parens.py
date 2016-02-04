

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




def find_permutations(string, start=None):
    if not start:
        start = string[0]
    slist = list(string)[1:]
    print start
    print slist
    perms = []
    for char in string:
        return perms(slist)
    string[0]


def perms(slist):
    ret = []
    stump = slist[:-1]
    for index in slist[:-1]:
        perm = slist[0:index] + [slist[0]] + slist[index:]
        ret.append(perm)
        print ret
        ret.extend(perms(perm))
    print ret
    return

    print char

    print '({}){}'.format(first_char, ''.join(slist))
    slist = list(slist)
    ret = []
    if(len(slist) == 1):
        return [first_char + slist[0]]
    for index, char in enumerate(slist):
        newlist = slist[:]
        del newlist[index]
        ret.extend(perms(char, newlist))
    return ret



def find_dupe(alist):
    while True:
        curr = alist.pop()
        if curr in alist:
            return curr


print find_dupe([1,2,3,4,5,4,8,9])

#print perms('isogram')


