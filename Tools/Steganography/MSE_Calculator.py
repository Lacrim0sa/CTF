from skimage import io
import numpy as np

# Load the two images
img1 = io.imread('image1.jpg')
img2 = io.imread('image2.jpg')

# Calculate the mean squared error
mse = ((img1 - img2) ** 2).mean()

print("MSE: ", mse)

#####
# En stéganographie, le "MSE" peut signifier "Mean Square Error" en anglais, ou "Erreur Quadratique Moyenne" en français, mais il se réfère généralement à une mesure de la distorsion entre deux images, à savoir l'image originale (aussi appelée "image couverture") et l'image qui a été modifiée pour y cacher des informations secrètes (aussi appelée "image stéganographique" ou "image avec du contenu stéganographique").
#
# Le MSE en stéganographie est calculé en prenant la différence pixel par pixel entre les valeurs des pixels de l'image couverture et de l'image stéganographique, en élevant cette différence au carré pour éviter que les valeurs positives et négatives se compensent, puis en prenant la moyenne de ces valeurs carrées sur l'ensemble des pixels. Une valeur de MSE plus basse indique généralement que l'image stéganographique est plus similaire à l'image couverture, ce qui signifie que les informations secrètes ont été cachées avec moins de distorsion.
#
# Le MSE est l'une des mesures couramment utilisées pour évaluer la qualité de la stéganographie, car il permet de quantifier objectivement la distorsion entre l'image originale et l'image stéganographique. 
# Cependant, il existe d'autres mesures de la qualité en stéganographie, notamment la différence de pixel absolue (DPA) et la corrélation (ou autocorrélation) entre les images, qui peuvent également être utilisées pour évaluer la performance de techniques stéganographiques.
#####
