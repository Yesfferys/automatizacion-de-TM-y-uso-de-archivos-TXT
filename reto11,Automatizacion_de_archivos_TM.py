

"""
this program is a test to evaluate the multiplie tablets, in this, register a user and save it in a file if it exits, if not, create a file to save it.
also register the average for each player to be evaluated y show it on the screen
"""

import random
import os
import time
# presentaciones 

def generador_test():
	"""
	Only generate the option for the user and return the option to be processed
	"""

	print("---")
	print()
	print("GENERADOR DE TEST")
	print()
	print("---")
	print("1. Entrar al sistema")
	print("2. Darse de alta")
	print("3. Salir")
	print("--->")

	opcion=input("Por favor introduce una opcion: ")
	while opcion not in ("1","2","3"):
		opcion=input("Por favor introduce NUEVAMENTE una opcion: ")
		print(" Esa opcion No es valida ")
	else:	
		if opcion == "1":
			return 1
		elif opcion == "2":
			return 2
		elif opcion == "3":
			return 3 

def entrada_al_sistema(usuario):
	"""
	only generate the option for the user and return the option to be processed, after the user is validated
	"""

	print("---")
	print()
	print("USUARIO: ",usuario)
	print()
	print("---")
	print("1. Hacer TEST")
	print("2. Puntuaciones")
	print("3. Salir")
	print("--->")

	opcion=input("Por favor introduce una opcion: ")
	while opcion not in ("1","2","3"):
		print(" Esa opcion No es valida ")
		opcion=input("Por favor introduce NUEVAMENTE una opcion: ")
		
	else:	
		if opcion == "1":
			return 1
		if opcion == "2":
			return 2
		if opcion == "3":
			return 3

def ver_puntuaciones(usuario,veces,mejor,media):
	"""
	Show the user only the count, the best result, and the average of the tests done
	"""

	print("---")
	print()
	print("PUNTUACIONES DE: ",usuario)
	print()
	print("-----------------------------")
	print("Veces","|","Mejor","|","Media")
	print(" ",veces,"| ","{:.2f}".format(mejor),"| " ,"{:.2f}".format(media))
	print("-----------------------------")

def verificar_usuario():
	"""
	check if the entered user exists if not inform that must to regiter 
	"""
	
	if os.path.exists("usuarios_registrados.txt"):
		with open("usuarios_registrados.txt","r",encoding="utf-8") as archivo:
			usuarios=archivo.read()
			usuarios=usuarios.strip()
			claves=usuarios.split("\n")
			clave_verificada = [elemento.split(",") for elemento in claves]								 # example [['santiago', '12345'], ['elizabeth', '54321']]

			validacion_usuario=[]
			validacion="rechazada"

			estado_validacion_nombre = False
			while estado_validacion_nombre==False:
				entrada_usuario = input("Por favor introduce tu Nombre de usuario: ").lower()
				for elemento in clave_verificada:
					if entrada_usuario == elemento[0].lower():
						estado_validacion_nombre=True
						validacion_usuario.append(entrada_usuario)
				if estado_validacion_nombre==False:
					
					print("Debes darte de alta con el nombre de USUARIO marcado")
					continuar=input("Presione enter para continuar")
					os.system("cls")
					return validacion_usuario,validacion

					

						

				print()
				print("Introduce tu contraseña - recuerda que los campos son sensibles a letras May y Min")
				estado_validacion_contraseña = False

				intentos=2
				while not estado_validacion_contraseña:
					if intentos>=1:
						print("Tienes ", intentos ," intentos para crear la contraseña")
						entrada_contraseña= input("Por favor introduce tu contraseña: ").lower()
						intentos-=1
						continuar=input("Presione enter para continuar")
						os.system("cls")
						for elemento in clave_verificada:
							if entrada_contraseña == elemento[1].lower():
								estado_validacion_contraseña = True
								validacion_usuario.append(entrada_contraseña)
								validacion="verificada"
						if estado_validacion_contraseña == False:
							print("Tienes ", intentos ," intentos para ingresar la contraseña")
							entrada_contraseña = input("Por favor introduce tu contraseña: ").lower()
							intentos-=1
							continuar=input("Presione enter para continuar")
							os.system("cls")
					else:
						print("Intentalo de nuevo")
						break
						




			os.system("cls")
			return validacion_usuario,validacion																
		
	else:
		validacion_usuario="USUARIO DESCONOCIDO"
		validacion="rechazada"
		print("Debes darte de alta, ERES EL PRIMER USUARIO EN SER REGISTRADO")
		return validacion_usuario,validacion
		continuar=input("Presione enter para continuar")


