import randnum
import time
import bubble
import insert
import heap
import quick

# Prepare
# summary = open("Summary.txt", 'w')
# report = open("Report.txt", 'w')
# N = [50000, 100000, 150000, 200000, 300000, 500000]
N = [1000, 2000, 3000, 4000, 5000]
jobsLimit = 25
currentTime = lambda: int(round(time.time() * 1000))

# BubbleSort
# print("In BubbleSort:")
# for variable in N:
#     print("In " + str(variable) + " variable: ")
#     for jobs in range(jobsLimit):
#         data = randnum.rand(variable)
#         start = currentTime()
#         bubble.sort(data)
#         end = currentTime()
#         print(str(end-start) + " ms")

# InsertSort
# print("In InsertSort:")
# for variable in N:
#     print("In " + str(variable) + " variable: ")
#     for jobs in range(jobsLimit):
#         data = randnum.rand(variable)
#         start = currentTime()
#         insert.sort(data)
#         end = currentTime()
#         print(str(end-start) + " ms")

# HeapSort