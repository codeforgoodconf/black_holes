
import process_fits


def is_he2(wls, fxs, threshold):
    wl_min = 4686-10
    wl_max = 4686+10
    difference = 0
    for i,wl in enumerate(wls):
        if wl_min < wl < wl_max:
            difference += fxs[i]
    return difference > threshold









