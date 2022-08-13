# input a number and see if it is a prime number or not

def determine_prime(number):
    is_prime = True
    for i in range(2, number):
        if number % 2 == 0:
            is_prime = False
    if is_prime:
        print("It is a prime number!")
    else:
        print("It is not a prime number")


number_to_be_checked = int(input("Insert a number to determine if it is a prime: "))

determine_prime(number_to_be_checked)
