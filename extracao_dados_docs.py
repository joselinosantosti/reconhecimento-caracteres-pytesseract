import cv2
import glob
import os
import requests
import pytesseract as pt
import matplotlib as plt

#varredura nas imagens
for path in glob.glob("docs/*.jpg"):
	image = cv2.imread(path)
	#altura, largura, profundidade
	#print(image.shape)
	#print(image)

	#_, ax1 = plt.subplots(figsize=(20,10))
	#ax1.imshow(image)

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	#print(gray.shape)
	#cv2.imshow("Cortada",gray)

	#cortando a imagem
	t_y,b_y,l_x = 145, 210, 270
	data = gray[t_y:b_y,l_x:]

	#reconhecendo os caracteres com pytesseract
	texto = pt.image_to_string(data)
	print("Data: ", texto)
	#cv2.imshow("Cortada",data)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()



