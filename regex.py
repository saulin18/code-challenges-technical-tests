# Write a simple regex to validate a username. Allowed characters are:
#
# lowercase letters,
# numbers,
# underscore
# Length should be between 4 and 16 characters (both included).

import re


def validate_usr(username: str):
    # a-z\d_
    is_valid_regex = re.fullmatch("[a-z0-9_]{4,16}", username)
    is_valid_regex.__bool__

    return is_valid_regex


# Description:
# Your task is simply to count the total number of lowercase letters in a string.
#
# Examples
# "abc" ===> 3
#
# "abcABC123" ===> 3
#
# "abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 3
#
# "" ===> 0;
#
# "ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 0
#
# "abcdefghijklmnopqrstuvwxyz" ===> 26


def lowercase_count(strng: str):
    # re.findall(r"[^A-Z0-9\s\W]", texto)  # Negar mayúsculas, dígitos, espacios y no-word
    return len(re.findall("[a-z]", strng))


# Regex validate PIN code
# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
#
# If the function is passed a valid PIN string, return true, else return false.
#
# Examples (Input --> Output)
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false


def validate_pin(pin: str):
    return re.fullmatch("[0-9]{4}|[0-9]{6}", pin)


# Your function should return a valid regular expression. This is a pattern which is normally used to match parts of a string.
# In this case will be used to check if all the characters given in the input appear in a string.
# Input
# Non empty string of unique alphabet characters upper and lower case.
# Output
# Regular expression pattern string.
# Examples
# Your function should return a string.
## Function example
# def regex_contains_all(st):
#  return r"abc"
# That regex pattern will be tested like this.
#
## Test
# abc = 'abc'
# pattern = regex_contains_all(abc)
# st = 'zzzaaacccbbbzzz'
# bool(re.match(pattern, st), f"Testing if {st} contains all characters in {abc} with your pattern {pattern}") -> True
# Regular ExpressionsFundamentalsStrings
import re


def regex_contains_all(st: str):
    patterns = []
    for char in st:
        escaped_char = re.escape(char)
        patterns.append(f"(?=.*{escaped_char})")

    pattern = "".join(patterns) + ".*"
    return pattern


# You are given a positive natural number n (which is n > 0) and you should create a regular expression pattern which only matches
# the decimal representation of all positive natural numbers strictly less than n without leading zeros. The empty string, numbers with
# leading zeros, negative numbers and non-numbers should not match the regular expression compiled from your returned pattern.
#
# Input
# n > 0 natural number, n can be from the full possible positive range
# Output
# regular expression pattern as string which will be used to compile a regular expression to do the matches
# Tests
# The compiled regular expression will be tested against decimal representations of random numbers with and without leading zeros,
# strings including letters and the empty string and should only match for decimal representations of numbers k with 0 < k < n.
#
# Tests use re.match() to do the matches.


def regex_below(n: int):
    if n <= 1:
        return "(?!.)"  # Patrón que nunca coincide

    digits = []
    temp = n
    while temp > 0:
        last_digit = temp % 10
        digits.insert(0, last_digit)
        temp //= 10

    patterns = []

    # FASE 1: Grupos completos (solo con MENOS dígitos que n)
    counter = 10
    digit_count = 1
    num_digits = len(digits)

    while counter < n and digit_count < num_digits:
        if digit_count == 1:
            pattern_str = "[1-9]"
        else:
            pattern_str = "[1-9]" + "[0-9]" * (digit_count - 1)
        patterns.append(pattern_str + "$")  # ✅ Agregar $ al final
        digit_count += 1
        counter *= 10

    # FASE 2: Grupo parcial (números con la misma cantidad de dígitos que n)
    if len(digits) > 0:
        first_digit = digits[0]

        # 1. Grupos completos dentro del grupo parcial
        if first_digit > 1:
            for i in range(1, first_digit):
                pattern_str = str(i) + "[0-9]" * (num_digits - 1)
                patterns.append(pattern_str + "$")  # ✅ Agregar $ al final

        # 2. Grupo parcial empezando con first_digit
        current_prefix = str(first_digit)

        for i in range(1, len(digits)):
            current_digit = digits[i]

            if i == len(digits) - 1:
                # Último dígito
                if current_digit > 0:
                    if current_digit == 1:
                        patterns.append(
                            current_prefix + "[0]$"
                        )  # ✅ Agregar $ al final
                    else:
                        patterns.append(current_prefix + f"[0-{current_digit - 1}]$")
            else:
                for j in range(current_digit):
                    remaining = num_digits - len(current_prefix) - 1
                    patterns.append(current_prefix + str(j) + "[0-9]" * remaining + "$")

                current_prefix += str(current_digit)

    return "|".join(patterns)


regex_below(234)

# 57. Word Starts & Ends with Vowel
#
# Write a Python program that checks whether a word starts and ends with a vowel in a given string. Return true if a word matches 
# the condition; otherwise, return false.
#
# Sample Data:
# ("Red Orange White") -> True
# ("Red White Black") -> False
# ("abcd dkise eosksu") -> True

def starts_and_end_with_a_vowel(string: str) -> bool:
    regex = re.compile(r"\b[aeiouAEIOU]\w*[aeiouAEIOU]\b")
    return bool(re.search(regex, string))