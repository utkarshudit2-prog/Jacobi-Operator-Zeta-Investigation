import numpy as np
import matplotlib.pyplot as plt

def build_jacobi_matrix(n):
    # Diagonal entries (b_n) - based on asymptotic density
    b = np.linspace(0, 100, n)
    
    # Off-diagonal entries (a_n) - your linear growth formula
    # a_n = 0.82*n + 7.0
    a = 0.82 * np.arange(1, n) + 7.0
    
    # Building the tridiagonal matrix
    J = np.diag(b) + np.diag(a, k=1) + np.diag(a, k=-1)
    return J

# Matrix size N=100
N = 100
J_N = build_jacobi_matrix(N)

# Calculating eigenvalues
eigenvalues = np.linalg.eigvalsh(J_N)

# Plotting the spectral distribution
plt.hist(eigenvalues, bins=20, color='blue', alpha=0.7)
plt.title("Spectral Distribution of Jacobi Matrix")
plt.xlabel("Eigenvalues")
plt.ylabel("Frequency")
plt.show()

# Printing the trace
print(f"Trace of the matrix: {np.trace(J_N)}")
