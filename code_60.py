# Best time to Buy and Sell Stock
def max_profits(prices):
    l,r=0,1 #l is buying and r is selling
    maxP=0
    while r<len(prices):
        if prices[l]<prices[r]:
            profit=prices[r]-prices[l]
            maxP=max(maxP,profit)
        else:
            l = r 
        r+=1
    return maxP
prices=[7,1,5,3,6,4]
print("Max Profit:", max_profits(prices))