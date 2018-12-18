# Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

# For example:

# next_smaller(21) == 12
# next_smaller(531) == 513
# next_smaller(2071) == 2017
# Return -1 (for Haskell: return Nothing), when there is no smaller number that contains the same digits. Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.

# next_smaller(9) == -1
# next_smaller(135) == -1
# next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
# some tests will include very large numbers.
# test data only employs positive integers.
#

# def next_smaller(n):
#     numbers = [int(x) for x in list(str(n))]
#     # find pivot
#     i = len(numbers) - 2
#     while i >= 0:
#         if numbers[i] > numbers[i + 1]:
#             break
#         else:
#             i = i - 1

#     if i == -1:
#         return -1

#     j = len(numbers) - 1
#     while j >= i:
#         if numbers[j] < numbers[i]:
#             break
#         else:
#             j = j - 1

#     left = numbers[:i]
#     # remove substitute of pivot
#     right = numbers[i:j] + numbers[j + 1:]
#     right = sorted(right, reverse=True)
#     # combine left + substitute of pivot + sorted right
#     return int("".join([str(x) for x in left + [numbers[j]] + right]))


def next_smaller(n):
    s = list(str(n))
    i = j = len(s) - 1
    while i > 0 and s[i - 1] <= s[i]:
        i -= 1
    if i <= 0: return -1
    while s[j] >= s[i - 1]:
        j -= 1
    s[i - 1], s[j] = s[j], s[i - 1]
    s[i:] = reversed(s[i:])
    if s[0] == '0': return -1
    return int(''.join(s))


class Test(object):
    @staticmethod
    def it(value):
        print(value)

    @staticmethod
    def assert_equals(a, b):
        if a != b:
            print("test case fail ", "expect: ", b, " real: ", a)


Test.it("Smaller numbers")
Test.assert_equals(next_smaller(127), -1)
Test.assert_equals(next_smaller(2071), 2017)
Test.assert_equals(next_smaller(414), 144)
Test.assert_equals(next_smaller(123456798), 123456789)
Test.assert_equals(next_smaller(123456789), -1)
Test.assert_equals(next_smaller(1234567908), 1234567890)
