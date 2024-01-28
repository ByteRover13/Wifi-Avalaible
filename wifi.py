
import os
import sys
from colorama import Fore, Style

#mamatana2807

def conectred():
    os.system("nmcli device wifi list")
    casual = input(f"{Fore.BLUE}Desea Conectarse a una red ? Si/No: {Style.RESET_ALL}").lower()
    if casual == "no":
        print(f"{Fore.GREEN}App Cerrado Correctamente{Style.RESET_ALL}")
    elif casual == "si":
        ssid = input(f"{Fore.BLUE}Ingresar SSID de la red : {Style.RESET_ALL}")
        passwd = input(f"{Fore.BLUE}Ingresar password : {Style.RESET_ALL}")
        os.system(f"nmcli device wifi connect '{ssid}' password {passwd}")
    else:
        print(f"{Fore.RED}Opcion incorrecta, vuelve a intentarlo{Style.RESET_ALL}")
try:
    usuario = int(input(f"{Fore.YELLOW}1 -> Redes Disponibles \n2 -> Conectar a una red \n3 -> Mostrar conexion actual{Style.RESET_ALL}\n{Fore.GREEN}Escoja cualquiera de las dos opciones: {Style.RESET_ALL}"))

    match usuario:
        case 1:
            conectred()
        case 2:
            ssid = input(f"{Fore.BLUE}Ingresar SSID de la red : {Style.RESET_ALL}")
            passwd = input(f"{Fore.BLUE}Ingresar password : {Style.RESET_ALL}")
            os.system(f"nmcli device wifi connect {ssid} password {passwd}")

        case 3:
            print(f"{Fore.BLUE}Conexiones Actuales: \n")
            os.system("nmcli connection show")
        case _:
            print("Opcion invalida")
except KeyboardInterrupt:
    sys.exit()