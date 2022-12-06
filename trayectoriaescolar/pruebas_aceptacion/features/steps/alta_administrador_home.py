from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given(u'que entro a la url "{url}"')
def step_impl1(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)


@given(u'para iniciar sesión ingreso mis credenciales de usuario "{usuario}" y contraseña "{contraseña}"')
def step_impl2(context, usuario, contraseña):
    context.driver.find_element(By.ID, 'id_username').send_keys(usuario)
    context.driver.find_element(By.ID, 'id_password').send_keys(contraseña)
    context.driver.find_element(
        By.XPATH, '/html/body/div/div/div/div/div/div/div[2]/div/form/button').click()


@given(U'luego me muevo a la url "{url}"')
def step_impl3(context, url):
    context.driver.get(url)


@given(u'en el registro lleno los campos usuario "{username}", correo "{correo}"')
def step_impl4(context, username, correo):
    time.sleep(3)
    context.driver.find_element(
        By.XPATH, '//*[@id="username"]').send_keys(username)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(correo)


@given(u'id_password "{contra}" y id_confirmar "{recontra}"')
def step_impl6(context, contra, recontra):
    context.driver.find_element(
        By.XPATH, '//*[@id="examplePasswordInput"]').send_keys(contra)
    context.driver.find_element(
        By.XPATH, '//*[@id="exampleRepeatPasswordInput"]').send_keys(recontra)


@when(u'oprimo el botón Guardar Administrador')
def step_impl7(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="content"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/form/button').click()
    time.sleep(1)


@then(u'redirige a la ruta "{url}"')
def step_impl8(context, url):
    assert url == "http://localhost:8000/home"


@then(u'muestra un mensaje como el siguiente "{esperado}"')
def step_impl9(context, esperado):
    time.sleep(3)
    mensajes = context.driver.find_element(By.CLASS_NAME, 'errorlist')
    mensaje = mensajes.find_element(By.CLASS_NAME, 'errorlist').text
    assert esperado == mensaje, mensaje
