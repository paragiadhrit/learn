import sys
import math
##choose function
def choose_function():
    def is_float(element):
        try:
            float(element)
            if "." in element and float(element) % 1 != 0:
                sys.exit("Only natural numbers.")
                return True
        except ValueError:
            return False
    ##total_amount
    n_str = input("How many are you choosing from? ")
    is_float(n_str)
    n = int(n_str)
    ##choosing_amount
    r_str = input("How many are you choosing? ")
    is_float(r_str)
    r= int(r_str)
    ##calc
    ##n!
    numerator_choose = math.factorial(int(n))
    ## (n-r)! * r!
    denominator_choose = math.factorial(int(n-r))* math.factorial(int(r))
    possibilites_choose = numerator_choose / denominator_choose


    print("The amount of ways to choose ", str(r), "things out of ", str(n), "things is ", str(int(possibilites_choose)))

## simple_permutation function
def simple_permutation_function():
    def is_float(element):
        try:
            float(element)
            if "." in element and float(element) % 1 != 0:
                sys.exit("Only natural numbers.")
                return True
        except ValueError:
            return False
    ##total amount
    n_str = input("What is the total amount of items? ")
    is_float(n_str)
    n= int(n_str)
    ##amount being arranged
    r_str = input("How many items are being arranged? ")
    is_float(r_str)
    r= int(r_str)
    ##calc
    ##n!
    numerator_permutation = math.factorial(n)
    ##(n-r)!
    denominator_permutation= math.factorial(n-r)
    possibilites_permutations= numerator_permutation / denominator_permutation

    print("The amount of ways to arrange", r_str, "items from", n_str, "items is", str(int(possibilites_permutations)))

## system start
perm_or_choose = input("Would you like to do a simple permutation or choose calculation? Answer using P or C. ")
if perm_or_choose == "P" or "p" or "permutation" or "Permutation":
    simple_permutation_function()
elif perm_or_choose == "C" or "c" or "choose" or "Choose":
    choose_function()
else:
    sys.exit("No function with the name{'perm_or_choose'}")
