dic1,dic2=input().split(';')
dic1=eval(dic1)
dic2=eval(dic2)
dic3={**dic1,**dic2}

print(dic3)

#or

dic1.update(dic2)

print(dic1)

#or

dic3 = dict(dic1, **dic2)

print(dic3)
