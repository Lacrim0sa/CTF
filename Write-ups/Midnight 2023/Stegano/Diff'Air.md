# Diff'Aire
## Stega JPG | Une différence

### Challenge

Dans la galerie de l'attaquant, il y a quelques photos mais il y a un détail intéressant, la photo suspecte est en deux copies, sûrement pour cacher une information ou une charge utile.

Essayez de trouver ce qu'elle cache.

Fichier : https://cdn.midnightflag.fr/DiffAir.zip  

Auteur : Nemo

Un zip, j'unzip, j'obtiens deux images jpeg.  
L'hypothèse est la suivante, deux images, une d'origine et une autre modifiée. Il faut donc faire le delta entre les deux.  

Je dump l'hexa des deux fichiers avec **xxd** :  

![image](https://user-images.githubusercontent.com/70716302/232305502-324031aa-764f-4066-ab34-e6d68b175e4f.png)  

Puis en utilisant **Diff**, je viens faire un comparatif :  

![image](https://user-images.githubusercontent.com/70716302/232305656-ccccd1fe-fd24-4092-8530-514b279ae123.png)  

On peut entrevoir une chaîne en base 64, copier coller, un one-liner, je décode :  

```echo "TUNURnttMXJyMHJfMW1hZzNfYzBtcDRyNGk1MG4hfQ==" | base64 --decode```  

![image](https://user-images.githubusercontent.com/70716302/232305907-d5be4856-fefe-4d03-8c8b-c1f4a3dd4d7d.png)

Hop hop hop ! Flag : **MCTF{m1rr0r_1mag3_c0mp4r4i50n!}**

Auteur de l'article : Anth0
