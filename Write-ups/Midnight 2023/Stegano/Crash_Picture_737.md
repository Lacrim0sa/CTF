# Crash Picture 737
## Stega PNG | Les chunks

### Challenge
Plusieurs kilometres après la derniere trace du vol, des valises ont été retrouvée. Un ordinateur a pu etre trouvé. Après une analyse, nous remarquons qu'une image à été envoyé quelques minutes avant la perte de la communication. Les analystes pensent que cette image n'est pas valide. Prouvez leur le contraire.

Autheur: KØDΛ

Je télécharge le fichier zip, j'extrais et on obtient le fichier "crash".
Première étape, il faut en apprendre plus sur ce fichier en utilisant la commande file :
![image](https://user-images.githubusercontent.com/70716302/232286608-69ce9ac2-c5cd-4326-80ce-9a4248469a3a.png)

JFIF est l'acronyme de "JPEG File Interchange Format", qui se réfère à un format de fichier d'image utilisé pour les images JPEG compressées.
Une image jpeg donc ?
Je passe bêtement l'extension du ficher au format ".jpg" :
![image](https://user-images.githubusercontent.com/70716302/232286949-f650a10e-e104-48d8-9b77-f9db1c3b9ef7.png)

Bon... C'étais prévisible.
Par curiosité, j'ouvre le fichier avec hexeditor :
![image](https://user-images.githubusercontent.com/70716302/232287522-c3796f3b-0d57-43bf-9090-4fc77e32565e.png)

Au premier coup d'oeil on peut observer les chunks "IHDR" / "IDAT"
Lourd le fichier jpeg avec un file format PNG !

Mon hypothèse est donc que les chunks du fichier PNG on été altéré, il faut les reconstruires.
J'écrase le début du fichier avec la signature PNG "89 50 4E 47 0D 0A 1A 0A" et je rectifie la longueur du chunks IHDR "00 00 00 0D" :
![image](https://user-images.githubusercontent.com/70716302/232288071-ee4e931b-5832-4667-9ff7-2834508df9ae.png)

Je change l'extension du fichier par ".png", et là, normallement notre image devrait se sentir un peu mieux dans sa petite tête de PNG.
![image](https://user-images.githubusercontent.com/70716302/232288156-54663415-a311-49c8-af81-6935af11a031.png)
Une merveille ! Bon... Prévisible...

Je sors la caisse à outils, TWEEKPNG :
![image](https://user-images.githubusercontent.com/70716302/232288336-562d930b-0b8a-4389-948f-97c60437c3a3.png)

Je lance l'image viewer :
![image](https://user-images.githubusercontent.com/70716302/232288364-e90d9bae-d6ca-45ff-8755-12f80469b867.png)

Un problème avec les chunks IDAT's ? Bun voyons, je me suis souvenu d'un chall, où les chunks IDAT devaient être manipulés pour reconstruire l'image, je me mets à tripoter leur position :
![image](https://user-images.githubusercontent.com/70716302/232288814-f091cb75-97fb-4be5-9a4b-a0ff842fc465.png)

BINGO ! Flag : MCTF{a3ro_chunk_n0p_f!l3}

Liens :
https://en.wikipedia.org/wiki/PNG
https://entropymine.com/jason/tweakpng/

Auteur de l'article : Anth0 alias Lacrim0sa
