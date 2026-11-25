python

"""
Simple visualisation of the TONE inversion
for the matrix multiplication exponent.
"""

import numpy as np
import matplotlib.pyplot as plt

n = np.logspace(1, 4, 200)

# Classical claim
ops_classical = n ** 2.25

# TONE (inversion applied)
ops_tone = n ** 2

plt.figure(figsize=(8, 5))
plt.loglog(n, ops_classical, label=r"OpenAI claim: $n^{9/4}$", linestyle="--")
plt.loglog(n, ops_tone, label=r"TONE: $n^2$", linewidth=2)
plt.xlabel("Matrix size n")
plt.ylabel("Operations")
plt.title("Matrix Multiplication Exponent: Classical vs TONE")
plt.legend()
plt.grid(True, which="both", ls=":")
plt.tight_layout()
plt.savefig("exponent_comparison.png", dpi=150)
print("Saved exponent_comparison.png")
