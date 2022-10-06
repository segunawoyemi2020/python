def find_max(numbers):
    max =numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

flst = list(range(1, 101))
is_even = lambda num : num % 2 == 0
print(list(filter(is_even, flst)))
map
