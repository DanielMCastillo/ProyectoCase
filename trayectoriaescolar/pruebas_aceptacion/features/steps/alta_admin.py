from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'que ingreso a la url "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)
    time.sleep(2)

@given(u'en la sección de registro agrego los datos nombre "{nombre}",')
def step_impl(context, nombre):
    context.driver.find_element(By.NAME, 'username').send_keys(nombre)
    time.sleep(2)    

@given(u'correo "{corr}", contraseña "{contra}" y confirmar "{conf}"')
def step_impl(context, corr, contra, conf):
    context.driver.find_element(By.NAME, 'email').send_keys(corr)
    context.driver.find_element(By.NAME, 'password').send_keys(contra)
    context.driver.find_element(By.NAME, 'repassword').send_keys(conf)
    time.sleep(2)

@when(u'presiono el botón Registrar')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/div/form/div[5]/div/button').click()
    time.sleep(2)

@then(u'la página me manda a la url "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)

@then(u'puedo ver un mensaje de error "{esperado}"')
def step_impl2(context, esperado):
    mensajes = context.driver.find_element(By.CLASS_NAME, 'errorlist')
    mensaje = mensajes.find_element(By.CLASS_NAME, 'errorlist').text
    print("HOLAAAAA: ", mensaje)
    assert esperado == mensaje, mensaje