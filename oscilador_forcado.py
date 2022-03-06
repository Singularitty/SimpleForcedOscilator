# Importar bibliotecas
import matplotlib.pyplot as plt
import numpy as np
from math import sin

plt.rcParams.update({'font.size': 14})

# Definir funcao
# Podem alterar os valores default para verem o que acontece
def forced_oscilator(t, frequency = 1., base_force = 1., base_frequency = 1.1):
    first_term = base_force / (base_frequency**2 - frequency**2)
    return first_term * sin( (frequency*t + base_frequency*t) / 2) * sin( (base_frequency*t - frequency*t) / 2)

# Ressonancia
def forced_ressonance(t, base_force=1, base_frequency=1):
    return base_force / 2*base_frequency * t * sin(base_frequency*t)

# Definir valores para plot
time = np.arange(1,130,0.5)
position = np.vectorize(forced_oscilator)

# Realizar Plot
fig = plt.figure()
plt.title("Oscilador Forçado sem Atrito")
plt.xlabel("Tempo t")
plt.ylabel("Posição x")
plt.plot(time,position(time),color="black")
fig.savefig("freq_forcada.png",dpi=200)

# Pontos
time = np.arange(1,120,0.5)
posicao = np.vectorize(forced_ressonance)

# Plot
fig1 = plt.figure()
plt.title("Ressonância")
plt.xlabel("Tempo t")
plt.ylabel("Posição x")
plt.plot(time,posicao(time),color="black")
fig1.savefig("freq_ressonancia.png",dpi=200)

