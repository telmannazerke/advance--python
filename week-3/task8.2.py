def swap_first_last(arr):
    if len(arr) > 1:
        arr[0], arr[-1] = arr[-1], arr[0]


m = int(input("Enter m: "))
A = list(map(int, input("Enter elements: ").split()))

print("Original array:", A)

swap_first_last(A)

print("Result array:", A)
