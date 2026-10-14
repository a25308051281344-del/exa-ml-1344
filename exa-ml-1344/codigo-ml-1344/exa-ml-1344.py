
# Examen de Machine Learning con Pandas
# NC 1344
# Numero de lista: 29

import os
import io
import importlib.util
import pandas as pd

print("EXAMEN DE MACHINE LEARNING - NC 1344")
print("Version de Pandas:", pd.__version__)

# Cargar diccionario
carpeta_proyecto = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

ruta_diccionario = os.path.join(
    carpeta_proyecto,
    "datos-de-entrada-ml-1344",
    "dicc-1344.py"
)

spec = importlib.util.spec_from_file_location(
    "diccionario", ruta_diccionario
)
diccionario = importlib.util.module_from_spec(spec)
spec.loader.exec_module(diccionario)

# Crear DataFrame
df = pd.DataFrame(diccionario.datos_asignaturas)

# Preparar reporte
reporte = [
    "# Resultados del examen de Machine Learning",
    "",
    "**NC:** 1344",
    "**Numero de lista:** 29",
    ""
]

def registrar(titulo, resultado):
    print(f"\n--- {titulo} ---")
    print(resultado)

    reporte.extend([
        f"## {titulo}",
        "",
        "```text",
        str(resultado),
        "```",
        ""
    ])

# 1. Mostrar todos los datos
registrar("1. Datos de asignaturas", df)

# 2. Mostrar las primeras dos filas
registrar("2. Primeras dos filas", df.head(2))

# 3. Mostrar las ultimas dos filas
registrar("3. Ultimas dos filas", df.tail(2))

# 4. Mostrar dimensiones
registrar("4. Dimensiones (filas, columnas)", df.shape)

# 5. Mostrar tipos de datos
registrar("5. Tipos de datos", df.dtypes)

# 6. Mostrar informacion general
buffer = io.StringIO()
df.info(buf=buffer)
registrar("6. Informacion general", buffer.getvalue())

# 7. Estadisticas de horas por semana
registrar(
    "7. Estadisticas de horas por semana",
    df["Horas_semana"].describe()
)

# 8. Orden ascendente
registrar(
    "8. Orden ascendente por horas",
    df.sort_values(by="Horas_semana")
)

# 9. Orden descendente
registrar(
    "9. Orden descendente por horas",
    df.sort_values(
        by="Horas_semana",
        ascending=False
    )
)

# Guardar reporte
carpeta_resultados = os.path.join(
    carpeta_proyecto,
    "resultados-1344"
)
os.makedirs(carpeta_resultados, exist_ok=True)

ruta_reporte = os.path.join(
    carpeta_resultados,
    "resultados-ml-1344.md"
)

with open(ruta_reporte, "w", encoding="utf-8") as archivo:
    archivo.write("\n".join(reporte))

print("\nReporte creado correctamente:")
print(ruta_reporte)
print("\nEXAMEN TERMINADO")
