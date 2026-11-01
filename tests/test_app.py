"""Pruebas con unittest: no se necesitan bibliotecas externas."""
import unittest
from datetime import datetime, timezone
from src.app import generar_informe


class InformeTests(unittest.TestCase):
    def test_cuenta_activos(self) -> None:
        resultado = generar_informe([
            {"activo": True}, {"activo": False}, {"activo": True},
        ])
        self.assertIn("## (2 activos)", resultado)

    def test_anio_y_vacios(self) -> None:
        resultado = generar_informe([])
        self.assertIn(f"INFORME {datetime.now(timezone.utc).year}", resultado)
        self.assertTrue(resultado.endswith("(0 activos)"))


if __name__ == "__main__":
    unittest.main()
