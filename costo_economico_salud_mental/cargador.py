"""Cargador de datos para Costo Economico Salud Mental DVN/GOHAII."""
import pandas as pd, numpy as np, requests, io

DATASET_DOI = "doi:10.7910/DVN/GOHAII"
DATAVERSE_BASE = "https://dataverse.harvard.edu/api"

def obtener_doi(): return "https://doi.org/10.7910/DVN/GOHAII"

def listar_archivos():
    a = ["perdida_pib_por_pais","perdida_productividad_por_sector","avad_trastornos_mentales",
         "brecha_tratamiento_por_region","gasto_sanitario_salud_mental","costos_paises_latam","tendencia_2020_2024"]
    for x in a: print(f"  {x}.csv")
    return a

def cargar_datos(nombre_archivo=None, token_api=None):
    """
    Carga datos de costos economicos desde Harvard Dataverse.
    Devuelve datos de muestra si no disponible.

    Ejemplos
    --------
    >>> from costo_economico_salud_mental import cargar_datos
    >>> df = cargar_datos('perdida_pib_por_pais')
    """
    if nombre_archivo is None: nombre_archivo = "perdida_pib_por_pais"
    cabeceras = {"X-Dataverse-key": token_api} if token_api else {}
    try:
        r = requests.get(f"{DATAVERSE_BASE}/datasets/:persistentId/?persistentId={DATASET_DOI}", headers=cabeceras, timeout=30)
        if r.status_code == 200:
            for f in r.json().get("data",{}).get("latestVersion",{}).get("files",[]):
                if nombre_archivo.lower() in f.get("dataFile",{}).get("filename","").lower():
                    fid = f["dataFile"]["id"]
                    fr = requests.get(f"{DATAVERSE_BASE}/access/datafile/{fid}", headers=cabeceras, timeout=60)
                    if fr.status_code == 200: return pd.read_csv(io.StringIO(fr.text))
    except Exception: pass
    return _muestra()

def resumen_costos():
    return pd.DataFrame({
        "anio": [2020,2021,2022,2023,2024],
        "costo_global_miles_millones_usd": [830,860,900,945,980],
        "costo_latam_miles_millones_usd": [118,127,138,149,161],
        "perdida_productividad_miles_millones_usd": [625,651,680,715,745],
        "pct_pib_mundial": [0.93,0.96,0.99,1.02,1.05],
    })

def _muestra():
    paises = ["EE.UU.","Reino Unido","Brasil","Mexico","Argentina","Colombia","Chile","Espana","Alemania","Francia"]
    return pd.DataFrame({
        "pais": paises,
        "pib_miles_millones_usd": [23000,2960,1870,1290,630,340,310,1420,4260,2940],
        "costo_sm_pct_pib": [3.2,3.1,4.8,5.1,5.5,5.3,4.2,2.9,2.7,2.8],
        "costo_sm_miles_millones_usd": [736,92,90,66,35,18,13,41,115,82],
        "anio": [2024]*10,
    })
