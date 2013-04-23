'''
  RSA Generator
  @author: Deepanshu Mehndiratta
  @url: http://www.deepanshumehndiratta.com
'''

from __future__ import print_function
import math

bits = 20 # Specify the number of bits

s = [0]*(bits+1) # The array of s values
s[0] = 75634
p = 103
q = 211
N = p*q
fi = (p-1)*(q-1)
b = 2717 # Choosing a b such that G.C.D(b,fi) = 1

b1 = b%2
p = (b-b1)/2

for i in range(0,bits):
  #print "S" + str(i) + " = " + str(s[i])
  print(s[i]%2, end="")
  temp = 1
  t1 = (s[i]**2)%N
  for j in range(0,p):
    temp = ((temp*t1)%N)
  if b1 == 1:
    s[i+1] = ((temp*s[i])%N)
  else:
    s[i+1] = temp

#print "S" + str(bits) + " = " + str(s[bits])
print(s[bits]%2)
