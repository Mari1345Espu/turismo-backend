from django.test import TestCase

class SafeDummyTestCase(TestCase):
    def __init__(self):
        super().__init__(methodName='__init__')

def before_scenario(context, scenario):
    context.test = SafeDummyTestCase()
    context.test._pre_setup()  # esto SÍ funciona como instancia
    context.client = context.test.client  # acceso al APIClient

def after_scenario(context, scenario):
    context.test._post_teardown()
