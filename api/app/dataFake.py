from faker import Faker
import random
import string

# Configuración de Faker para español
fake = Faker('es_ES')

# Nombre del archivo SQL
filename = 'datos_falsos.sql'

# Más categorías, géneros, mecánicas y plataformas
categorias = [
    'Acción', 'Aventura', 'Deportes', 'Estrategia', 'Simulación', 
    'Rol', 'Puzzle', 'Horror', 'Aventura gráfica', 'Educativo'
]

generos = [
    'FPS', 'RPG', 'MOBA', 'Plataformas', 'Sandbox', 
    'Táctico', 'De construcción', 'De cartas', 'De supervivencia', 
    'De carreras', 'Aventura gráfica', 'Horror de supervivencia', 'MOBA'
]

mecanicas = [
    'Un jugador', 'Multijugador', 'Cooperativo', 'Competitivo', 
    'Online', 'Offline', 'Realidad aumentada', 'Realidad virtual'
]

plataformas = [
    'PC', 'PlayStation', 'Xbox', 'Switch', 'Mac', 'Linux', 
    'iOS', 'Android', 'VR', 'Web'
]

# Función para generar un código de producto de 8 caracteres
def generate_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

# Función para generar datos falsos
def generate_fake_data():
    return (
        generate_code(),                         # codigo_producto
        fake.word(),                             # nombre
        fake.text(max_nb_chars=200),             # descripcion
        round(random.uniform(10.0, 100.0), 2),   # precio
        random.choice(categorias),                # categoria
        random.choice(generos),                   # genero
        fake.date_this_decade().strftime('%Y-%m-%d'),  # fecha_lanzamiento (formato YYYY-MM-DD)
        random.choice(plataformas),               # plataforma
        random.choice(mecanicas)                  # mecanica
    )

# Crear archivo SQL y escribir sentencias
with open(filename, mode='w', encoding='utf-8') as file:
    num_records = 10  # Número de registros a generar
    
    # Escribir la sentencia INSERT INTO
    file.write("INSERT INTO bodega.videojuego (\n")
    file.write("    codigo_producto, nombre, descripcion, precio, categoria, \n")
    file.write("    genero, fecha_lanzamiento, plataforma, mecanica\n")
    file.write(") VALUES\n")
    
    values_list = []

    for _ in range(num_records):
        data = generate_fake_data()
        # Verificar el número de elementos en data
        if len(data) != 9:
            raise ValueError(f"Se esperaban 9 elementos en la tupla, pero se obtuvieron {len(data)}: {data}")

        # Formatear valores asegurando que las comillas y los caracteres especiales se manejen correctamente
        sql_values = (
            f"('{data[0].replace('\'', '\\\'')}', "
            f"'{data[1].replace('\'', '\\\'')}', "
            f"'{data[2].replace('\'', '\\\'')}', "
            f"{data[3]}, "
            f"'{1}', "
            f"'{data[5].replace('\'', '\\\'')}', "
            f"'{data[6]}', "
            f"'{data[7]}', "
            f"'{data[8]}')"
        )
        values_list.append(sql_values)
    
    # Unir todos los valores en una sola línea o en varias líneas separadas por comas
    file.write(",\n".join(values_list))
    file.write(";\n")

print(f'Sentencia INSERT INTO generada en el archivo {filename}.')
