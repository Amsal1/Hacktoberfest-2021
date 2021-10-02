def tower_builder(n_floors):
    n_floors-=1 
    ast = 1
    tower = []
    
    while n_floors >= 0:
        a = n_floors*"b" + ast*"*" + n_floors*"b"
        ast += 2
        tower.append(a)
        print "a:",a
        n_floors-=1 
    return tower

print tower_builder(3)
