from os import remove


print("****ajenda telefonica****")
nome=[]
numero=[]
opicao=0

while opicao != 6:

    print("OPIÇÃOS:","\n","1-LISTAR CONTATO","\n","2-INSERIR CONTATO","\n","3-ALTERAR CONTATO","\n","4-BUSCAR CONTATO","\n","5-REMOVER CONTATO","\n","6-SAIR")
    opicao=int(input("sua opição:"))

    if opicao==1:
        print(nome,"---", numero,)
    
    elif opicao==2:
        n1=input("nome:")
        nome.append(n1)
        n2=int(input("numero:"))
        numero.append(n2)

    elif opicao==3:
        
        n=input("nome do contato:")
        
        if n in nome:
            nome.remove(nome[n])
            del(numero[n])
            n1=input("novo nome:")
            nome.append(n1)
            n2=int(input("novo numero:"))
            numero.append(n2)
        
        else :
            print("não existe na lista")









print("FIM DO PROGRAMA!")

    