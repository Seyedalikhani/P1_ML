
import matplotlib.pyplot as plt
import numpy as np
import random

# In numpy arrays can be multi dimentional
a=np.array([[1,2],[3,4]]);

# In numpy matrixes are only two dimentional
b=np.matrix([[1,2],[3,4]]);

# Due to memory management it is better to slect dtaa type (int8, int16, int32, int64, Boolean, float, complex)
b1=np.matrix([[1,2],[3,4]],dtype='int8');

print(b1)

# Matrix Multiply
print("--------Matrix Multiply----------")
print(a@b)
print(np.dot(a,b))


# Multiply one by one element
print("--------Multiply one by one element----------")
print(np.multiply(a,b))

# Multiply In Matrix and In Array
print("--------Multiply In Array and In Matrix----------")
print(a*a)
print(b*b)
print(a*b)  # In Array * Matrix (results are same as Matrix * Matrix)



# Multiply the elements together
print("--------Multiply the elements together----------")
print(np.prod(a))

# Broadcasting
print("--------Broadcasting----------")
c=np.array([[1,2,3]]);
print(c+5)

d=np.ones((3,3))   # Tuple
print(d)
print(c+d)

e=np.ones((3,1));
f=np.array([5,6,7]);
print(e+f)


# Summation of elements
print("--------Summation of elements----------")
print(np.sum(a))
print(np.cumsum(a,axis=0))  # cumsum on rows
print(np.cumsum(a,axis=1))  # cumsum on columns


# Subtraction of elements
print("--------Subtraction of elements----------")
print(np.subtract(a,np.ones((2,2))))

# Division
print("--------Division----------")
print(np.divide([5,6,7],3))
print(np.floor_divide([5,6,7],3))


# math library
print("--------math library----------")
print(np.math.sqrt(5))
print(np.math.nan)    # null
print(np.math.inf)    # infinite

# distribution
print(np.random.uniform(1,5,(2,3)))   # uniform distribution matrix with size of 2*3 between 1 and 5
print(np.random.standard_normal((2,3)))   # nomal distribution matrix with size of 2*3 between -1 and 1


print