#Find me a name
#Leonadro Duarte
def printList(list, **kwargs):
    bullet = kwargs.get("bullet", True)
    tab = kwargs.get('tab', True)
    limit = kwargs.get('limit', -1)
    c = 0
    for x in list:
        out = ''
        if tab:
            out += '\t'
        if bullet:
            out += '* '
        out += x
        print(out)
        c += 1
        if c == limit:
            break

    

#\$P\{[A-Za-z][0-9]?.?[A-Z\-Z]*[0-9]?\}
def genFileName(**kwargs):
    px = kwargs.get("prefix", 'out')
    sx = kwargs.get("sulfix", None)
    typ = kwargs.get("type_mod", None)
    time_mod = kwargs.get("time_mod", False)
    
    ct = datetime.datetime.now()
    name_mod = f'{ct.month}{ct.day}{ct.hour}{ct.minute}{ct.second}'
    
    name = px
    if sx != None:
        name += sx
    if time_mod:
        name += name_mod
    if typ != None: 
        name += typ
    return name
