# Time: O(n + k) where k is the range of data

# Note - This can be written with negative arrays, but we'll stick to positive arrays,
# so k is the max of the array

# Space: O(k)

def counting_sort(arr):
  maxx = max(arr)
  counts = [0] * (maxx + 1)

  for x in arr:
    counts[x] += 1

  i = 0
  for c in range(maxx + 1):
    while counts[c] > 0:
      arr[i] = c
      i += 1
      counts[c] -= 1

F = []
n=int(input(": "))
for i in range(n):
  F.append(int(input()))
  
counting_sort(F)
print(F)