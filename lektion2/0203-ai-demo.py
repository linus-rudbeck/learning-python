import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Exempeldata: storleken på hus (i kvadratmeter) och priset (i tusen kronor)
storlek = np.array([50, 60, 80, 100, 120, 150, 200]).reshape(-1, 1)  # Storlek på hus
pris = np.array([200, 250, 300, 350, 400, 500, 600])  # Pris på hus

# Skapa och träna en linjär regressionsmodell
modell = LinearRegression()
modell.fit(storlek, pris)

# Förutsäg priset för ett hus på 90 kvm
forutsagt_pris = modell.predict([[90]])
print(f"Förutsagt pris för ett hus på 90 kvm: {forutsagt_pris[0]:.2f} tusen kronor")

# Visualisera resultatet
plt.scatter(storlek, pris, color='blue')  # Data som punkter
plt.plot(storlek, modell.predict(storlek), color='red')  # Linjen som modellen lär sig
plt.xlabel("Storlek på hus (kvm)")
plt.ylabel("Pris på hus (tusen kronor)")
plt.title("Linjär regression: Huspris beroende på storlek")
plt.show()
