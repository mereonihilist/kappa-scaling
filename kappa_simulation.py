# kappa_simulation.py

import numpy as np
import matplotlib.pyplot as plt

kappa = np.linspace(0.5, 1.5, 21)
fidelity = 0.98 * (0.25) / ((kappa - 1)**2 + 0.25)
concurrence = 1 - 0.3 * (kappa - 1)**2
visibility = np.exp(-6.25 * (kappa - 1)**2)

np.savetxt('data/raw_fidelity_data.csv', np.column_stack((kappa, fidelity)), delimiter=',', header='kappa,fidelity', comments='')
np.savetxt('data/raw_concurrence_data.csv', np.column_stack((kappa, concurrence)), delimiter=',', header='kappa,concurrence', comments='')
np.savetxt('data/raw_visibility_data.csv', np.column_stack((kappa, visibility)), delimiter=',', header='kappa,visibility', comments='')
