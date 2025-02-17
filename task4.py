# Task 1a: Write a Python function that takes a list of numbers as input and returns a new list containing only the even numbers.
# l = [10,11,3,2,7,6]
# newl = list(filter(lambda x : x%2 == 0 , l))
# print(newl)
# Task 2a: Create a function that accepts a string and returns the string in reverse order without using built-in reverse functions.
# def reversing():
#     y = str(input("Enter a string :"))
#     newl = "".join(map(lambda x : y[len(y) - 1 - x] , range(len(y))))
#     print(newl)
# reversing()
# Task 1b: Use a lambda function to filter out odd numbers from a given list of integers.
#l = [10,11,3,2,7,6]
# newl = list(filter(lambda x : x%3 == 0 , l))
# print(newl)
#Task 2b: Write a lambda function to find the square of a given number and use it with the map() function to square all elements in a list.
# l = [2,3,4,5,6,7,8]
# newl = list(map(lambda x : x*x , l))
# print(newl)
#Task 1c: Given a list of numbers, use the map() function to create a new list where each number is multiplied by 2.
# l = [2,3,4,5,6,7,8]
# newl = list(map(lambda x : x*2 , l))
# print(newl)
#Task 2c: Use the reduce() function from the functools module to find the product of all elements in a list.
# from functools import reduce
# l = [2,3,4,5,6,7,8]
# newl = reduce(lambda x,y : x*y , l)
# print(newl)
# Task 1: Write a simple decorator that logs the execution time of a function.
# import time
# def log(fx):
#     def mfx(*args, **kwargs):
#         start = time.time()
#         result = fx(*args, **kwargs)
#         end = time.time()
#         print(f"{fx.__name__}{end - start:.6f} seconds")
#         return result
#     return mfx
# @log
# def func():
#     time.sleep(1)  # Simulating delay
#     print("Hello!")
 
# func()
def log(fx):
    def mfx():
        print("Execution Started")
        fx()
        print("Execution Completed")
    return mfx
 
@log
def hello():
    print("Hello!")
 
hello()
