# Hadoop MapReduce con Python Streaming

Este repositorio contiene una colección de scripts en Python diseñados para ejecutar tareas de **MapReduce** utilizando la utilidad **Hadoop Streaming**. El objetivo es procesar un dataset de ventas distribuidas para extraer diversas métricas de negocio.

## Descripción del Dataset

Los ejercicios utilizan un archivo de ventas que registra transacciones individuales.
Cada línea del archivo contiene **5 campos**:

1.  **Fecha** (AAAA-MM-DD)
2.  **Tienda** (Ubicación)
3.  **Categoría** (Tipo de producto)
4.  **Costo** (Importe de la venta)
5.  **Método de Pago**

**Ejemplo de formato:**
```text
2021-11-09 18:27	Ferrol	Hogar	61.92	efectivo
2023-01-24 17:27	Lugo	Ropa	134.85	mastercard
```

## Prerrequisitos
* Acceso a un clúster Hadoop (con YARN y HDFS funcionando).
* Python instalado en los nodos del clúster.
* Los scripts (`mapper.py`, `reducer.py`) deben tener permisos de ejecución (`chmod +x *.py`).
