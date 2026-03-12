# Key Idea: Greedy(Kadane style)
# - Traverse from the first to last
# - - Identify the min price
# - - If current price is greater than min price
# - - - Calculate the profit if selling the stock at this day
# - - If the profit is greater than current max profit 
# - - - Re-assign the value for max profit and sell date

def trade_stock(price_histories: list)->tuple:
    min_price = float("inf")
    buy_date = 0
    sell_date = 0
    max_profit = 0

    for date, stock_price in enumerate(price_histories):
        if min_price > stock_price:
            min_price = stock_price
            buy_date = date

        profit = stock_price - min_price
        
        if profit > max_profit:
            sell_date = date
            max_profit = profit

    return buy_date, sell_date, max_profit


print(trade_stock([7,1,5,3,6,4]))
        
