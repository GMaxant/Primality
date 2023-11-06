# Primality
Tries on primality in python

-----
Primality testing and factorisation of non primal numbers.
Save in a .csv file

-----
Pseudocode used to generate the python code:

Demander quelle est la valeur maximale à tester

Pour chaque nombre supérieur à 1 et inférieur à cette valeur maximale
	rechercher si c'est un nombre premier
		si c'est un nombre premier, le placer dans une liste de nombre premier croissante
		afficher le nombre à l'écran
		
	Si il n'est pas premier
		donner la liste de tous les nombres premiers qui permettent de le factoriser, et les stocker dans une liste
		

enregister la liste des nombres premiers dans un fichier de type premiers.csv
enregister la liste de tous les nombres étudiés, dans un tableau constitué en x de tous les nombres premiers, en y des nombres étudiés, et dont chaque colonne comportera le nombre de fois dont le nombre premier en x intervient dans la factorisation du nombre en y
