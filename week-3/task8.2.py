def swap_first_last(array):
    if len(array) > 1:
        array[0], array[-1] = array[-1], array[0]

m = int(input("enter m: "))
A = list(map(int, input("enter elements: ").split()))

print("original array:", A)
swap_first_last(A)
print("result array:", A)
