num = int(input("Enter a number: "))
if num % 2 == 0:
    print("THE NUMBER IS DIVISIBLE BY 2")
elif num % 3 == 0:
    print("THE NUMBER IS DIVISIBLE BY 3")
# elif num % 2 == 0 and num % 3 == 0:
#     print("THE NUMBER IS DIVISIBLE BY BOTH 3 AND 2") // IN THIS CASE IT WILL ONLY SHOW DIVISIBLE BY 2 IN THE OUTPUT 
else:
    print("THE NUMBER IS NOT DIVISIBLE BY 3 OR 2")