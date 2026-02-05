# Write a function that takes an integer as input, and returns the number of bits that are equal to one
# in the binary representation of that number. You can guarantee that input is non-negative.
#
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
#
# BitsAlgorithms
def count_bits(n):
    def integer_to_binary(num: int) -> str:
        """
        Get the binary representation of a number.
        :param num: Number for getting the binary representation
        :type num: int
        :return: The binary representation of the number in digits (0, 1)
        :rtype: int
        """
        if num == 0:
            return 0

        digits = []
        res = []

        while num > 0:
            digits.append(num % 2)
            num //= 2

        for index in range(len(digits) - 1, 0, -1):
            res.append(str(digits[index]))

        return "".join(str(num) for num in digits)

    return integer_to_binary(n).count("1")


print(count_bits(1234))
