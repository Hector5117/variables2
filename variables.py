###Variables###

my_string_variable = "My string variable"
#print(my_string_variable)

my_int_variable = 5
#print(my_int_variable)

my_float_variable = 1.8
#print(my_float_variable)
#print(type(my_float_variable))

my_int_to_str_variable = str(my_int_variable)
#print(my_int_to_str_variable)
#print(type(my_int_to_str_variable))

my_bool_variable = True
#print(my_bool_variable)
#print(type(my_bool_variable))



#concatenacion de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:",my_bool_variable)

#algunas funciones del sistema
#len obtiene largo de la cadena
print(len(my_string_variable))

#variables en una sola linea. ¡Cuidado con abusar de esta sintaxis!

name, surname, alias, age = "Hector", "Sanchez", 'Laxer', 32 
print("Me llamo:", name,surname, "Mi edad es:",
      age, ". Y mi alias es:", alias)

# Inputs 

name = input('¿Cual es tu nombre?')
age = input('¿Cuantos años tienes?')
print(name)
print(age)
print(type(name))
print(type(age))

#cambiamos su tipo
name = 35 
age = brais
print(name)
print(age)
print(type(name))
print(type(age))

#¿forzamos el tipo?
address: str = "Mi direccion"
address = input('¿cual es su direccion?')
#address = True
#address = 5
#address = 1.2
print(type(address))


#¿forzamos el tipo?
address: int= 1 
address = input('¿cual es su direccion?')
#address = True
#address = 5
#address = 1.2
print(type(address))
