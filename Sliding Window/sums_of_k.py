def window(arr,k):
  result=[]
  n=len(arr)
  if k>n:
    return "k is greater than the lenght of array"
  window_sum=sum(arr[:k])
  sums=window_sum
  result.append(sums)

  for i in range(k,n):
    window_sum=window_sum-arr[i-k]+arr[i]
    result.append(window_sum)
  return result

print(window([2, 1, 5, 1, 3, 2],3))
