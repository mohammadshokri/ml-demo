import numpy as np
from sklearn.datasets import load_digits
print('*'*20)
data, labels = load_digits(return_X_y=True)
print(data)
# print(data[1][1])

print(labels)
print(labels[4])
(n_samples, n_features), n_digits = data.shape, np.unique(labels).size

# print(f"# digits: {n_digits}; # samples: {n_samples}; # features {n_features}")