def darse_de_alta():
	"""
	check if usuarios_registrados file exists if not create a new file whit same name and to enter the user new
	"""
	if os.path.exists("usuarios_registrados.txt"):
		with open("usuarios_registrados.txt","r") as archivo:
			texto=archivo.read()																	
			archivo=texto.split("\n")																
			archivo_formateado=[elemento.split(",") for elemento in archivo]						
			usuario=input("Porfavor introduce el nombre de USUARIO a registrar: ").lower()
			
			registrado=False
			for elemento in archivo_formateado:
				if elemento[0]==usuario:
					return "Este USUARIO ya se encuentra registrado"
					continuar=input("Presione enter para continuar")
					
			
			
			if registrado==False:
				print("El usuario ",usuario," no se encuentra registrado")
				print()
				print("Quieres registrar al usuario?")
				respuesta=input("Introduce -----> 'Yes'  o  'No' ").upper()
				continuar=input("Presione enter para continuar")
				os.system("cls")

				while respuesta not in ("YES","NO"):
					respuesta=input("Introduce nuevamente-----> 'Yes'  o  'No' ").upper()
					continuar=input("Presione enter para continuar")
					os.system("cls")
				else:
					if respuesta=="YES":
						with open("usuarios_registrados.txt","a") as archivo:
							primer_usuario=usuario


							while True:
								while True:
									primera_contraseña=input("Porfavor introduce la contraseña a crear: ")
									if validar_contrasena(primera_contraseña)==False:
										print("Debe contener 1 Letra MAY")
										print("Debe contener 1 Letra MIN")
										print("Debe contener 1 numero")
										continuar=input("Presione enter para continuar")
										os.system("cls")
									else:
										print(" La contraseña cumple con las condiciones anteriores ")
										continuar=input("Presione enter para continuar")
										os.system("cls")
										break
								
								print("Estas seguro de la CONTRASEÑA que deseas registrar? ")

								respuesta=input("Introduce -----> 'Yes'  o  'No' ").upper()
								while respuesta not in ("YES","NO"):
									respuesta=input("Introduce nuevamente-----> 'Yes'  o  'No' ").upper()
									continuar=input("Presione enter para continuar")
									os.system("cls")

								else:
									if respuesta=="YES":
										print("contraseña registrada con exito")
										break
									elif respuesta=="NO":
										#primera_contraseña=input("Porfavor introduce la contraseña a crear: ")
										continuar=input("Presione enter para continuar")
										os.system("cls")
										continue


							usuario=primer_usuario+","+primera_contraseña+"\n"
							archivo.write(usuario)
							
					elif respuesta=="NO":
						print("No se registrara ningun usuario, por parte del cliente")
						continuar=input("Presione enter para continuar")
						os.system("cls")

						
	else:
		with open("usuarios_registrados.txt","w") as archivo:
			primer_usuario=input("Porfavor introduce el nombre de usuario a crear: ")
			print("Estas seguro del nombre de USUARIO que deseas registrar? ")

			respuesta=input("Introduce -----> 'Yes'  o  'No' ").upper()
			continuar=input("Presione enter para continuar")
			os.system("cls")
			while respuesta not in ("YES","NO"):
				respuesta=input("Introduce nuevamente-----> 'Yes'  o  'No' ").upper()
			else:
				if respuesta=="SI":
					primer_usuario=primer_usuario
				elif respuesta=="NO":
					primer_usuario=input("Porfavor introduce NUEVAMENTE el nombre de usuario a crear: ")
					continuar=input("Presione enter para continuar")
					os.system("cls")


			primera_contraseña=input("Porfavor introduce la contraseña a crear: ")
			print("Estas seguro de la CONTRASEÑA que deseas registrar? ")

			respuesta=input("Introduce -----> 'Yes'  o  'No' ").upper()
			while respuesta not in ("YES","NO"):
				respuesta=input("Introduce nuevamente-----> 'Yes'  o  'No' ").upper()
				continuar=input("Presione enter para continuar")
				os.system("cls")
			else:
				if respuesta=="SI":
					primera_contraseña=primera_contraseña
				elif respuesta=="NO":
					continuar=input("Presione enter para continuar")
					primer_usuario=input("Porfavor introduce NUEVAMENTE el nombre de usuario a crear: ")

			usuario=primer_usuario+","+primera_contraseña+"\n"
			archivo.write(usuario)
			#print("Se ha registrado con exito")
			return "Se ha registrado con exito"
			continuar=input("Presione enter para continuar")
			os.system("cls")


