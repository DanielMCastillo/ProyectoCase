from django import template


register = template.Library()

@register.filter(name='pertenece_grupo')
def pertenece_grupo(usuario, grupo):
    for gpo in usuario.groups.all():
        if gpo.name == grupo:
            return True
    return False



@register.filter(name='tipo_dato')
def tipo_dato(tipo):
    TIPO_DATO=[
        ('1','text'),
        ('2','number'),
        ('3','decimal'),
        ('4','date'),
        ('5','datetime'),
        ('6','email'),
    ]
    return dict(TIPO_DATO)[tipo]

@register.filter(name='requerido')
def requerido(opcion):
    return 'required' if opcion == '1' else ''