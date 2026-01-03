class Animal:
    def __init__(self,especie):
        self._especie = especie

    @property
    def mostrar_especie(self):
        return self._especie


g = Animal('Cachorro')
print(g.mostrar_especie)