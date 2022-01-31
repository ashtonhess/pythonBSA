import time
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12.0, 9.0)

algo_times = []
all_times = []

def doBSA(filename, number):
    all_timeStart = time.time()
    dataFile = open(filename, 'r')

    dataContent = dataFile.read()
    # print(dataContent)
    dataContentList = dataContent.split(" ")
    dataFile.close()
    # print(dataContentList)

    algo_timeStart = time.time()
    result = algBSA(dataContentList, number, 0, len(dataContentList) - 1)
    algo_times.append(time.time() - algo_timeStart)
    print("algo_time (printed): %s seconds" % (time.time() - algo_timeStart))
    #print is approximate because it is calculated again. Times stored in array and graphed are more accurate than this print right now.

    if result != -1:
        print("Element is at index: " + str(result))
    else:
        print("Element was not found.")

    return (time.time() - all_timeStart)

#Helper function to directly implement BSA alg.
#Split this off from the doBSA so alg. implementation is in a focused func.
def algBSA(array, number, lowPtr, highPtr):
    if highPtr >= lowPtr:
        midPtr = lowPtr+(highPtr-lowPtr)//2
        # // -> floor division
        if int(array[midPtr]) == number:
            return midPtr
        elif int(array[midPtr]) > number:
            return algBSA(array, number, lowPtr, midPtr-1)
        else:
            return algBSA(array, number, midPtr+1, highPtr)
    else:
        return -1

def fillAllTimes():
    all_times.append(doBSA("data1.txt", 19))
    all_times.append(doBSA("data1.txt", 225))
    all_times.append(doBSA("data1.txt", 705))
    all_times.append(doBSA("data2.txt", 128))
    all_times.append(doBSA("data2.txt", 5756))
    all_times.append(doBSA("data2.txt", 9982))
    all_times.append(doBSA("data3.txt", 1997))
    all_times.append(doBSA("data3.txt", 20680))
    all_times.append(doBSA("data3.txt", 23887))
    all_times.append(doBSA("data4.txt", 68189))
    all_times.append(doBSA("data4.txt", 921111))
    all_times.append(doBSA("data4.txt", 935099))
    return

print("\t\t__________data1.txt__________")
print("\n")
print("all_time: " + str(doBSA("data1.txt", 19)))
print("\n")
print("all_time: " + str(doBSA("data1.txt", 225)))
print("\n")
print("all_time: " + str(doBSA("data1.txt", 705)))

print("\n\n")

print("\t\t__________data2.txt__________")
print("\n")
print("all_time: " + str(doBSA("data2.txt", 128)))
print("\n")
print("all_time: " + str(doBSA("data2.txt", 5756)))
print("\n")
print("all_time: " + str(doBSA("data2.txt", 9982)))

print("\n\n")

print("\t\t__________data3.txt__________")
print("\n")
print("all_time: " + str(doBSA("data3.txt", 1997)))
print("\n")
print("all_time: " + str(doBSA("data3.txt", 20680)))
print("\n")
print("all_time: " + str(doBSA("data3.txt", 23887)))

print("\n\n")

print("\t\t__________data4.txt__________")
print("\n")
print("all_time: " + str(doBSA("data4.txt", 68189)))
print("\n")
print("all_time: " + str(doBSA("data4.txt", 921111)))
print("\n")
print("all_time: " + str(doBSA("data4.txt", 935099)))

print("\n\n")

X = [2,2,2,3,3,3,4,4,4,5,5,5]

print(algo_times)
plt.scatter(X, algo_times)
plt.show()

print("\n\n\n")

fillAllTimes()
print(all_times)

algo_timesMean = np.mean(algo_times)
all_timesMean = np.mean(all_times)


