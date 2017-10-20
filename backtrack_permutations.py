def is_a_solution(path, k, input_set:list):
    return k == len(input_set)

def process_solution(path:list, k:int, input_set:list):
    print("{", end="")
    for i in range(k):
        print(input_set[path[i]], end='')
    print("}",end='')

def construct_candidates(path, k, input_set, candidates):
    in_perm = [False]* len(input_set)
    for i in range(k):
        in_perm[path[i]] = True#used already
    for i in range(len(in_perm)):
        if in_perm[i] == False:
            candidates.append(i)

def back_track(path, k, input_set):
    if is_a_solution(path, k, input_set):
        process_solution(path, k, input_set)
    else:
        k += 1
        #get condidates
        candidates = []
        construct_candidates(path, k-1, input_set, candidates)
        for c in candidates:
            path[k-1] = c 
            back_track(path, k, input_set)

def get_permutation(input_set):
    path = [0]*len(input_set)
    back_track(path, 0, input_set)

get_permutation("1234")

