from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given(u'que me meto a la url "{url}"')
def step_impl1(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)


@given(u'en la sección de inicio de sesión ingreso los datos "{usuario}" y contra "{contrasenia}"')
def step_impl2(context, usuario, contrasenia):
    context.driver.find_element(By.ID, 'id_username').send_keys(usuario)
    context.driver.find_element(By.ID, 'id_password').send_keys(contrasenia)
    context.driver.find_element(
        By.XPATH, '/html/body/div/div/div/div/div/div/div[2]/div/form/button').click()


@given(U'luego me meto a la url "{url}"')
def step_impl3(context, url):
    context.driver.get(url)


@given(u'en el registro agrego los datos usuario "{usuario}", correo "{correo}"')
def step_impl4(context, usuario, correo):
    time.sleep(3)
    context.driver.find_element(By.ID, 'username').send_keys(usuario)
    context.driver.find_element(By.ID, 'email').send_keys(correo)


@given(u'nombre "{nombre}", segundo nombre "{nombre2}", primer apellido "{apellido1}", segundo apellido "{apellido2}", programa academico "{programa}", unidad academica "{unidad}"')
def step_impl5(context, nombre, nombre2, apellido1, apellido2, programa, unidad):
    context.driver.find_element(By.ID, 'nombre').send_keys(nombre)
    context.driver.find_element(By.ID, 'nombre2').send_keys(nombre2)
    context.driver.find_element(By.ID, 'apellidoP').send_keys(apellido1)
    context.driver.find_element(By.ID, 'apellidoM').send_keys(apellido2)
    context.driver.find_element(By.ID, 'unidad_academica').send_keys(unidad)
    context.driver.find_element(
        By.ID, 'programa_academico').send_keys(programa)


@given(u'contraseña "{contra}" y confirmar "{recontra}"')
def step_impl6(context, contra, recontra):
    context.driver.find_element(
        By.ID, 'examplePasswordInput').send_keys(contra)
    context.driver.find_element(
        By.ID, 'exampleRepeatPasswordInput').send_keys(recontra)


@when(u'oprimo el botón Guardar Responsable')
def step_impl7(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="content"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/form/button').click()
    time.sleep(1)


@then(u'la página me envia a la url "{url}"')
def step_impl8(context, url):
    assert url == "http://localhost:8000/home_case"


@then(u'puedo ver el error "{esperado}"')
def step_impl8(context, esperado):
    time.sleep(3)
    mensajes = context.driver.find_element(By.CLASS_NAME, 'errorlist')
    mensaje = mensajes.find_element(By.CLASS_NAME, 'errorlist').text
    assert esperado == mensaje, mensaje
