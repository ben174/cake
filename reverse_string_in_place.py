
def reverse_string(mystr):
    strlist = list(mystr)
    for i in xrange(len(strlist)/2):
        start_index = i
        end_index = -(i+1)
        strlist[i], strlist[-(i+1)] = strlist[-(i+1)], strlist[i]
    return "".join(strlist)


print reverse_string('hello how are you today?')
