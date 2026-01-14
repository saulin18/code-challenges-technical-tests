from collections import defaultdict
from itertools import chain, groupby
import itertools
from itertools import compress
from itertools import product
from itertools import accumulate
from itertools import dropwhile
from itertools import batched
from itertools import filterfalse
from itertools import cycle
from itertools import takewhile
from operator import mul
from typing import Dict, List
from unittest import result
from typing_extensions import Any

# 1. Iterator from Iterables
#
# Write a Python program to create an iterator from several iterables in a
# sequence and display the type and elements of the new iterator.


def iterator_from_iterables(iterables):
    result = chain.from_iterable(iterables)
    print(list(result))
    return result


print(iterator_from_iterables([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def running_product_of_a_iterable(iterable):
    product_cartesian = itertools.product(iterable)
    return product_cartesian


def product_of_a_iterable(iterable):
    product_accumulate = accumulate(iterable, mul)
    return product_accumulate


print(list(running_product_of_a_iterable([1, 2, 3, 4, 5])))
print(list(product_of_a_iterable([1, 2, 3, 4, 5])))

# 3. Max & Min from Iterable
#
# Write a Python program to generate the maximum and minimum values of the elements of an iterable.


def max_and_min_from_iterable(iterable):
    max_value = max(iterable)
    min_value = min(iterable)

    max_dropwhile = dropwhile(lambda x: x < max_value, iterable)
    min_takewhile = takewhile(lambda x: x > min_value, iterable)

    return max_dropwhile, min_takewhile


print(list(max_and_min_from_iterable([1, 2, 3, 4, 5])))

# 4. Infinite Iterator with Step
#
# Write a Python program to construct an infinite iterator that returns evenly spaced values starting with a specified number and step.


def infinite_iterator_with_step(start, step):
    iterator = itertools.count(start, step)

    first_three = [next(iterator), next(iterator), next(iterator)]

    return first_three


print(infinite_iterator_with_step(1, 2))


def infinite_iterator_with_cycle(iterable):
    iterator = cycle(iterable)
    first_six = [
        next(iterator),
        next(iterator),
        next(iterator),
        next(iterator),
        next(iterator),
        next(iterator),
    ]
    return first_six


print(infinite_iterator_with_cycle([1, 2, 3]))


def drop_positives(iterable):
    elements_dropped = dropwhile(lambda x: x > 0, iterable)
    return elements_dropped


def drop_negatives(iterable):
    elements_dropped = dropwhile(lambda x: x < 0, iterable)
    return elements_dropped


def group_elements(iterable):
    elements_grouped = groupby(iterable, key=lambda x: x)
    for key, group in elements_grouped:
        print(key, list(group))
    return elements_grouped


print(group_elements([1, 2, 3, 4, 5]))

# 5. Group Elements by Common Property
#
# Write a Python program to iterate over an iterable, grouping consecutive
# elements that share a common property, and output the key with its group as a list.


def group_elements_by_common_property(
    iterable: List[Dict[Any, Any]],
    key: Any,
) -> Dict[Any, List[Any]]:
    result = defaultdict(list)
    group = groupby(sorted(iterable, key=lambda x: x[key]), key=lambda x: x[key])
    for key_in_group, group_in_group in group:
        result[key_in_group].extend(list(group_in_group))
    return dict(result)


def iterables_from_iterable(iterable):
    res = batched(iterable, 2)

    return res


print(list(iterables_from_iterable([1, 2, 3, 4, 5, 6])))

# 19. FizzBuzz with Itertools
#
# Write a Python program that iterates the integers from 1 to a given number and prints "Fizz" for multiples of three,
# prints "Buzz" for multiples of five, and prints "FizzBuzz" for multiples of both three and five using the itertools module.


def fizzbuz_with_itertools(iterable):
    def is_divisible_by_3(number):
        return number % 3 == 0

    def is_divisible_by_5(number):
        return number % 5 == 0

    taked_numbers = list(iterable)

    string_to_print = ""
    for num in taked_numbers:
        if is_divisible_by_3(num):
            string_to_print += "Fizz"
        if is_divisible_by_5(num):
            string_to_print += "Buzz"
        if string_to_print == "":
            string_to_print = str(num)
        print(string_to_print)
        string_to_print = ""


print(fizzbuz_with_itertools(range(1, 16)))
