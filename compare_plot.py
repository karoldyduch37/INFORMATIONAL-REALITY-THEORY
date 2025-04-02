import matplotlib.pyplot as plt
from tri_model import tri_velocity

# Obserwacyjne dane SPARC (NGC 3198)
r_obs = [0.48, 1.44, 2.40, 3.36, 4.32, 5.28, 6.24, 7.20, 8.16, 9.12,
         10.08, 11.04, 12.00, 12.96, 13.92, 14.88, 15.84, 16.80,
         17.76, 18.72, 19.68, 20.64, 21.60, 22.56, 23.52, 24.48,
         25.44, 26.40, 27.36, 28.32, 29.28, 30.24, 31.20, 32.16,
         33.12, 34.08, 35.04, 36.00, 36.96, 37.92, 38.88, 39.84,
         40.80, 41.76, 42.72]

v_obs = [25.6, 44.3, 63.3, 79.7, 94.4, 106.9, 118.3, 128.1, 136.2, 142.6,
         147.9, 152.1, 155.5, 157.9, 158.8, 158.4, 157.3, 155.7, 154.2,
         153.0, 152.1, 151.4, 150.9, 150.6, 150.4, 150.4, 150.4, 150.5,
         150.6, 150.8, 151.0, 151.2, 151.4, 151.6, 151.8, 152.0, 152.2,
         152.3, 152.5, 152.6, 152.8, 152.9, 153.0, 153.1, 153.2]

# Model TRI
v_tri = [tri_velocity(r) for r in r_obs]

# Wykres
plt.figure(figsize=(10, 6))
plt.plot(r_obs, v_obs, 'o-', label='SPARC – obserwacja')
plt.plot(r_obs, v_tri, 'r--', label='TRI – model')
plt.title('NGC 3198: porównanie TRI vs SPARC')
plt.xlabel('Promień (kpc)')
plt.ylabel('Prędkość rotacji (km/s)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
