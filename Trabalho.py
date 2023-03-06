#Processo de Gram–Schmidt é um algoritmo para obter uma base ortogonal (ou ortonormal) a partir de uma base qualquer. De maneira mais geral, o método permite transformar um conjunto de vetores linearmente independentes em um conjunto ortogonal que gera o mesmo espaço vetorial.
#

import numpy as np 

print("Processo de Gram–Schmidt no R²")

flag = 0
while flag == 0:

  v1=float(input("\nDigite o primeiro vetor v1: "))
  v2=float(input("Digite o segundo vetor v2: "))
  v3=float(input("Digite o terceiro vetor v3: "))
  v4=float(input("Digite o quarto vetor v4: "))
  
  x= [v1,v2]
  y= [v3,v4]
  z=[x,y]
  R=[[v1,v2],[v3,v4]]
  mT=np.array(R)
  
  det=np.linalg.det(mT)
  
  #Verificação se são L.I
  if det==0:
    print('\n Não é possível realizar o processo de Gram–Schmidt, pois, os 2 vetores são linearmente dependentes e não são bases.')

  else:
    flag = 1
    
    print("\n>>> É Linearmente independente, e sua base escolhida foi: ",z)
    
    #O processo de Gram–Schmidt
    u1 = [v1, v2] 
    u2 = [v3, v4]
    
    a= ((v1*v3)+(v2*v4))
    b= ((v1**2)+(v2**2))
    α = a/b
    
    U2 = [v3-(α*v1),v4-(α*v2)]
    vetorortoGonal = [u1, U2]
    
    #Normalização
    nv1 = v1/(b**0.5)
    nv2= v2/(b**0.5)
    nw1=[nv1,nv2]
    
    c= v3-(α*v1)
    
    d= v4-(α*v4)
    prodOeP= ((c**2)+(d**2))
    nv3= c/(prodOeP**0.5)
    nv4= d/(prodOeP**0.5)
    nw2= [nv3,nv4]
    
    vetorOrtonormal = [nw1, nw2]
    
      
    if np.dot(u1,u2) == 0:
       print("\nOs seus vetores já são ortoganais")
       print ("\nA Sua base ortonormal é: ", vetorOrtonormal)
    
    else:
      print ("\nA Sua base ortogonal é: ", vetorortoGonal)
      print ("\nA Sua base ortonormal é: ", vetorOrtonormal)