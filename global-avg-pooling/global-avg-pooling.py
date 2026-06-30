import numpy as np

def global_avg_pool(x):
    """
    Compute global average pooling over spatial dims.
    Supports (C,H,W) => (C,) and (N,C,H,W) => (N,C).
    """
    # Write code here
    if x.ndim < 3:
        raise ValueError("Supports (N,C,H,W) and (C,H,W)")
    return x.mean(axis=(-2, -1))