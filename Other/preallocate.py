import time


def doAppend(size=1000):
    result = []
    for i in range(size):
        message = 10
        result.append(message)
    return result


def doAllocate(size=1000):
    result = size*[None]
    for i in range(size):
        message = 10
        result[i] = message
    return result


##############################################################################
# Test and Debug
##############################################################################
if __name__ == '__main__':

    size = 100000000

    start = time.time()
    doAppend(size)
    end = time.time()
    timeAppend = end - start

    start = time.time()
    doAllocate(size)
    end = time.time()
    timeAllocate = end - start

    print((timeAppend, timeAllocate))
