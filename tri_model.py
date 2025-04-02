import math

def tri_velocity(r, alpha=124, r_scale=2.8, offset=25):
    # TRI model calibrated for NGC 3198 (3rd calibration)
    return offset + alpha * (1 - math.exp(-r / r_scale))
