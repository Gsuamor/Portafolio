#Reescriba el ejercicio de la hipoteca considerando que el deudor incrementa sus pagos en un porcentaje que este define en los periodos impares 

# Captación de los datos 
print("Cálculo de la cuota de una hipotéca('método fracés')")
print('Indique monto del préstamo')

k= input ()

print('Indique la tasa de interés: ')

i= input()

print('Indique el número de cuotas ():')

n= input()

print('Indique el porcentaje de incremento en los periodos impares:')
h = input()

k= float(k)
i= float(i) / 100
n= int(n)
h= float(h) / 100

# Cálculo de la cuota (procesamiento de Datos)
valor_actual= 0 
count_h= 0
for j  in range(n):
    if (j + 1) % 2 == 0:
        valor_actual += (1 + h)**(count_h) *(1 + i)**(-(j + 1))
    else:
        valor_actual += (1 + h)**(-(count_h)) *(1 + i)**(-(j + 1))
         
        
q= k / valor_actual 

    
# Impresión de los Datos

print ('resultados')
print ('Un prestamo de :' , k)
print ('Con una tasa de interés de:', i)
print ('a pagar en esta cantidad de meses :', n)
print ( 'Con una cuota mensual de:', q)



