import cv2
import math

# Load the two images
img1 = cv2.imread("image1.jpg")
img2 = cv2.imread("image2.jpg")

# Calculate the mean squared error
mse = ((img1 - img2) ** 2).mean()

# Calculate PSNR
if mse == 0:
    psnr = float('inf')
else:
    MAX_I = 255.0
    psnr = 20 * math.log10(MAX_I / math.sqrt(mse))

print("PSNR: ", psnr)

# Le PSNR (Peak Signal-to-Noise Ratio), ou Rapport Signal-Bruit Crête en français, est une autre mesure couramment utilisée pour évaluer la qualité de l'image en stéganographie, ainsi que dans d'autres domaines de traitement d'image.
#
# Le PSNR est une mesure de la qualité de l'image basée sur la différence entre les valeurs des pixels de l'image originale (ou image couverture) et de l'image modifiée (ou image stéganographique), combinée avec la puissance du bruit (différence entre l'image originale et l'image modifiée). Mathématiquement, il est défini comme suit :
#
# PSNR = 10 * log10((L^2) / MSE)
#
# où :
#
# PSNR est le rapport signal-bruit crête en décibels (dB)
# L est la plage dynamique maximale possible des valeurs de pixel (par exemple, pour une image en niveaux de gris, L serait égal à 255 pour des pixels codés sur 8 bits)
# MSE est l'erreur quadratique moyenne entre les valeurs de pixel de l'image originale et de l'image modifiée.
# Un PSNR plus élevé indique généralement une meilleure qualité d'image, car cela signifie que l'image modifiée est plus similaire à l'image originale avec moins de distorsion.
#
# Le PSNR est largement utilisé dans la littérature scientifique et dans l'industrie pour évaluer la qualité d'image en stéganographie, ainsi que dans d'autres applications de traitement d'image où la fidélité de l'image est importante, comme la compression d'image et la restauration d'image. Cependant, il convient de noter que le PSNR peut ne pas toujours être parfaitement corrélé avec la perception visuelle de la qualité d'image par les êtres humains, car il ne tient pas compte de certains aspects de la perception visuelle, tels que la sensibilité à certaines distorsions visuelles. Par conséquent, il est souvent recommandé d'utiliser plusieurs mesures de qualité d'image, y compris le PSNR, en combinaison avec des évaluations subjectives basées sur des observateurs humains, pour obtenir une évaluation complète de la qualité d'image.
