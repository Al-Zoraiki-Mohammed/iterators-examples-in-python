"""Iterators, generators and list comprehension homework: task1 """

# -----------------------------------------------------------------------
print()
print("--" * 20 + " Question1: " + "--" * 20)
# -----------------------------------------------------------------------

"""
1. You need to implement the class MyEnumerate in such a way
that the result of passing through the loop gives the expected value.
The class constructor accepts a value as a character string.
You need to iterate over the characters and output the result like <character index> : <character>

Expected output:
    0 : a
    1 : b
    2 : c
    3 : d
    4 : f
"""


class MyEnumerate:
    """Custom implementation of enumerate."""
    def __init__(self, data: str):
        self.data = data
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.data):
            raise StopIteration
        result1 = self.idx, self.data[self.idx]
        self.idx += 1
        return result1


for index, letter in MyEnumerate('abcdf'):
    print(f'{index} : {letter}')

# -----------------------------------------------------------------------
print("--" * 20 + " Question2: " + "--" * 20)
# -----------------------------------------------------------------------
"""
2. You need to implement the classes CircleIterator and Circle in such a way
that the result of passing through the loop gives the expected value.
Circle class constructor accepts a value as a string of characters
and the number of characters in the resulting list.
You need to loop through the symbols until you reach the maximum number of symbols.

Expected output:
    ['a', 'b', 'c', 'a', 'b']
"""


class CircleIterator:
    """Custom iterator for iterating over data in a circular manner."""
    def __init__(self, data: str, max_times: int):
        self.data = data
        self.max_times = max_times
        self.length = len(self.data)
        self.idx = 0

    def __next__(self):
        if self.idx == self.length:
            self.idx = 0
        if self.max_times <= 0:
            raise StopIteration
        result2 = self.data[self.idx]
        self.idx += 1
        self.max_times -= 1
        return result2


class Circle:
    """Iterable object that iterates over data in a circular manner."""
    def __init__(self, data: str, max_times: int):
        self.data = data
        self.max_times = max_times

    def __iter__(self):
        return CircleIterator(self.data, self.max_times)


c = Circle('abc', 5)
print(list(c))

# -----------------------------------------------------------------------
print("--" * 20 + " Question3: " + "--" * 20)
# -----------------------------------------------------------------------

"""
3. You need to create a generator function that iterates over prime numbers up to the limit.
The function takes as input an integer value, up to which we will go by prime numbers.

Expected output:
    2 3 5 7
"""


def gen_primes(limit: int):
    """Generate prime numbers up to the specified limit."""
    yield 2
    yield 3
    for num in range(5, limit + 1):
        is_prime = True
        for j in range(2, int(num / 2) + 1):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            yield num


for i in gen_primes(10):
    print(i)

# -----------------------------------------------------------------------
print("--" * 20 + "Question4_1:" + "--" * 20)
# -----------------------------------------------------------------------

"""
4. You need to use the list comprehension to connect the numbers separated by commas.
(There is a better solution without list comprehension, find it.)

Expected output:
    0,1,2,3,4,5,6,7,8,9,10,11,12,13,14
"""

numbers = range(15)
RESULT = ','.join([str(i) for i in numbers])
print(RESULT)

# ------------------------------------------
print("--" * 20 + "Question4_2:" + "--" * 20)
# ------------------------------------------
RESULT = ','.join(str(i) for i in numbers)
print(RESULT)

# -----------------------------------------------------------------------
print("--" * 20 + " Question5: " + "--" * 20)
# -----------------------------------------------------------------------

"""
5. You need to use the list comprehension to take the numbers separated by
spaces from the string and sum them up.
Expected output:
    Sum: 100
"""

NUMBERS = '10 abc 20 de44 30 55fg 40'
total = sum([int(num) for num in NUMBERS.split() if num.isdigit()])
print(f'Sum: {total}')

# -----------------------------------------------------------------------
print("--" * 20 + " Question6: " + "--" * 20)
# -----------------------------------------------------------------------

"""
6. You need to use the list comprehension to swap keys and values in a dictionary.
Expected output:
    {1: 'a', 2: 'b', 3: 'c'}
"""

d = {'a': 1, 'b': 2, 'c': 3}
flipped_d = {value: key for key, value in d.items()}
print(flipped_d)

# -----------------------------------------------------------------------
print("----" * 23)
# -----------------------------------------------------------------------
