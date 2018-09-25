# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
#
# Example:
#
# n = 15,
#
# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]


class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        returnArray = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                returnArray.append("FizzBuzz")
            elif i % 3 == 0:
                returnArray.append("Fizz")
            elif i % 5 == 0:
                returnArray.append("Buzz")
            else:
                returnArray.append(str(i))
        return returnArray
