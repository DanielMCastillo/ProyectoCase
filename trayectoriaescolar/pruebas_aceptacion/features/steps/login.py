from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given(u'que ingreso al sistema en el dominio "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)
    time.sleep(5)


@given(u'escribo mi usuario "{usuario}" y contraseña "{contra}"')
def step_impl(context, usuario, contra):
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(contra)
    time.sleep(5)


@when(u'presiono el botón Ingresar')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '/html/body/div/div/div[2]/form/div[3]/div/button').click()


@then(u'puedo ver mi nombre de usuario "{usuario}" en la página principal.')
def step_impl(context, usuario):
    mensaje = context.driver.find_element(By.TAG_NAME, 'h2').text
    time.sleep(5)
    assert usuario in mensaje, mensaje


@then(u'puedo ver el mensaje "{esperado}"')
def step_impl(context, esperado):
    mensaje = context.driver.find_element(By.CLASS_NAME, 'alert').text
    assert esperado == mensaje, mensaje
