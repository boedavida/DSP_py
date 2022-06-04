# binary_2_numpy.py
"""Reads data from a binary file and puts the data into a numpy array"""

# Make a numpy array
import numpy as np
array = 1.0*np.array(np.arange(1_000_001))
print(array)
dt = np.dtype(array[0])
print(dt)

# Open a binary file in write mode:
outfile = open("out_binary.bin", 'wb') 
#array.tofile(outfile) # Converts to bytes and writes to binary file
array.tobytes() # Convert numpy array to bytes 
outfile.write(array) # Write to the binary file
outfile.close()

infile = open("out_binary.bin", 'rb')
#numpy.fromfile
newarray = np.array([])
while True:
    buf = infile.read(1024*1024)
    if buf:
        a = np.frombuffer(buf,dtype=dt)
        newarray = np.append(newarray, a, axis=0)
        print('.', end ='', flush = True)
    else:
        break
infile.close()
print('\n')
print(f"newarray = {newarray}")

print('\n')
print(np.shape(newarray))
print(np.size(newarray))
