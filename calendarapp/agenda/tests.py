from django.test import TestCase
from .models import Categoria
from django.core.exceptions import ValidationError


class TestCategoria(TestCase):

    def test_grabacion(self):
        with self.assertRaises(ValidationError) as qv:
            q = Categoria.objects.create(titulo='No permitido')
            q.full_clean()

        mensaje_error = dict(qv.exception)
        self.assertEqual(mensaje_error["titulo"][0], "No es una opcion permitida")
