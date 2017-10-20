import sys

def MinNumOfCoins(listOfCoins, total):
    '''
    return a num telling minimum  number of coins needed to make up the total

    listOfCoins--all available coins
    total, an integer
    '''
    if total == 0:
        return 0

    dp = [sys.maxsize] * (total + 1)
    dp[0] = 0
    for coin in listOfCoins:
        for i in range(total+1):
            if coin <= i and (dp[i - coin] + 1) < dp[i]:
                dp[i] = dp[i - coin] +1

    return dp[total]

def test():
    '''
    test cases
    '''
    listOfCoins = [1, 3, 5]
    print("All Coins", listOfCoins)
    for i in range(16):
        print("for total: ", i, MinNumOfCoins(listOfCoins, i), " Coins needed")

test()