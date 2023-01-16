import numpy as np

from my_python_package.operators import (
        add,
        multiply,
        )

def main():

    # test for scalars
    print(f'add(1, 3): {add(1, 3)}')
    print(f'multiply(2, 12.): {multiply(2, 12.)}')
    
    # test for arrays
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = 2. * np.ones(A.shape)
    print(f'add(A, B):\n{add(A, B)}')
    print(f'multiply(A, B):\n{multiply(A, B)}')


if __name__ == '__main__':
    main()
