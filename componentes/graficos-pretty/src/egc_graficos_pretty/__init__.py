"""Renderizado textual mínimo para el ejemplo de EGC."""

def dibujar_barra(longitud: int) -> str:
    return "#" * max(0, longitud)
