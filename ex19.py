import sys

def cheese_and_crackers(cheese_count, box_count):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {box_count} boxes of crackers")
    print("Man, that's enough for a party.")
    print("Get a blanket. \n")

print("We can give the function numbers directly")
cheese_and_crackers(20,30)

print("Or, we can use variables from our script")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can do math inside a funciton too.")
cheese_and_crackers(10+20, 5+6)

print("And we can combine the two, math and variables.")
cheese_and_crackers(100+amount_of_cheese, 100+amount_of_crackers)
