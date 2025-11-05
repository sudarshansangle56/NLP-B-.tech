import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Define feature universe (0 to 10)
x = np.arange(0, 11, 1)

# Define fuzzy sets for Roundness
round_low = fuzz.trimf(x, [0, 0, 5])
round_medium = fuzz.trimf(x, [2, 5, 8])
round_high = fuzz.trimf(x, [5, 10, 10])

# Visualize
plt.figure()
plt.title("Fuzzy Set for Roundness (Shape Matching)")
plt.plot(x, round_low, 'b', label='Low Roundness')
plt.plot(x, round_medium, 'g', label='Medium Roundness')
plt.plot(x, round_high, 'r', label='High Roundness')
plt.xlabel('Roundness Feature Value')
plt.ylabel('Membership Degree')
plt.legend()
plt.show()
