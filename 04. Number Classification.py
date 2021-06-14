numbers = [int(nums) for nums in input().split(", ")]

# def positive_numbers(number):
#     if number >= 0:
#         return True
#     return False
#
# def negative_numbers(number):
#     if number < 0:
#         return True
#     return False
# def odd_numbers(number):
#     if not number % 2 == 0:
#         return True
#     return False
# def even_number(number):
#     if number % 2 == 0:
#         return True
#     return False

positives = [str(positive) for positive in numbers if positive >= 0]
negative = [str(negative) for negative in numbers if negative < 0]
even = [str(even) for even in numbers if even % 2 == 0]
odd = [str(odd) for odd in numbers if odd % 2 == 1]

print(f"Positive: {', '.join(positives)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")



