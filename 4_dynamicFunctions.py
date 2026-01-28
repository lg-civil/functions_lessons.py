# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.
lists = (1, -1000, 25, -27)

def all_positives(lists):
    for numbers in lists:
        if numbers > 0:
            return True
    return False

print(all_positives(lists))
        
    



# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.

numbers = [150, 2000, 350, -50, 800, 999, 1001]
def sum_less(numbers):
    total = 0 
    for num in numbers:
        if 0 < num < 1000:
            total += num
    return total 
print(sum_less(numbers))




# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.













