import numpy as np
from scipy.stats import pearsonr

p_scores = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
h_scores = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

corr, p_val = pearsonr(p_scores, h_scores)

print(f'{corr:.3f}')