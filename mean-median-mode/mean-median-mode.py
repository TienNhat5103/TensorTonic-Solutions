import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    mean = np.mean(x)
    median = np.median(x)
    freq = Counter(x)
    max_frequent = max(freq.values())
    max_freq_key = [num for num in x if freq[num] == max_frequent]
    mode = min(max_freq_key)
    return (float(mean), float(median), float(mode))