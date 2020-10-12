'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    
    sub = 'th'
    count = 0

    word_len = len(word)
    sub_len = len(sub)

    if (word_len == 0 or word_len < sub_len):
        return 0

    if (word[ : sub_len] == sub):
        # count +=1
        # print('elif', word)
        # print(count)
        return count_th(word[sub_len-1:]) + 1
    
    else:    
        # print('else', word)
        # print(count)
        return count_th(word[sub_len-1:])

    # print('count', count)

    return count 

    # non-functional code that I don't want to throw away
    # in case I come back to work on this later
    
    
    # if word[0] == 't' and word[1] == 'h':
    #     count +=1

    # count += count_th(word[1:])

    # return count 



if __name__ == '__main__':

    word = 'hitherethouthat'
    print(count_th(word))

    word2 = 'thhtthht'
    print(count_th(word2))
