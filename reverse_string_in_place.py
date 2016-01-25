
def reverse_string(mystr):
    strlist = list(mystr)
    for i in xrange(len(strlist)/2):
        start_index = i
        end_index = -(i+1)
        strlist[i], strlist[-(i+1)] = strlist[-(i+1)], strlist[i]
    return "".join(strlist)

def reverse_words(sentence):
    slist = sentence.split()
    for i in xrange(len(slist)/2):
        start_index = i
        end_index = -(i+1)
        slist[i], slist[-(i+1)] = slist[-(i+1)], slist[i]
    return ' '.join(slist)


print reverse_string('hello how are you today?')
message = 'find you will pain only go you recordings security the into if'

assert reverse_words(message) == 'if into the security recordings you go only pain will you find'

