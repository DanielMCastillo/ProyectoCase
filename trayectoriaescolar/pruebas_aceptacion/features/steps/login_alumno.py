from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given(u'que ingreso al portal de alumno "{url}"')
def step_impl_alumno_1(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)
    time.sleep(5)


@given(u'escribo mi matricula "{usuario}" y contraseña "{contra}"')
def step_impl_alumno_2(context, usuario, contra):
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(contra)
    time.sleep(5)


@when(u'le doy click al botón Ingresar')
def step_impl_alumno_3(context):
    context.driver.find_element(
        By.XPATH, '/html/body/div/div/div/div/div/div/div[2]/div/form/button').click()


@then(u'puedo ver "{servicios}" en la página principal.')
def step_impl_alumno_4(context, servicios):
    mensaje = context.driver.find_element(
        By.XPATH, '//*[@id="content"]/div/div[2]/div/div[1]/h6').text
    time.sleep(5)
    assert servicios in mensaje, mensaje


@then(u'puedo ver un mensaje "{esperado}"')
def step_impl5(context, esperado):
    mensaje = context.driver.find_element(By.CLASS_NAME, 'alert').text
    assert esperado == mensaje, mensaje
