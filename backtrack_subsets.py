def is_a_solution(path:list, k:int, input_set:int):
    return k == len(input_set)

def construct_candidates(path:list, k:int, input_set:list, candidates:list, num_candidates:int):
    '''
    '''
    candidates[0] = True
    candidates[1] = False

def process_solution(a:list, k:int, n:int):
    print("{",end="")
    for i in range(k):
        if a[i]:
            print(n[i],end="")
    print("}", end="")

def backtrack(path:list, k:int, input_set:int):
    if  is_a_solution(path, k, input_set):
        process_solution(path,  k, input_set)
    else:
        k += 1
        num_candidates = 2
        candidates = [True] * num_candidates
        construct_candidates(path, k, input_set,candidates, 2)
        for i in range(num_candidates):
            path[k-1] = candidates[i]
            #make_move()
            backtrack(path, k, input_set)
            #unmake_move()
            #if finished:
            #    return;

def generate_subsets(input_set:list):
    path=[True]*len(input_set)
    backtrack(path, 0, input_set)

generate_subsets(["A","B","C"])