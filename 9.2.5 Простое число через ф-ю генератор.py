# put your python code here
# def is_prime_number():
#     num = 2
#     while True:
#         count = 0
#         for i in range(2, num//2 +1):
#             if num % i == 0:
#                 count = 1

#         if count == 0:
#             yield num
#         num += 1

def is_prime_number():
    num = 2
    while True:
        for i in range(2, num//2 + 1):
            if num % i == 0:
                break
        else:
            yield num
        num +=1
        

prime_list = is_prime_number()
for i in range(20):
    print(next(prime_list), end = ' ')
