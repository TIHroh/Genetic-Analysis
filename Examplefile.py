install setup.py 
import numpy as np

mu, sigma = 150, 1
s = np.random.normal(mu, sigma, 100)
s= ['%.2f'% elem for elem in s]

for i in range(1,11):
  print("April", str(i)+",","2015"+",", s[i])
  
