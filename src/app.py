"""Aplicación ficticia: usa cuatro componentes de terceros simulados."""
from egc_core_filtros import contar_activos
from egc_graficos_pretty import dibujar_barra
from egc_informe_mit import etiqueta
from egc_legado_fechas import anio_actual


def generar_informe(registros: list[dict[str, object]]) -> str:
    """Resume registros activos en un formato muy sencillo."""
    cantidad = contar_activos(registros)
    return f"{etiqueta(f'informe {anio_actual()}')} {dibujar_barra(cantidad)} ({cantidad} activos)"


if __name__ == "__main__":
    ejemplo = [{"activo": True}, {"activo": False}, {"activo": True}]
    print(generar_informe(ejemplo))
