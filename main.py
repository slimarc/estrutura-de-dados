from datetime import date

class Pessoa:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def dias_vividos(self):
        return (date.today() - self.data_nascimento).days

p1 = Pessoa('Ricardo', date(1999, 6, 14))
print("A quantidade de dias vividos foram: ", p1.dias_vividos())