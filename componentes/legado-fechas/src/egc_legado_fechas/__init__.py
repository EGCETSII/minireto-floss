"""Consulta la fecha del sistema; paquete ficticio sin licencia explícita."""
from datetime import datetime, timezone

def anio_actual() -> int:
    return datetime.now(timezone.utc).year
