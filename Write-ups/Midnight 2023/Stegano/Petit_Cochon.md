# Petit Cochon
## Stega JPG / PNG | Le canal

### Challenge

Vous trouvez cette image dans le téléphone d'une personne disparue.  

Prouvez qu'il cache quelque chose.  

Fichier : https://cdn.midnightflag.fr/petit-cochon.zip  

Auteur : KØDΛ  

Au premier abord, il s'agit bien d'un fichier jpeg :  

![image](https://user-images.githubusercontent.com/70716302/232308650-66ecfee8-8fa0-43e8-a6ed-0245af3d91fa.png)  

J'enchaîne sur un test rapide, avec un petit **Binwalk** juste pour voir s'il n'y a pas un petit quelque chose qui traîne :  

![image](https://user-images.githubusercontent.com/70716302/232308825-c78cd2ba-b0f0-40c6-bfbe-12c352bf70bc.png)  

Une archive Zip, un fichier "name: step2or3.jpg", ok jackpot !  
Je l'extrais, toujours avec **Binwak** :  

![image](https://user-images.githubusercontent.com/70716302/232308953-a6b5a819-1b64-4d45-96ae-11cd08bc8141.png)  

Avant même de bouger un doigt, un **File** sur le fichier .jpg : 

![image](https://user-images.githubusercontent.com/70716302/232309064-89cb2f1b-5c82-4613-bad4-add08c8561a9.png)  

Il s'agit donc d'un PNG et non pas d'un JPG. Je revois l'extension du fichier, et à suivis à cet instant une batterie de tests non-concluant.  
Pour finir, un détail, en parcourant l'image avec l'outil stegsolve, j'arrive sur le 4em bit du canal blue et on peut observer cette image :  

![image](https://user-images.githubusercontent.com/70716302/232309265-f28cd4f2-1159-4730-b7e2-bfccb729efc1.png)  

Et si on regarde tout en haut :  

![image](https://user-images.githubusercontent.com/70716302/232309373-731358c9-356d-436f-8a06-4d3509993060.png)

Une ligne un peu bizarre, je décide donc de me diriger sur le Data Extract de l'outil, je me positionne sur le 4em bit du canal bleu et j'extrais :  

![image](https://user-images.githubusercontent.com/70716302/232309476-09596f3f-d796-4f87-98bf-984506dcbd4f.png)  

Du binaire ? Ouais, c'est du binaire, je n'ai pas écouté à l'école, mais c'est du binaire.

Après un mal de crâne, ce binaire serais du Baconian Cipher...  
La méthode Baconian, également connue sous le nom de chiffrement de Bacon, est une technique de cryptographie utilisée pour encoder des messages en utilisant un alphabet binaire de caractères.  
Elle a été développée par l'écrivain et philosophe anglais Francis Bacon au début du XVIIe siècle.

Très bien, maintenant, flemme de decode à la mano, direction [Decode](https://www.dcode.fr/bacon-cipher)  

Résultat :  

![image](https://user-images.githubusercontent.com/70716302/232312643-229a6116-f036-4a52-837a-bd772866ef5d.png)  
  
YES ! Flag : **MCTF{SHAKESPEARECYPHEREXAMINED}**