def test(valor_nombre):
	"""
	Generate a test about multiple tablets to be evaluated. In this, ask the user which tablet they want to work with
	"""
	def funcion_tabla(n):
		tabla=dict()
		for i in range(1,11):
			tabla[n,i]=i*n
		return tabla

	print(" Vamos a practicar las tablas de multiplicar ")
	print("           Trata de no equivocarte           ")
	print()

	while True:
		print()
		print("Vamos a estudiar las tablas de multiplicar")
		tabla_estudiar=input(" Introduce la tabla a estudiar --- >  ")
		while tabla_estudiar not in ("1","2","3","4","5","6","7","8","9","10") and tabla_estudiar.isdigit()==False:
			tabla_estudiar=input(" Introduce bien la tabla que quieres estudiar en un rango del 1 al 10--- >  ")
		else:
			tabla_estudiar=int(tabla_estudiar)

		tablita=funcion_tabla(tabla_estudiar)

		print(f"empezemos a estudiar ",valor_nombre)

		registro=[]
		while True:
			contador=0
			maximo=3
			estado=None
			conteo_buenas=0
			conteo_malas=0
			while contador<maximo:
				pregunta=random.randint(1,10)
				pregunta1=pregunta*tabla_estudiar
				print(f'Cuanto es ',pregunta,' X ',tabla_estudiar,' ? ')
				
				respuesta= input("La respuesta es: ")
				while respuesta.isdigit()== False:
					respuesta=input("La respuesta debe ser un numero, introduce tu respuesta de nuevo: ")				
				else:
					respuesta=int(respuesta)
				
				if  tablita[(tabla_estudiar,pregunta)]==respuesta:
					estado="Has acertado, continuemos"
					print()
					print(estado)
					contador+=1
					conteo_buenas+=1
				else:
					estado="   Has fallado"
					print(estado)
					contador+=1
					conteo_malas+=1
				
				
				registro.append([contador,pregunta,tabla_estudiar,respuesta,estado])
				print()
				print(f"Te quedan ",maximo-(conteo_malas+conteo_buenas)," preguntas por responder ")
				if len(registro)>0:
					for i in range(len(registro)):
						print(f'Pregunta ',registro[i][0],' --> ',registro[i][1],'x',registro[i][2],'=', registro[i][3],' ---> ', registro[i][4])

				print()
				continuar=input("Presionar ENTER para continuar")
				os.system("cls")

			else:
				print("Debemos seguir estudiando")
				print(f'Obtuvistes',conteo_buenas,'buenas y ',conteo_malas,' malas')
				nota=conteo_buenas/maximo
				return str(nota)


