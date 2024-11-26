# Menu Creator

Este proyecto genera un menú semanal en formato PDF basado en listas de comidas proporcionadas en archivos de texto.

## Estructura del Proyecto

```
.gitattributes
main.py
readme.md
txt_files/
    comidas_con_carne.txt
    comidas_hierro.txt
    comidas_sin_carne.txt
```

## Archivos de Comidas

- `txt_files/comidas_con_carne.txt`: Lista de comidas con carne.
- `txt_files/comidas_hierro.txt`: Lista de comidas ricas en hierro.
- `txt_files/comidas_sin_carne.txt`: Lista de comidas sin carne.

## Uso

Las comidas en los archivos `.txt` son solo ejemplos. Debes reemplazarlas con tus propias listas de comidas.

1. Ejecuta el script `main.py`.
2. Introduce la fecha de inicio del calendario en formato `DD/MM/YYYY`.
3. Introduce el número de semanas que deseas generar.
4. El script generará un archivo `menu_semanal.pdf` con el menú semanal.

## Dependencias

- `pandas`
- `fpdf`

Puedes instalar las dependencias usando pip:

```sh
pip install pandas fpdf
```

## Ejecución

Para ejecutar el script, usa el siguiente comando:

```sh
python main.py
```

## Funcionalidades

- Lee listas de comidas desde archivos de texto.
- Genera un menú semanal aleatorio.
- Crea un archivo PDF con el menú semanal.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que desees realizar.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.