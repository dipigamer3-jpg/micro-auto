class auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.habilitados = []
        self.no_habilitados = []

    def getInfo(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Año:", self.año)

    def getConductores(self):
        if self.habilitados:
            print("Conductores habilitados del auto:")
            for i in self.habilitados:
                print("-", i)
        else:
            print("No hay conductores habilitados registrados para este auto.")
        if self.no_habilitados:
            print("Conductores no habilitados del auto:")
            for i in self.no_habilitados:
                print("-", i)

    def setConductor(self, conductor):
        self.habilitados.append(conductor)

    def setNohabilitado(self, noconductor):
        self.no_habilitados.append(noconductor)