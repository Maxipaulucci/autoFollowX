#--------------------------------------------------------------------------------------------------------------
# Modulos importados
#--------------------------------------------------------------------------------------------------------------
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

#--------------------------------------------------------------------------------------------------------------
# Inicialización de variables
#--------------------------------------------------------------------------------------------------------------
pathDatos = "(path of the file with the username, the password and the name of the person you want to follow, inside these "")"
pathNavegador = "(path of your navigator web inside these "", in my case the path is: C:/Program Files/Google/Chrome/Application/chrome.exe)"

#--------------------------------------------------------------------------------------------------------------
# Codigo
#--------------------------------------------------------------------------------------------------------------
options = Options()
options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
options.add_argument("--incognito")  # Buscador se corre en incognito

#Cargar opciones al driver
driver = webdriver.Chrome(options=options)

#Acceder a X (Twitter)
driver.get("https://www.twitter.com")
sleep(2)

#Buscamos los campos para iniciar sesion
inicioSesion = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div')
inicioSesion.click()
sleep(2)

#Buscamos el campo para ingresar el nombre de usuario
usernameInput = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div')
usernameInput.click()

#Buscar datos para el inicio de sesion
try:
    datos = open(pathDatos, mode = "r", encoding = "utf-8")

    lineas = datos.readlines()

    if len(lineas) == 3:
        usuario = lineas[0].strip("\n").split(" ")[1]
        password = lineas[1].strip("\n").split(" ")[1]
    else:
        print("Error: El archivo no tiene la estructura esperada.")

except (OSError, FileNotFoundError) as detalle:
    print(f"Error: {detalle}")
finally:
    try:
        datos.close()
    except:
        pass
#Ingresamos nombre de usuario
pyautogui.typewrite(usuario)
pyautogui.press("enter")
sleep(1)

#Ingresamos contraseña de usuario
pyautogui.typewrite(password)
pyautogui.press("enter")
sleep(3)

#Tocar boton del cartel de seguridad en caso de aparecer
try: 
    security = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div/div/svg/g/path')
    security.click()
    sleep(5)
except NoSuchElementException:
    pass

#Tocar busqueda
searchUser_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
searchUser_button.click()

#Buscar en el archivo de texto el nombre de usuario de la persona que desea seguir
seguir = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
try:
    datos = open(pathDatos, mode = "r", encoding = "utf-8")

    lineas = datos.readlines()

    if len(lineas) == 3:
        persona = lineas[2].strip("\n").split(" ")[1]
    else:
        print("Error: El archivo no tiene la estructura esperada.")

except (OSError, FileNotFoundError) as detalle:
    print(f"Error: {detalle}")
finally:
    try:
        datos.close()
    except:
        pass

#Escribir la persona que quiere seguir
pyautogui.typewrite(persona)
pyautogui.press("enter")
sleep(1)

#Tocar la parte de personas
peopleButton = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[3]/a/div/div/span')
peopleButton.click()
sleep(1)

#Seguir a la persona
followButton = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/div/span/span')
followButton.click()
sleep(5)