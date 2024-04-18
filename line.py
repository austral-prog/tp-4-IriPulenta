def line():
    def line() :
	coeficiente_A = float(input ("Ingrese el coeficiente A:"))
	coeficiente_B = float(input ("Ingrese el coeficiente B:"))
	coeficiente_x1 = float(input ("Ingrese el coeficiente X1:"))
	coeficiente_x2 = float(input ("Ingrese el coeficiente X2:"))
	coeficiente_y1 = coeficiente_A*coeficiente_x1+coeficiente_B
	coeficiente_y2 = coeficiente_A*coeficiente_x2+coeficiente_B
	punto_1 = coeficiente_x1,coeficiente_y1
	punto_2 = coeficiente_x2,coeficiente_y2
	
	print (f"El coeficiente A de su ecuación de la recta es: {coeficiente_A}")
	print (f"El coeficiente B de su ecuación de la recta es: {coeficiente_B}")
	print (f" El coeficiente X1 de su ecuación de la recta es:{coeficiente_x1}")
	print (f"El coeficiente X2 de su ecuación de la recta es:{coeficiente_x2}")

	print(f""" para la siguiente ecuacion:
		y = coeficiente_A*x+coeficiente_B""")


	print(f""" dados los siguientes puntos: 
		punto_1({coeficiente_x1,coeficiente_y1})
		punto_2({coeficiente_x2,coeficiente_y2})""")
	distance = math.dist (punto_1,punto_2)
	print(f" distancia entre los puntos es:{distance}")
