
def insertion_sort_increase(A):
    for j in range(1,len(A)):
        key = A[j]
        # insert A[j] into the sorted seq A[1 ... j-1]
        i = j-1
        while i >= 0 and A[i]>key: # important for increase ( if i+1 is smaller than i = swap it)
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key

    return A

def insertion_sort_deincrease(A):
    for j in range(1,len(A)):
        key = A[j]
        # insert A[j] into the sorted seq A[1 ... j-1]
        i = j-1
        while i >= 0 and A[i]<key: # important for increase ( if i+1 is bigger than i = swap it)
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key

    return A


A = [5,2,4,6,1,3]
A = [31,41,59,26,41,58]
print(A)
result_increase = insertion_sort_increase(A)
print(result_increase)

result_deincrease = insertion_sort_deincrease(A)
print(result_deincrease)