def regex_match(first, second):
    '''
    first is the pattern, second is the string.
    regex_match returns true if second matches the pattern, otherwise, returns false
    '''
    history = [False] * (len(first) +1)
    history[0] = True #base case: empty string always match with empty string
    for i in range(0, len(first)):
        history[i+1] = first[i] == '*' and history[i]

    for i in range(0, len(second)):
        print(history)
        new_history = [False] * (len(first) +1)
        for j in range(0, len(first)):
            if first[j] == '?':
                new_history[j+1] = history[j]
            elif first[j] == '*':
                new_history[j+1] = history[j+1] or new_history[j]
            else:
                new_history[j+1] = first[j] == second[i] and history[j]
        history = new_history
    print(history)
    return history[-1]
def match2(first, second):
    p = 0;index = 0; match_p = -1; match_i = -1
    while index < len(second):
        if p < len(first) and (first[p] == '?' or first[p] == second[index]):
            p += 1; index += 1
        elif p < len(first) and  first[p] == '*':
            match_i = index; match_p = p
            p += 1
        elif match_p != -1:
            p = match_p + 1
            index = match_i + 1
            index += 1
        else:
            return False
    while p < len(first) and first[p] == '*':
        p += 1
    return p == len(first)

def test():
    patten_list  = ["fi*de",    "fir?code",   'fi*d?',    "fi*d?",      "*i*d?",        '?i?e*d?', "*i?e*d?"]
    second_list  = ["firecode","firecode",    "firecode", "firecodee",  'fabfirecode',  'fairecode',"firecode"]
    #patten_list  = [ '?i?e*d?' ]
    #second_list  = ['fairecode']
    for i in range(0, len(patten_list)):
        first = patten_list[i]
        second = second_list[i]
        print("inputs:", first, second)
        if regex_match(first, second):
            print ("<<<<Yes>>>>")
        else:
            print ("==No==")
    for i in range(0, len(patten_list)):
        first = patten_list[i]
        second = second_list[i]
        print("inputs:", first, second)
        if match2(first, second):
            print ("<<<<Yes>>>>")
        else:
            print ("==No==")
        
test()