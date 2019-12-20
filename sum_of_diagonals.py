import numpy as np
m = np.arange(40).reshape(5,8)
print("Original matrix:")
print(m)
result =  np.trace(m)
print("Condition number of the said matrix:")
print(result)
