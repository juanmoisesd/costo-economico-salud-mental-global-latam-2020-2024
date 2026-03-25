"""
costo-economico-salud-mental
========================================
DOI: https://doi.org/10.7910/DVN/GOHAII
Autor: Juan Moises de la Serna (ORCID: 0000-0002-8401-8018)

Uso:
    from costo_economico_salud_mental import cargar_datos, resumen_costos
    df = cargar_datos('perdida_pib_por_pais')
"""
from .cargador import cargar_datos, listar_archivos, resumen_costos, obtener_doi
__version__ = "1.0.0"
__doi__ = "10.7910/DVN/GOHAII"
__autor__ = "Juan Moises de la Serna"
__all__ = ["cargar_datos","listar_archivos","resumen_costos","obtener_doi"]
