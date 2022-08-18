liste_old= [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
liste_new=[]

def flatten(n):
    for i in n:
        if isinstance(i,list): #eleman liste halindemi değilmi kontrol ediyor listeyse tekrardan fonksiyonu çağırıyor
            flatten(i)
        else:
            liste_new.append(i)    

flatten(liste_old)
print(liste_new)