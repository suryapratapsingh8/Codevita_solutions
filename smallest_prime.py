def is_prime(num):
  if num<2:
    return False
  for i in range(2,int(num*0.5)+1):
    if num%i==0:
      return False
  return True

def find_smallest_prime(input_numbers):
  q=min(input_numbers)
  p=2
  
  while True:
    divisible=all(p%num==q for num in input_numbers if num!=q)
    if divisible and is_prime(p):
      return p
    p+=1
    
input_numbers=list(map(int,input().split()))
res=find_smallest_prime(input_numbers)
print(res)