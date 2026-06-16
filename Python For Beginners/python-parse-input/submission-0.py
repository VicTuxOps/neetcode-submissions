from typing import List

def read_integers() -> List[int]:
    myInput = input()
    return [int(x) for x in myInput.split(",")]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
