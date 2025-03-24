# Current Principal: 500
# Annual Addition: 1000
# Years to grow: 30
# Interest Rate: 10
# Result: 189668.13

current = 500
annual_addition = 1000
years = 30
interest_rate = 10

total = current


for i in range(years):
    total = total + annual_addition
    total = total + (interest_rate * total / 100)

print (total)