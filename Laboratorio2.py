"""
Nombre: Súper primo
Entrada: Num
Salidad: True o False
restricciones: Tiene que ser un número mayor a cero y positivo
"""
def superPrimo(num):
    if(isinstance(num,int) and num>0):
        return superPrimos_aux(num,0)
    else:
        return "El número debe ser entero positivo"
    
def superPrimos_aux(num,res):
    if(num==0):
        return primo(res)
    else:
        if((num%10)%2==1):
            return superPrimos_aux(num//10,res+num%10)
        else:
            return superPrimos_aux(num//10,res)

def primo(num):
    if(num==1 or num==2):
        return True
    else:
        return primo2(num,2)

def primo2(num,i):
    if(i==num):
        return True
    else:
        if(num%i==0):
            return False
        else:
            return primo2(num,i+1)
#-------------------------------------------------------------------------------------
"""
Nombre: Números Compadres
Entrada: num,num1
Salidad: similitud de números
restricciones: Tiene que ser un número mayor a cero y positivo
"""
def numerosCompadres(num,num1):
    if isinstance(num,int) and isinstance(num1,int):
        if(num1>=3):
            return ("Error, el numero debe tener 3 o mas digitos")
        elif num1>=num:
            return numerosCompadresAux(num%1000,num1)
        else:
            return numerosCompadres(num//10,num1)
    else:
        return ("Digite un numero entero positivo ")

def numerosCompadresAux(num,num1):
    if num1<100:
        return False
    else:
        if num==num1%1000:
            return True
        else:
            return numerosCompadresAux(num,num1//10)
#-----------------------------------------------------------------------------------------
"""
Nombre: Factor de número
Entrada: num
Salidad: cantidad de veces que es el número factor 
restricciones: Tiene que ser un número mayor a cero y positivo
"""
def factoresNumero(num):
    if(isinstance(num,int)and num>0):
        return factoresNumero_aux(num,2,2,0,0)
    else:
        return print("error,digite un numero entero positivo")


def factoresNumero_aux(num,mul1,mul2,contar,res):
    if(contar==0):
        res=res//2-1
        return res
    elif(mul1*mul2==num)and mul!=2 and mul2!=num and mul1!=num1 and mul2!=1:
        return 1+factoresNumero_aux(num1,mu2,mul2+2,contar-1,res+1)
    elif(mul2==num):
        return factoresNumero_aux(num1,mul1+1,mul2-mul2,contar,res)
    else:
        return factoresNumero_aux(num1,mul1,mul2+1,contar-1,res)
        
  
        
#----------------------------------------------------------------------------------------------
"""
Nombre: Ascendente
Entrada: num
Salidad: Los números mayores 
restricciones: Tiene que ser un número entero
"""
def ascendente(num):
    if (isinstance(num,int)):
        x=num*-1
        y=Unioascendente_aux(x,num%10,0)
        if(num<0):
            return hacer_negativo(y)
        else:
            return Unioascendente_aux(num,num%10,0)
    else:
        return "El número debe ser entero"

def Unioascendente_aux(num,simi,pote):
    if (num==0):
        return 0
    else:
        if(pote==0):
            return (num%10)*10**pote+Unioascendente_aux(num//10,num%10,pote+1)
        if ((num%10)>=simi):
            return  (num%10)*10**pote+Unioascendente_aux(num//10,num%10,pote+1)
        else:
            return Unioascendente_aux (num//10,simi,pote)

def hacer_negativo(num):
    return num*-1

