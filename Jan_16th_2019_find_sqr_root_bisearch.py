# this is a program to find the square root of a Number
# within the range of error margin (err_margin)
# using bisection search

input_Number = float(input("give me a number please "))
number_Guesses = 0 # how many times it takes to guess sqrt root
err_margin = 0.001 # error margin
# increment = 0.001 # increment value for each iteration

top_margin = input_Number + err_margin
bottom_margin =input_Number - err_margin

lower_bound = 0 # initial lower_bound
upper_bound = input_Number # initial upper_bound
guess = input_Number/2 # initial guess for square root

# for number between 0 and 1
# sqrt_root will be larger than input_Number
# so guess**2 will never be greater than the top_margin
# so need to increase the search region to 1
if input_Number < 1:
    upper_bound = 1 + err_margin
    lower_bound = bottom_margin

while True:
    if input_Number == 1:
        guess = 1
        break
    guess = (lower_bound + upper_bound)/2
    print("guess: ", guess, "upper_bound: ", upper_bound, "lower_bound: ", lower_bound)
    if guess**2 > top_margin:
        upper_bound = guess
        number_Guesses += 1
    elif guess**2 < bottom_margin:
        lower_bound = guess
        number_Guesses += 1
    else:
        print("we found the answer")
        break


print("number of guess taken: ", number_Guesses)
print("for error margin of between ", err_margin)
if guess**2 > top_margin or guess**2 < bottom_margin:
    # no answer found
    print("no answer found")
else:
    print("the answer is: ", guess)
