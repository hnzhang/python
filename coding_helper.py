def levelFieldTime(numRows, numColumns, field):
    #idea: use a heap to track all the trees, also know which should be cut in sequence.

    import heapq
    
    heap = []
    #find all trees to be cut
    for row in range(numRows):
        for col in range(numColumns):
            if field[row][col] > 1:#this is a tree
                heapq.heappush(heap, (field[row][col], row, col ) )
    
    #if the heap size is 0, no cut is needed this is corner case
    if not heap:
        return 0
    
    #for each cut try:
    #   find a shortest path from start to the destination using bfs
    #   if a path cannot be reached
    #    the try failed, and return -1
    #   else:
    #       totalCost += move_cost + cut_cost
    total_cost = 0
    from_row = 0
    from_col = 0
    from collections import deque
    
    while heap:
        tree_to_cut = heapq.heappop(heap)
        to_row = tree_to_cut[1]
        to_col = tree_to_cut[2]
        #find shortest path between from to to
        que = deque()
        from_node = (from_row, from_col)
        to_node = (to_row, to_col)
        que.append( from_node )
        parent_info= {from_node:None}
        path_found = False
        while que and not path_found:
            node = que.popleft()
            candidates = []
            if node[0]>0:#row greater than 0
                candidates.append( (node[0] -1, node[1]) )
            if node[0] + 1 < numRows:
                candidates.append(  (node[0]+1, node[1]) )
            if node[1] >0:#col greater than 0
                candidates.append(  (node[0], node[1] -1) )
            if node[1] + 1 < numColumns:
                candidates.append( (node[0], node[1] + 1) )
            for candidate  in candidates:
                if candidate == to_node:
                    parent_info[candidate] = node
                    path_found = True
                    break
                elif field[candidate[0]][candidate[1]] == 1 and candidate not in parent_info:
                    #only flat area are moveable and 
                    parent_info[candidate] = node
                    que.append(candidate)
        #construct_path
        if not path_found:
            return -1
        
        node = (to_row, to_col)
        #path = [node]
        #get moving cost
        moving_cost = 0
        while node != from_node:
            node = parent_info[node]
            moving_cost += 1
        #calculate cost
        total_cost +=  moving_cost + field[to_row][to_col]#cut the tree taking X secs
        field[to_row][to_col] = 1#make it flat
        #move to new location
        from_row = to_row
        from_col = to_col

    return total_cost

field = [
    [1,1,0,5],
    [0,1,1,4]
]

print(levelFieldTime(2,4,field))

field = [
    [1,1,0,12,1,13],
    [1,1,1,1,0,0],
    [0,1,0,0,0,0],
    [0,1,1,1,14,0],
    [0,0,0,0,1,0],
    [15,1,1,1,1,1]
]
print(levelFieldTime(6,6, field))