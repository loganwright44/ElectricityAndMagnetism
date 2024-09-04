"""
By Logan Wright

Classical Mechanics Problem # 7.43
"""
import numpy as np
import matplotlib.pyplot as plt

# Define the constants
M = 1.0
m = 0.9
g = 1.0
R = 1.0
L = 0.0

#############################################################################
################################ Part B #####################################
#############################################################################
# Plot the potential as a function of φ
U = lambda φ: -g * (m * (L + R * φ) + M * R * np.cos(φ))

φ = np.linspace(-np.pi, 4 * np.pi, 10_000)

plt.plot(φ, U(φ))
plt.show()

#############################################################################
################################ Part C #####################################
#############################################################################
# Define the acceleration of φ double dot by the Lagrangian equations shown in Latex
φ_dot_dot = lambda φ: g / R * ((m - M * np.sin(φ)) / (m + M))

# Setup some constants for step size δt and initial φ0
δt = 1e-3
φ0 = 0.0

def DSolve(phi_double_dot, phi0, phi_dot0, duration, dt):
    phi = [phi0]
    phi_dot = [phi_dot0]
    t = [0.0]
    for _ in range(0, int(duration / dt)):
        phi_dot.append(phi_dot[-1] + phi_double_dot(phi[-1]) * dt)
        phi.append(phi_dot[-1] * dt)
        t.append(_ * dt)
        
    return np.array(t), np.array(phi_dot), np.array(phi)

solution = DSolve(φ_dot_dot, φ0, 10.0, 1.0, 1e-8)

print(solution[2])
plt.plot(solution[0], solution[2])
plt.show()

#############################################################################
################################ Part D #####################################
#############################################################################