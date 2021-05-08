

#Si hay argumentos tratar de usar Lista
def Potencia(Num, Base=2):
    if Base:
        Resultado = Num
        for a in range(1, Base):
            Resultado = Resultado * Num
        return Resultado



print(Potencia(5))
print(Potencia(5,3))
