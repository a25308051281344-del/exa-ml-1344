# Resultados del examen de Machine Learning

**NC:** 1344
**Numero de lista:** 29

## 1. Datos de asignaturas

```text
    Asignatura  Horas_semana     Profesor
0  Matemáticas             5    Dr. Pérez
1     Historia             3   Dra. López
2     Biología             4     Dr. Ruiz
3      Química             4   Dra. Gómez
4       Física             4     Dr. Díaz
5   Literatura             3  Dra. Torres
```

## 2. Primeras dos filas

```text
    Asignatura  Horas_semana    Profesor
0  Matemáticas             5   Dr. Pérez
1     Historia             3  Dra. López
```

## 3. Ultimas dos filas

```text
   Asignatura  Horas_semana     Profesor
4      Física             4     Dr. Díaz
5  Literatura             3  Dra. Torres
```

## 4. Dimensiones (filas, columnas)

```text
(6, 3)
```

## 5. Tipos de datos

```text
Asignatura        str
Horas_semana    int64
Profesor          str
dtype: object
```

## 6. Informacion general

```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   Asignatura    6 non-null      str  
 1   Horas_semana  6 non-null      int64
 2   Profesor      6 non-null      str  
dtypes: int64(1), str(2)
memory usage: 276.0 bytes

```

## 7. Estadisticas de horas por semana

```text
count    6.000000
mean     3.833333
std      0.752773
min      3.000000
25%      3.250000
50%      4.000000
75%      4.000000
max      5.000000
Name: Horas_semana, dtype: float64
```

## 8. Orden ascendente por horas

```text
    Asignatura  Horas_semana     Profesor
1     Historia             3   Dra. López
5   Literatura             3  Dra. Torres
3      Química             4   Dra. Gómez
2     Biología             4     Dr. Ruiz
4       Física             4     Dr. Díaz
0  Matemáticas             5    Dr. Pérez
```

## 9. Orden descendente por horas

```text
    Asignatura  Horas_semana     Profesor
0  Matemáticas             5    Dr. Pérez
2     Biología             4     Dr. Ruiz
4       Física             4     Dr. Díaz
3      Química             4   Dra. Gómez
1     Historia             3   Dra. López
5   Literatura             3  Dra. Torres
```
