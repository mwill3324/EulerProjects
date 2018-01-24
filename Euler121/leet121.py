def maxProfit(prices):
    plen = len(prices)
    if plen < 2 :
        return 0
    theprices = [ prices[x + 1] - prices[x] for x in range(len(prices)-1)]
    a = 0
    summ = theprices[a]
    minn = min(theprices[a], a)
    maxx = max(theprices[a], a)
    for i in range(1, len(theprices)):
        summ = summ + theprices[i]
        maxx = max(maxx, summ-minn)
        minn = min(minn, summ)
    return maxx
import sys
from collections import namedtuple
TestCase = namedtuple("TestCase", "prices exp_out")

def main():
    testcases = read_stdin()
    for tc in range(0, len(testcases)):
        perform_test(tc + 1, testcases[tc])

def perform_test(tc, testcase):
    print("Running test case", tc)
    result =  round(maxProfit(testcase.prices),2) # -- Note: here is where maxProfit() is called
    print("Expected/actual result = %s / %s\nTest case " % (testcase.exp_out, result), end="")
    if result == testcase.exp_out:
        print("passed\n")
    else:
        print("FAILED\n")
def read_stdin():
    testcases = list()
    for line in sys.stdin:
        numbers = [float(s) for s in line.strip().split()]
        testcases.append(TestCase(prices = numbers[1:len(numbers)], exp_out = numbers[0]))
    return testcases
main()
