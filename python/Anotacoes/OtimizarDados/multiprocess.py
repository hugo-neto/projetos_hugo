# Fonte: http://bit.ly/multiprocess-code
from time import time
import concurrent.futures

a = time()

def funcao():
    pass

# Multiprocess
with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_image, img_names)

b = time()

print(b-a)
