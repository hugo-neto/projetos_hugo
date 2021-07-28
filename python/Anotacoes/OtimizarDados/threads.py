
import concurrent.futures
from time import time


def do_something(var):
    x = 0
    while x < 10000000:
        x += 1
    print(f"Terminou: {var}")

a = time()

# Reliza processos de ações ao mesmo tempo
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [7, 6, 5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

with concurrent.futures.ThreadPoolExecutor(max_workers=2*os.cpu_count()) as executor:
    results = [executor.submit(funcao, i, a, b, c, ...) for i, tupla in enumerate(lista)]
    
dfResultado_ = pd.DataFrame({})
for f in as_completed(results):
    dfResultado_ = pd.concat([dfResultado, f.result()], ignore_index=True)   
 
 for result in results:
    print(results)
    
b = time()

do_something(7)
do_something(6)
do_something(5)
do_something(4)
do_something(3)
do_something(2)
do_something(1)

c = time()

print(f"Primeiro: {b-a}")
print(f"Segundo: {c-b}")
