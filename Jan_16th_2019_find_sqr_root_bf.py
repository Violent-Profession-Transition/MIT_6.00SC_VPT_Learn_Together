# this is a program to find the square root of a Number
# within the error margin (err_margin)

input_Number = float(input("give me a number please "))
number_Guesses = 0 # how many times it takes to guess sqrt root
guess = 0 # initial guess for square root
err_margin = 1 # error margin
increment = 0.001 # increment value for each iteration

top_margin = input_Number + err_margin
bottom_margin =input_Number - err_margin

while (guess**2 > top_margin or guess**2 < bottom_margin) and (guess <= input_Number):
    # increment guess until stop condition
    # guess start from initial value of 0
    guess += increment
    number_Guesses += 1

print("number of guess taken: ", number_Guesses)
print("for error margin of between ", err_margin)
print("each iteration increment by ", increment)
if guess >= input_Number:
    # no answer found
    print("no answer found")
else:
    print("the answer is: ", guess)

