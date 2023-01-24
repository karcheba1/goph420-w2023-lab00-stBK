import numpy as np

from fem_1d_heat.element import (
        global_to_local,
        shape,
        )


def main():
    print('successfully imported fem_1d_heat')

    z = 3.
    z_e = np.array([0, 6])
    print(f'testing global_to_local({z}, {z_e}): {global_to_local(z, z_e)}')

    z = 2.
    z_e = np.array([1, 4])
    print(f'testing global_to_local({z}, {z_e}): {global_to_local(z, z_e)}')

    s = 0.9
    print(f'testing shape({s}): {shape(s)}')


if __name__ == '__main__':
    main()
