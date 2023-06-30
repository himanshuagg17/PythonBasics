# Set 1
# quesiton 1 :- Write a Python program that prints "Hello, World!" to the console.
# print("hello world");

# question 2 :- Data Type Play: Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.

a=10
print(type(a), "value :", a);

name="himanshu"
print(type(name) , "value :", name );

x=3.14
print(type(x), "value :",x);

answer=False;
print(type(answer), "value :",answer);


# list
legends=["ABD", "VK" , "MSD", "Amla" , "smith"];
print(type(legends), "value :",legends);

# tuple (tuple data is in an order and cannot be changed whereas the list data has no order and can be changed)
marks=(12, 14, 18)
print(type(marks), "value :", marks);

# dictionary(it is like JSON files in JS)
student={"name":"himanshu",
         "interest":["coding","cricket"]}
print(type(student), "value :",student);

# set (it is an unordered collection like the list but no elements can repeat in a set)
marks={1,2,3,4};
print(type(marks), "value :",marks);


# question 3 :- List Operations: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.

# Create a list of numbers from 1 to 10
numbers = list(range(1, 11))
print("The List:", numbers)

# Add a number to the list
numbers.append(11)
print("After Adding 11th number:", numbers)

# Remove a number from the list
numbers.remove(2)
print("After Removing 2rd number:", numbers)

# Sort the list in ascending order
numbers.sort()
print("After Sorting:", numbers)


# question 4 : Sum and Average: Write a Python program that calculates and prints the sum and average of a list of numbers.

numbers=[12,11,21]

Sum=sum(numbers)
Average=Sum/len(numbers);
print("Sum :",Sum, "Average :",Average);

# question 5 : String Reversal: Write a Python function that takes a string and returns the string in reverse order.

def reverse(input_string):
    return input_string[::-1]

original_string = "Himanshu"
reversed_string = reverse(original_string)
print(reversed_string)

    
# question 6 : Count Vowels: Write a Python program that counts the number of vowels in a given string.

def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

# Example usage
text = "Himanshu aggarwal"
vowel_count = count_vowels(text)
print("Number of vowels:", vowel_count)


# question 7 : Prime Number: Write a Python function that checks whether a given number is a prime number.

def prime(number):
    if number < 2:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True


num = 11
if prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")


# question 8 Factorial Calculation: Write a Python function that calculates the factorial of a number.

def factorial(number):
    if number < 0:
        return "not valid for negative numbers"
    elif number == 0:
        return 1
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result


num = 5
fact = factorial(num)
print("Factorial of", num, "is", fact)


# question 9 Fibonacci Sequence: Write a Python function that generates the first n numbers in the Fibonacci sequence.

def fibonacci_sequence(n):
    sequence = []

    # Handle special cases for n = 0 and n = 1
    if n >= 1:
        sequence.append(0)
    if n >= 2:
        sequence.append(1)

    # Generate the Fibonacci sequence
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)

    return sequence


num = 10
fib_seq = fibonacci_sequence(num)
print("Fibonacci Sequence:", fib_seq)


# question 10 
# List Comprehension: Use list comprehension to create a list of the squares of the numbers from 1 to 10.
squares = [num**2 for num in range(1, 11)]

print(squares)
