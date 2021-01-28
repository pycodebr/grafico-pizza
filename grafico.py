import matplotlib.pyplot as plt
import numpy as np

# Valores do Gráfico #
y = np.array([35, 25, 25, 15])

# Itens do Gráfico #
mylabels = ['Maçãs', 'Bananas', 'Laranjas', 'Melancias']

# Espaço entre as "fatias" do gráfico #
myexplode = [0.2, 0, 0, 0]

# Monta o Gráfico e depois o mostra na tela #
plt.pie(y, labels=mylabels, explode=myexplode, shadow=True)
plt.show()