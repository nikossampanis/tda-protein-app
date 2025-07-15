import numpy as np

def extract_coordinates(pdb_file):
    coords = []
    for line in pdb_file:
        if line.startswith("ATOM"):
            try:
                x = float(line[30:38].strip())
                y = float(line[38:46].strip())
                z = float(line[46:54].strip())
                coords.append([x, y, z])
            except:
                continue
    return np.array(coords)
