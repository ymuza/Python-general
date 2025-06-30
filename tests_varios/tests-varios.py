import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh  # For solving Hermitian eigenvalue problems

# Constants (atomic units: ħ = 1, m = 1)
hbar = 1.0
m = 1.0

# Spatial domain
x_min, x_max = -5, 5
N = 1000  # Number of grid points
x = np.linspace(x_min, x_max, N)
dx = x[1] - x[0]

# Define potential: Infinite square well, harmonic oscillator, etc.
def V(x):
    # Harmonic oscillator: V(x) = 0.5 * m * ω^2 * x^2
    omega = 1.0
    return 0.5 * m * omega**2 * x**2

# Construct Hamiltonian matrix
V_diag = V(x)
kinetic = - (hbar**2) / (2 * m * dx**2)
diagonal = np.full(N, -2.0)
off_diagonal = np.full(N - 1, 1.0)

# Kinetic energy matrix (tridiagonal)
T = kinetic * (np.diag(diagonal) + np.diag(off_diagonal, 1) + np.diag(off_diagonal, -1))

# Potential energy matrix (diagonal)
V_matrix = np.diag(V_diag)

# Hamiltonian
H = T + V_matrix

# Solve eigenvalue problem
eigenvalues, eigenvectors = eigh(H)

# Plot first 4 eigenstates
plt.figure(figsize=(10, 6))
for n in range(4):
    psi = eigenvectors[:, n]
    psi = psi / np.sqrt(np.sum(psi**2) * dx)  # Normalize
    plt.plot(x, psi + eigenvalues[n], label=f'n={n}')  # Shift by energy for clarity
plt.plot(x, V(x), 'k--', label='Potential V(x)')
plt.title("Solutions to Schrödinger's Equation (Harmonic Oscillator)")
plt.xlabel('x')
plt.ylabel('ψ_n(x) + E_n')
plt.legend()
plt.grid()
plt.show()
