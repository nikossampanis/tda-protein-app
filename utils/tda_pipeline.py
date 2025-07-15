from ripser import ripser

def compute_persistence(coords):
    result = ripser(coords, maxdim=2)
    return result['dgms']
