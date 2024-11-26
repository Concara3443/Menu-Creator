import os
import random
import pandas as pd
from fpdf import FPDF
from datetime import datetime, timedelta

# Borrar el archivo menu_semanal.pdf si existe
if os.path.exists("menu_semanal.pdf"):
    os.remove("menu_semanal.pdf")

# Leer listas de comidas desde archivos .txt
def leer_comidas_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]

ComidasHierro = leer_comidas_desde_archivo('txt_files/comidas_hierro.txt')
ComidasConCarne = leer_comidas_desde_archivo('txt_files/comidas_con_carne.txt')
ComidasSinCarne = leer_comidas_desde_archivo('txt_files/comidas_sin_carne.txt')

# Preguntar al usuario la fecha de inicio y el número de semanas
fecha_inicio_str = input("¿Qué día empieza el calendario? (DD/MM/YYYY): ")
num_semanas = int(input("¿Cuántas semanas quieres generar?: "))
fecha_inicio = datetime.strptime(fecha_inicio_str, "%d/%m/%Y")

# Ajustar la fecha de inicio al lunes de esa semana
fecha_inicio_lunes = fecha_inicio - timedelta(days=fecha_inicio.weekday())

# Clase PDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Menú Semanal', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_menu_table(self, menu_df):
        self.set_font('Arial', 'B', 12)
        self.cell(40, 10, 'Día', 1)
        self.cell(150, 10, 'Comida', 1)
        self.ln()
        self.set_font('Arial', '', 12)
        for _, row in menu_df.iterrows():
            self.cell(40, 10, row['Día'], 1)
            self.cell(150, 10, row['Comida'], 1)
            self.ln()

# Crear PDF
pdf = PDF()

for semana in range(num_semanas):
    # Generar menú
    menu = []
    menu.append(random.choice(ComidasHierro))

    num_meat_dishes = random.randint(0, 2)
    if num_meat_dishes > len(ComidasConCarne):
        num_meat_dishes = len(ComidasConCarne)
    menu.extend(random.sample(ComidasConCarne, num_meat_dishes))

    remaining_slots = max(0, min(7 - len(menu), len(ComidasSinCarne)))
    if remaining_slots > len(ComidasSinCarne):
        remaining_slots = len(ComidasSinCarne)
    menu.extend(random.sample(ComidasSinCarne, remaining_slots))

    random.shuffle(menu)

    # Asegurarse de que haya suficientes comidas para llenar toda la semana
    while len(menu) < 7:
        menu.append(random.choice(ComidasSinCarne + ComidasConCarne + ComidasHierro))

    # Crear DataFrame para el menú
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    menu_df = pd.DataFrame({"Día": dias_semana, "Comida": [""] * 7})

    # Ajustar el menú para el día de inicio
    indice_inicio = fecha_inicio.weekday()
    for i in range(len(menu)):
        menu_df.at[(indice_inicio + i) % 7, "Comida"] = menu[i]

    # Dejar en blanco los días antes del día de inicio
    for i in range(indice_inicio):
        menu_df.at[i, "Comida"] = ""

    # Calcular el rango de fechas
    fecha_fin = fecha_inicio_lunes + timedelta(days=6)
    rango_fechas = f"{fecha_inicio_lunes.strftime('%d/%m')} - {fecha_fin.strftime('%d/%m')}"

    # Añadir página al PDF
    pdf.add_page()
    pdf.chapter_title(f'Menú Semanal ({rango_fechas})')
    pdf.add_menu_table(menu_df)

    # Ajustar la fecha de inicio para la siguiente semana
    fecha_inicio_lunes += timedelta(days=7)
    fecha_inicio = fecha_inicio_lunes

# Guardar PDF
pdf.output('menu_semanal.pdf')