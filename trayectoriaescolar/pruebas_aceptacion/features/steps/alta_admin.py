from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given(u'que ingreso a la url "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)

@given(u'en la sección de nombre de usuario agregó los datos nombre del administrador "{usuario}",')
def step_impl(context, username):
    context.driver.find_element(By.NAME, 'username').send_keys(username)


@given(u'correo electronico "{correo}", contraseña "{contrasenia}", confirmar "{contrasenia2}"')
def step_impl(context, correo, contrasenia, contrasenia2):
    context.driver.find_element(By.NAME, 'email').send_keys(correo)
    context.driver.find_element(By.NAME, 'password').send_keys(contrasenia)
    context.driver.find_element(By.NAME, 'repassword').send_keys(contrasenia2)


@when(u'presiono el botón "Registrar"')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, 'btn-success').click()


@then(u'puedo ver el mensaje de salida "{esperado}"')
def step_impl(context, esperado):
    mensaje = context.driver.find_element(By.CLASS_NAME, 'alert').text
    assert esperado == mensaje, mensaje
    
    
    

@given(u'que me meto a la url "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)



@given(u'que en la sección de nombre de usuario agrego el nombre "{usuario}",')
def step_impl(context, username):
    context.driver.find_element(By.NAME, 'username').send_keys(username)


@given(u'correo electronico "{correo}", contraseña "{contrasenia}", contraseña2 "{contrasenia2}"')
def step_impl(context, correo, contrasenia, contrasenia2):
    context.driver.find_element(By.NAME, 'email').send_keys(correo)
    context.driver.find_element(By.NAME, 'password').send_keys(contrasenia)
    context.driver.find_element(By.NAME, 'repassword').send_keys(contrasenia2)


@when(u'presiono "Registrar"')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, 'btn-success').click()


@then(u'puedo ver "{esperado}"')
def step_impl(context, esperado):
    mensaje = context.driver.find_element(By.CLASS_NAME, 'alert').text
    assert esperado == mensaje, mensaje
    
    
    
    

@given(u'que me ingreso a "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)



@given(u'que en la sección de nombre de usuario agrego "{usuario}",')
def step_impl(context, username):
    context.driver.find_element(By.NAME, 'username').send_keys(username)


@given(u'en email "{correo}", contraseña "{contrasenia}", contraseña2 "{contrasenia2}"')
def step_impl(context, correo, contrasenia, contrasenia2):
    context.driver.find_element(By.NAME, 'email').send_keys(correo)
    context.driver.find_element(By.NAME, 'password').send_keys(contrasenia)
    context.driver.find_element(By.NAME, 'repassword').send_keys(contrasenia2)


@when(u'presiono el botón con el nombre "Registrar"')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, 'btn-success').click()


@then(u'puedo observar el mensaje de error "{esperado}"')
def step_impl(context, esperado):
    mensaje = context.driver.find_element(By.CLASS_NAME, 'alert').text
    assert esperado == mensaje, mensaje