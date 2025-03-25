import math
class temperatura:
    def __init__(self,celsius):
        self.celsius=celsius
    def converter_fahrenheit(self):
        fahrenheit=(self.celsius*1.8)+32
        return fahrenheit
    def converter_kelvin(self):
        kelvin=self.celsius+273.15
        return kelvin

temp1=float(input().strip())
if temperatura(temp1).converter_kelvin()<0:
    print("A temperatura não pode ser menor que o zero absoluto.")
else:
    print(f'Fahrenheit: {temperatura(temp1).converter_fahrenheit()}\n'
          f'Kelvin: {round(temperatura(temp1).converter_kelvin(),1)}')
