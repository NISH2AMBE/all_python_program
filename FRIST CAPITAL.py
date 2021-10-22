# FRIST CAPITAL

def frist_capital(l,**kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]

names = ['nish','raj']
print(frist_capital(names,reverse_str=True))