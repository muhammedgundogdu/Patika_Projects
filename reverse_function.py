liste_old=[[1, 2], [3, 4], [5, 6, 7]]
liste_old=liste_old[::-1] #listeyi kendi içerisinde ters döndürür [[2, 1], [4, 3], [7, 6, 5]]

for i in range(len(liste_old)):
    (liste_old[i])=(liste_old[i])[::-1] #listenin tamamını ters döndürür [[7, 6, 5], [4, 3], [2, 1]]

print(liste_old)
