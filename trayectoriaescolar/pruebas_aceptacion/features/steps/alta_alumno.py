from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given(u'que me dirijo a la url "{url}"')
def step_impl1(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)


@given(u'para iniciar sesión ingreso los datos "{usuario}" y contra "{contrasenia}"')
def step_impl2(context, usuario, contrasenia):
    context.driver.find_element(By.ID, 'id_username').send_keys(usuario)
    context.driver.find_element(By.ID, 'id_password').send_keys(contrasenia)
    context.driver.find_element(
        By.XPATH, '/html/body/div/div/div/div/div/div/div[2]/div/form/button').click()


@given(U'luego me dirijo a la url "{url}"')
def step_impl3(context, url):
    context.driver.get(url)


@given(u'en el registro agrego los datos matricula "{matricula}", correo "{correo}"')
def step_impl4(context, matricula, correo):
    time.sleep(3)
    context.driver.find_element(By.ID, 'matricula').send_keys(matricula)
    context.driver.find_element(By.ID, 'correo').send_keys(correo)


@given(u'nombre "{nombre}", segundo nombre "{nombre2}", primer apellido "{apellido1}", segundo apellido "{apellido2}", telefono "{telefono}"')
def step_impl5(context, nombre, nombre2, apellido1, apellido2, telefono):
    context.driver.find_element(By.ID, 'nombre').send_keys(nombre)
    context.driver.find_element(By.ID, 'segundo_nombre').send_keys(nombre2)
    context.driver.find_element(By.ID, 'primer_apellido').send_keys(apellido1)
    context.driver.find_element(By.ID, 'segundo_apellido').send_keys(apellido2)
    context.driver.find_element(By.ID, 'telefono').send_keys(telefono)


@given(u'con los datos contraseña "{contra}" y confirmar "{recontra}"')
def step_impl6(context, contra, recontra):
    context.driver.find_element(
        By.ID, 'examplePasswordInput').send_keys(contra)
    context.driver.find_element(
        By.ID, 'exampleRepeatPasswordInput').send_keys(recontra)


@when(u'oprimo el botón Guardar Alumno')
def step_impl7(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="content"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/form/button').click()
    time.sleep(1)


@then(u'redirige a la url "{url}"')
def step_impl8(context, url):
    assert url == "http://localhost:8000/home"


@then(u'muestra un mensaje de error "{esperado}"')
def step_impl9(context, esperado):
    time.sleep(3)
    mensajes = context.driver.find_element(By.CLASS_NAME, 'errorlist')
    mensaje = mensajes.find_element(By.CLASS_NAME, 'errorlist').text
    assert esperado == mensaje, mensaje
