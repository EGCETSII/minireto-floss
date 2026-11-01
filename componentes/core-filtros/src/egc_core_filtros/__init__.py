"""Utilidades para filtrar registros (licencia: consulte el paquete)."""

def contar_activos(registros: list[dict[str, object]]) -> int:
    return sum(1 for registro in registros if registro.get("activo", False))
