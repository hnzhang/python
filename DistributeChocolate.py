def distribute_chocolate(points):
    if not points:
        return 0
    chocolates = [1]*len(points)
    for i in range(1, len(points)):
        if points[i] > points[i-1] and chocolates[i] <=  chocolates[i - 1]:
            points[i] = points[i-1] + 1
    print("after round 1:", chocolates)
    for i in reversed(range(0, len(points)-1)):
        if points[i] > points[i+1] and chocolates[i] <= chocolates[i+1]:
            chocolates[i] = chocolates[i+1] + 1
    return sum(chocolates) 