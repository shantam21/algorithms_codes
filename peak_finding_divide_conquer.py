# for monotonically inceeasing then decreasing sequence of arrays

arr = [-1, -3, 7, 20, 4, 1, 0]

def find_peak(arr):
    """Finds peak for a monotonicaly increasing then decreasing function

    Arguments:
        arr {[array]} -- Array of sequence

    Returns:
        [int]/[float] -- peak for the sequence
    """    
    # print(arr)
    mid = int(len(arr)/2)
    # print("mid is ", mid)
    if mid == 1 and len(arr) == 2:
        return arr[mid]
    else:
        if arr[mid] <= arr[mid+1]:
            # print("case1")
            return find_peak(arr[mid:])
        elif arr[mid] <= arr[mid - 1]:
            # print("case 2")
            return find_peak(arr[:mid])
        else:
            return arr[mid]



print("-----------------------------------")
print("The peak for the sequence is : ", find_peak(arr) )
print("-----------------------------------")


