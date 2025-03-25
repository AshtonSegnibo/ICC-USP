ent=eval(input())

def contar_termos(x):
    contagem=0

    if isinstance(x,list):
        for sub_item in x:
            contagem+=contar_termos(sub_item)
    else:
        contagem+=1
    
    return contagem

print(contar_termos(ent))






