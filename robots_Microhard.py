l, n = int(input()), int(input())
arr = [int(i) for i in input().split()]
arr.sort()
print(max(l - arr[0], arr[n - 1]))
