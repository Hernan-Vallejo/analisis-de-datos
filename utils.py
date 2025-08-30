import pandas as pd

def cargar_datos(path: str) -> pd.DataFrame:
    """Carga los datos de ventas desde un CSV"""
    return pd.read_csv(path, parse_dates=["fecha"])

def agregar_columna_total(df: pd.DataFrame) -> pd.DataFrame:
    """Agrega columna con el total de venta (precio * cantidad)"""
    df["total"] = df["precio"] * df["cantidad"]
    return df
