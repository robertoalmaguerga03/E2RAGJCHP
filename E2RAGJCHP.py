try:
    import requests
    import os
    import sys
    import webbrowser 
except ImportError: 
    os.system('pip install webbrowser')
    os.system('pip install request')
    os.system('pip install sys')
    os.system('pip install os')
    print('Instalando programas...') 
    print('Ejecuta de nuevo tu script...') 
    exit()

#Roberto Almaguer Garza
#Jair Caleb Hernandez Polendo

#Explicación: El programa primeramente importa los modulos a utilizar en las respectivas busquedas
#que hará el programa, seguido, nos pregunta dos numeros para usarlos como rango en la página de
#noticias de la UANL, después nos pide ingresar las siglas de alguna facultad. Después, con los
#numeros antes dados utilizando un if se asegura de que al primer numero sea menos que el segundo
#y de no ser asi, los reacomoda. Luego, por cada página en la que encuentre coincidencia con la
#dependencia que ingresamos, la abrirá en nuestro navegador.

print("Este script navega en las páginas de noticas de la UANL")
inicioRango = int(input("Pagina inicial para buscar: "))
finRango = int(input("Pagina final para buscar: "))
dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
if inicioRango > finRango:
    inicioRango,finRango = finRango,inicioRango
for i in range (inicioRango,finRango,1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get (url)
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    else:
        soup = bs(pagina.content,"html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content,"html.parser")
                parrafos = soup2.select("p")    
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print ("Abriendo",url2)
                        webbrowser.open(url2)
                        break
