# A format for expressing an ordered list of integers is to use a comma separated list of either


# individual integers
# or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example ("12, 13, 15-17")
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.
def solution(args):
    result = ""
    index = 0
    while index < len(args) - 2:
        flag = False
        start = args[index]
        current = args[index]
        end = args[index + 1]
        while current - end == -1 and index < len(args) - 2:
            flag = True
            index += 1
            current = args[index]
            end = args[index + 1]
        if flag:
            result = result + str(start) + "-" + str(current) + ","
        else:
            result = result + str(start) + ","
        index += 1
    return result[:-1]


from test import Test
Test.assert_equal(
    solution([
        -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20
    ]), '-6,-3-1,3-5,7-11,14,15,17-20')
Test.assert_equal(
    solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]),
    '-3--1,2,10,15,16,18-20')
