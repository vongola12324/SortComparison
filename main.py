import timeit
import randnum
import bubble
import selection
import insert
import heap
import quick
import time
import platform
import sys

# Prepare
summary = open("Summary.txt", 'w')
N = [50000, 100000, 150000, 200000, 300000, 500000]
jobsLimit = 25

# Record SysInfo
summary.write("[Info]\n")
summary.write("System: " + platform.platform() + "(" + platform.system() + ")" + "\n")
summary.write("Arch: " + ("64bit" if sys.maxsize > 2 ** 32 else "32bit") + "\n")
summary.write("Computer: " + platform.node() + "\n")
summary.write("CPU: " + platform.processor() + "\n")
summary.write("Python: " + platform.python_version() + "\n")
summary.write("Run At: " + time.strftime("%Y/%m/%d %H:%M:%S") + "\n\n")

# BubbleSort
summary.write("[BubbleSort]\n")
for variable in N:
    summary.write("> " + str(variable) + " variable: \n")
    total = 0
    for job in range(jobsLimit):
        data = randnum.rand(variable)
        start = timeit.default_timer()
        bubble.sort(data)
        end = timeit.default_timer()
        summary.write(str((end-start)*1000) + "\n")
        total += (end-start)*1000
    summary.write("Avg: " + str(total/jobsLimit) + "\n\n")



# SelectionSort
summary.write("[SelectionSort]\n")
for variable in N:
    summary.write("> " + str(variable) + " variable: \n")
    total = 0
    for job in range(jobsLimit):
        data = randnum.rand(variable)
        start = timeit.default_timer()
        selection.sort(data)
        end = timeit.default_timer()
        summary.write(str((end-start)*1000) + "\n")
        total += (end-start)*1000
    summary.write("Avg: " + str(total/jobsLimit) + "\n\n")

# InsertSort
summary.write("[InsertSort]\n")
for variable in N:
    summary.write("> " + str(variable) + " variable: \n")
    total = 0
    for job in range(jobsLimit):
        data = randnum.rand(variable)
        start = timeit.default_timer()
        insert.sort(data)
        end = timeit.default_timer()
        summary.write(str((end-start)*1000) + "\n")
        total += (end-start)*1000
    summary.write("Avg: " + str(total/jobsLimit) + "\n\n")

# HeapSort
summary.write("[HeapSort]\n")
for variable in N:
    summary.write("> " + str(variable) + " variable: \n")
    total = 0
    for job in range(jobsLimit):
        data = randnum.rand(variable)
        start = timeit.default_timer()
        heap.sort(data)
        end = timeit.default_timer()
        summary.write(str((end-start)*1000) + "\n")
        total += (end-start)*1000
    summary.write("Avg: " + str(total/jobsLimit) + "\n\n")

# QuickSort
summary.write("[QuickSort]\n")
for variable in N:
    summary.write("> " + str(variable) + " variable: \n")
    total = 0
    for job in range(jobsLimit):
        data = randnum.rand(variable)
        start = timeit.default_timer()
        quick.sort(data)
        end = timeit.default_timer()
        summary.write(str((end-start)*1000) + "\n")
        total += (end-start)*1000
    summary.write("Avg: " + str(total/jobsLimit) + "\n\n")

# Build-In Sort (TimSort)
summary.write("[TimSort(Build-In)]\n")
for variable in N:
    summary.write("> " + str(variable) + " variable: \n")
    total = 0
    for job in range(jobsLimit):
        data = randnum.rand(variable)
        start = timeit.default_timer()
        data.sort()
        end = timeit.default_timer()
        summary.write(str((end-start)*1000) + "\n")
        total += (end-start)*1000
    summary.write("Avg: " + str(total/jobsLimit) + "\n\n")

# Close
summary.close()
print("Done!")