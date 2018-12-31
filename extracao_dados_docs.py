#Objetivo: extrair dados de uma determinada regiao de documentos em formato de imagem
#Nesse projeto todas as imagens são iguais apenas para simulacao, pode ser aplicado em documentos com pequenas alteracoes como a data
import cv2
import glob
import os
import pytesseract as pt

#varredura na psta com as imagens imagens
for path in glob.glob("docs/*.jpg"):
	image = cv2.imread(path)
	
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	
	#cortando a regiao com a data
	t_y,b_y,l_x = 145, 210, 270
	data = gray[t_y:b_y,l_x:]

	#reconhecendo os caracteres com pytesseract
	texto = pt.image_to_string(data)
	print("Data: ", texto)
	
	#exibe a imagem recortada com a regiao de interesse
	cv2.imshow("Cortada",data)
	cv2.waitKey(0)
	cv2.destroyAllWindows()



