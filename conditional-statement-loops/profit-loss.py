# Check for profit and loss 
cost_price = int(input('enter the cost price of the product: '))
selling_price = int(input('enter the selling price if the product: '))
if cost_price<selling_price:
    profit = selling_price-cost_price
    print(f'Profit of:{profit}')
elif cost_price>selling_price:
    loss = cost_price-selling_price
    print(f'Loss of:{loss}')
else:
    print('No profit No loss')