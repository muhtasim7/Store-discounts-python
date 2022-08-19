# Author: Muhtasim Khan

# Date Created: 26/05/2021

"""

Description: This is a program that takes the total price

and calculates the varying discounts for the purchases over $40.

"""

# Variables: 

# price represents the price of the product without discount

# discount represents how much is being subtracted off from the total price

# finalPrice represents the final price of the product with the discount

#this prints out the discounts based on the purchases 

print ("""

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Purchases and Discounts:

$200 or more: $50 off the total price

$100 to $199.99: $20 off the total price

$40 to $99.99: $5 off the total price

Less than $40: No discount

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

""")

#input of the purchase

price =float(input("What is the total price (in $)? "))

"""

it is rounding the price to 2 decimal place because without it python does not recognize

the number, such as if you plug in 99.99999 it will not recognize that the number is between 

100 and 199.99 it will think the number does not require a discount

"""

price = round(price,2)

#processing the discounts

if price >= 200:

    discount = 50

elif 100<=price<=199.99:

    discount = 20

elif 40 <=price<= 99.99:

    discount= 5

else:

    discount=0

finalPrice = (price - discount)

#output the result with the final price with rounding the final number to 2 decimal places 

print("The final price (including any discount) is $%.2f" %finalPrice)

