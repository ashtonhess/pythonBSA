import time

def doBSA(filename, number):
    return 0

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

