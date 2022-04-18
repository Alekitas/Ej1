class Email:
    __idcuenta=''
    __dominio=''
    __tipodominio=''
    __contrasenia=''
    def __init__ (self,idcuenta,dominio,tipodominio,contrasenia):
        self.__idcuenta=idcuenta
        self.__dominio=dominio
        self.__tipodominio=tipodominio
        self.__contrasenia=contrasenia
        
    def retmail(self):
        return self.__idcuenta+'@'+self.__dominio+'.'+self.__tipodominio
    
    def getdom(self):
        return self.__dominio
    
    def modcontrasenia(self):
        cont=input('\n ingrese contraseña actual: ')
        if self.__contrasenia==cont:
         cont.nuev=input('\n ingrese contraseña nueva: ')
         self.__contrasenia=cont.nuev 
         
    def crearcuenta(self,email):
        email=email.split('@')
        print(email)
        self.__idcuenta=email[0]
        dominio=email[1].split('.')
        print(dominio)
    def mostrardatos(self):
         print("(idcuenta,dominio,tipodominio) = (",self.__idcuenta,',', self.__dominio,',',self.__tipodominio,',',self.__contrasenia,")")
import csv
if __name__== '__main__':
    persona='Alekas'
    unemail=Email('alumnopoo', 'gmail', 'com', '1234')
    print('Estimado {} le enviaremos sus mensajes a la direccion:  '.format(persona), unemail.retmail())
    retmail=unemail.retmail()
    print(retmail)
    unemail.modcontrasenia()
    unemail.mostrardatos()
    email= input('Direccion de correo: ')
    lista=[]
    archivo=open('emails_1.csv')
    reader=csv.reader(archivo,delimiter=';')
    doming=input('Ingrese dominio a contar')
    c=0
    for fila in reader:
        lista=fila[0]+fila[1]+fila[2]
        if fila[1]==doming:
            c+=1
    archivo.close()
    print('cantidad de emails con el dominio ingresado: {}'.format(c))
    
    