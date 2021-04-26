#!/usr/bin/env python
# coding: utf-8

# ## Problem 1 - Simple temperature calculator (*3 points*)
# 
# In the first problem your aim is to create a function that converts the input temperature from degrees Fahrenheit to degrees Celsius. The conversion formula from Fahrenheit to Celsius can be found below.
# 
#   T_{Celsius} = ( T_{Fahrenheit} - 32 ) / 1.8
# 
# Notice: Closely follow the instructions! 
# 
# Your score on this problem will be based on following criteria:
# 
# - Creating a function called `fahr_to_celsius`
# - Defining the function to have one input parameter called `temp_fahrenheit`
# - Creating a variable called `converted_temp` inside the function to which you should assign the conversion result (i.e., the input Fahrenheit temperature converted to Celsius)
# - Returning the converted value from the function back to the user
# - Answering some questions about functions at the end of this problem
# - Adding comments in your code and a docstring that explains how to use your `fahr_to_celsius` function (i.e., you should write the purpose of the function, parameters, and returned values)

# YOUR CODE HERE

#fahr_to_celsius() is the function which change fahr to celsius
def fahr_to_celsius(temp_fahrenheit):
    #converted_temp is the changed variable(fahr to celsius)
    converted_temp = ( temp_fahrenheit - 32 ) / 1.8
    return converted_temp

# ### Problem 1 tests
# 
# Check that the function produces correct answers for:
# 1. What is 48° Fahrenheit in Celsius? 
# 2. What about 71° Fahrenheit in Celsius?

# ### Check your code
#Print the answer for 1.
print('1. 48° Fahrenheit in Celsius is '+str(round(fahr_to_celsius(48),2)))
#Print the answer of 2.
print('2. 71° Fahrenheit in Celsius is '+str(round(fahr_to_celsius(71),2)))

# - Make sure you used the given variable names
# - Check that you have added necessary comments to your code
# - Check that your function has a docstring that describes what it does
# 
# ### Questions
# 
# We would like you to think about and answer the following questions based on the materials and ideas that you learned during the lecture:
# 
#   1. Is the concept of function clear to you? If not, what do you not understand?
#   2. What are some of the benefits of using functions?
#   
# Write your answers below:

# YOUR ANSWER HERE. Write your answers as comments

#1. I creally understood the baisic ways to use function.
#

#2. There are three advantages of the function.
#First of all, you can make program.
#The second, being able to omit a calculation procedure for the same processing.
#The third, promote efficiency of each other's work by sharing function all over the world. 
#

# #### Done!
# 
# That's it! Now you are ready to continue with Problem 2.
