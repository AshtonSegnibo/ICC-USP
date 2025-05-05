from datetime import datetime
from dateutil.relativedelta import relativedelta

dia,mes,ano=map(int,input().split('/'))

nascimento=datetime(ano,mes,dia)

hoje=datetime(2024,4,4)

idade = relativedelta(hoje,nascimento)

anos=f'{idade.years} ano'+('s' if idade.years!=1 else '')
meses=f'{idade.months} '+('mes' if idade.months==1 else 'meses')
dias=f'{idade.days+1} dia'+('s' if idade.days!=1 else '')





print(f'{anos}, {meses} e {dias}')


