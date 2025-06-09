# Calculate the electricity bill based on consumption: ₹5 per unit for the first 100
# units, ₹10 per unit for the next 200, ₹15 per unit for anything above 300 units.

units = int(input('Enter units used : '))
rate_cost  = 0.0
if  units <= 100:
    rate_cost = units * 5
    #print(f'Rate of cost: {rate_cost}')
elif units <= 200:
    remaining_units = units - 100
    rate_cost = rate_cost + ((units - 100) * 10)
else:
    rate_cost = (100 * 5) + (100 * 10)
    rate_cost = rate_cost + ((units - 200) * 15)

print(f'electricity bill: {rate_cost}')

'''
output
--------
Enter units used : 34
electricity bill: 170

Enter units used : 127
electricity bill: 270.0

Enter units used : 226
electricity bill: 1890
'''
