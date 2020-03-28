import numpy as np
from plyfile import PlyData, PlyElement


def create_ply_file_from_np_array(np_array, fname, has_colors=False):
    if has_colors:
        serialization_data = np.array(np_array, dtype=[('x', 'f4'), ('y', 'f4'), ('z', 'f4'),
                                                       ('red', 'u1'), ('green', 'u1'), ('blue', 'u1')])
    else:
        serialization_data = np.array(np_array, dtype=[('x', 'f4'), ('y', 'f4'), ('z', 'f4')])
    el = PlyElement.describe(serialization_data, 'vertex')
    PlyData([el], text=True).write(fname)

