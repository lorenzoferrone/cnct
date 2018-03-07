def multiple3: 3 % 0 =

def multiple5: 5 % 0 =

def multiple15: 15 % 0 =

def rangeFrom1: 1 switch interval 


def fizzbuzz n: 
    (
        (n multiple15 ['FizzBuzz']) # if
        (n multiple5 ['Buzz'])      # elif
        (n multiple3 ['Fizz'])      # elif
        [n]                         # else
    ) case

# MAIN
100 rangeFrom1 [fizzbuzz] map unroll


# 100 rangeFrom1,
# [
#     dup multiple15 
#     [drop 'FizzBuzz'] 
#     [
#         dup multiple5 
#         [drop 'Buzz'] 
#         [
#             dup multiple3
#             [drop 'Fizz']
#             [id] if
#         ] if
#     ] if
# ] map
# unroll

