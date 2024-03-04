def print_positive_numbers(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    if positive_numbers:
        print("Output:", ", ".join(map(str, positive_numbers)))
    else:
        print("Output: No positive numbers found")



list1 = [12, -7, 5, 64, -14]
print("Input:", list1)
print_positive_numbers(list1)

list2 = [12, 14, -95, 3]
print("\nInput:", list2)
print_positive_numbers(list2)
