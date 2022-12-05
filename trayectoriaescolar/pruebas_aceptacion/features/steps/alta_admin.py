from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given(u'que ingreso a la url "{url}"')
def step_impl1(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)
    time.sleep(2)

@given(u'en la sección de inicio de sesión agrego los datos "{usuario}" y contra "{contrasenia}"')
def step_impl2(context, usuario, contrasenia):
    context.driver.find_element(By.ID, 'id_username').send_keys(usuario)
    context.driver.find_element(By.ID, 'id_password').send_keys(contrasenia)
    context.driver.dind_element(By.XPATH, '/html/body/div/div/div/div/div/div/div[2]/div/form/button').click()
    
@given(U' luego ingreso a la url {url}')
def step_impl3(context, url):
    context.driver.get(url)

@given(u'en la sección de registro agrego los datos nombre "{nombre}",')
def step_impl4(context, nombre):
    context.driver.find_element(By.NAME, 'username').send_keys(nombre)
    time.sleep(2)


@given(u'correo "{corr}", contraseña "{contra}" y confirmar "{conf}"')
def step_impl5(context, corr, contra, conf):
    context.driver.find_element(By.NAME, 'email').send_keys(corr)
    context.driver.find_element(By.NAME, 'password').send_keys(contra)
    context.driver.find_element(By.NAME, 'repassword').send_keys(conf)
    time.sleep(2)


@when(u'presiono el botón Registrar')
def step_impl6(context):
    context.driver.find_element(
        By.XPATH, '/html/body/div/div/div/div/div[2]/div/form/div/div/button').click()
    time.sleep(2)


@then(u'la página me manda a la url "{url}"')
def step_impl7(context, url):
    assert url == "http://127.0.0.1:8000/login"


@then(u'puedo ver un mensaje de error "{esperado}"')
def step_impl8(context, esperado):
    mensajes = context.driver.find_element(By.CLASS_NAME, 'errorlist')
    mensaje = mensajes.find_element(By.CLASS_NAME, 'errorlist').text
    assert esperado == mensaje, mensaje