def registro_de_juegos(usuario,nota): 
	"""
	register the note of each user if not generate one file to register the nota and user
	"""
	valores=usuario+","+nota
	if os.path.exists("registro_de_juegos.txt"):
		with open("registro_de_juegos.txt","a") as archivo:
			texto=archivo.write(valores+"\n")
			
	else:
		 with open("registro_de_juegos.txt","a+") as archivo:
		 	texto=archivo.write(valores+"\n")

def mostrar_puntuaciones(usuario):												 
	"""
	Count the number of times each user has played
	find the best note for each user
	Find the average number of times played for each player
	"""
	if os.path.exists("registro_de_juegos.txt"):
		with open("registro_de_juegos.txt","r") as archivo:
			texto=archivo.readlines()
			texto_formateado=[elemento.strip("\n") for elemento in texto]
			lista_registro=[elemento.split(",") for elemento in texto_formateado]

			
			conteo_de_veces_jugadas_usuario=0
			notas_usuario_float=[]
			for elemento in lista_registro:
				if usuario in elemento:
					conteo_de_veces_jugadas_usuario+=float(1)
					notas_usuario_float.append(float(elemento[1]))

			mejor_nota_usuario=0
			for elemento in notas_usuario_float:		
				if elemento>mejor_nota_usuario:
					mejor_nota_usuario=elemento
					

			suma_notas_usuario_float=0
			for nota in notas_usuario_float:
				suma_notas_usuario_float+=float(nota)

			media_nota_usuario=suma_notas_usuario_float/conteo_de_veces_jugadas_usuario



			return conteo_de_veces_jugadas_usuario,mejor_nota_usuario,media_nota_usuario

	else:
			print("El usuario NO TIENE REGISTRO DE JUEGOS")
			return "no_registrado"


def validar_contrasena(contrasena):
	"""
	verify if pasword have all conditions
	"""
	if len(contrasena) < 1:
		return False
	if not any(c.islower() for c in contrasena):
		return False
	if not any(c.isupper() for c in contrasena):
		return False
	if not any(c.isdigit() for c in contrasena):
		return False
	return True


# program flow
#############################################################################################################################    

inicio=True
while inicio:
	opcion=generador_test()
	os.system("cls")
	if opcion==1: 																													
		validar_usuario,validacion=verificar_usuario()

		if validacion=="rechazada":
			print()
			print("Te recomendamos darte de alta o revisar tus contraseña con el administrador")
			continue

		elif validacion=="verificada":
			entrada_sistema=entrada_al_sistema(validar_usuario[0])

			if entrada_sistema == 1:																								
				nota=test(validar_usuario[0])	
				control_de_registro=registro_de_juegos(validar_usuario[0],nota)
				print()
				os.system("cls")
				continuar=input("Presionar ENTER para continuar")

			elif entrada_sistema == 2:																								  
				if mostrar_puntuaciones(validar_usuario[0])=="no_registrado":
					continuar=input("Presionar ENTER para continuar")
					os.system("cls")
					pass
				else:
					conteo_de_veces_jugadas_usuario,mejor_nota_usuario,media_nota_usuario=mostrar_puntuaciones(validar_usuario[0])
					os.system("cls")
					ver_puntuaciones(validar_usuario[0],conteo_de_veces_jugadas_usuario,mejor_nota_usuario,media_nota_usuario)
					continuar=input("Presionar ENTER para continuar")
					os.system("cls")

			elif entrada_sistema == 3:
				print("Fin del programa")
				time.sleep(3)
				break


	elif opcion==2:																												
		registro=darse_de_alta()
		continuar=input("Presionar ENTER para continuar")
		os.system("cls")

	elif opcion==3:
		print("Fin del programa")
		os.system("cls")
		time.sleep(3)
		inicio=False


