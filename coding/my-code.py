import pandas as pd
import matplotlib.pyplot as plt

urls = [ "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv",
        "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv",
        "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv",
        "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"
]

sum_stores = []


def sum_by_price():
    count = 0

    for url in urls:
        df = pd.read_csv(url)
        sum_price = df['Precio'].sum()
        sum_stores.append(sum_price)

        print(f'El valor tolar de venta de -> Tienda {count + 1} es: $ {sum_price}\n')
        count += 1

def count_by_category():
    count = 0

    for url in urls:
        df = pd.read_csv(url)
        count_store = df.groupby(['Categoría del Producto'])['Categoría del Producto'].count()
        print(f'La cantidad de ventas por categoria de -> Tienda {count + 1} es: \n{count_store}\n')
        count += 1

def average_by_score():
    count = 0 
    for url in urls:
        df = pd.read_csv(url)
        sum_score = df['Calificación'].sum()
        count_sales = df['Calificación'].count()
        average_score = sum_score / count_sales
        print(f'Cantidad de ventas -> {count + 1}: {count_sales}, Promedio: {average_score}\n')
        count += 1


sum_by_price()
count_by_category()
average_by_score()



# count_store_1 = df_store_1.groupby(['Categoría del Producto'])['Categoría del Producto'].count()

# print(f'{store_1.head()}\n')
# print(f'{count_store_1}\n') 

# def store_sum_store():
#     sum_stores.append(sum_price_store_1)
# total_value_store()



