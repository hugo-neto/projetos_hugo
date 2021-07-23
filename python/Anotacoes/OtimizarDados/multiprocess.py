# Fonte: http://bit.ly/multiprocess-code
from time import time
import concurrent.futures

a = time()

def funcao():
    pass

# Multiprocess
with concurrent.futures.ProcessPoolExecutor() as executor:
    results = executor.map(process_image, img_names)
 

for result in results:
    retult

b = time()

print(b-a)
