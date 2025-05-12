# Importacion de las librerias
import pandas as pd
import matplotlib.pyplot as plt

# Declaracion de globales
url_1 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url_2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url_3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url_4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

store_1 = pd.read_csv(url_1)
store_2 = pd.read_csv(url_2)
store_3 = pd.read_csv(url_3)
store_4 = pd.read_csv(url_4)

stores = {'Store_1': store_1, 'Store_2': store_2, 'Store_3': store_3, 'Store_4': store_4}


# DEfinicion de funciones

def show_data_in_bars():
    for bar in bars:
        bar_height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width()/2, 
            bar_height + 1, 
            f'$ {bar_height:.2f}', 
            ha='center', 
            va='bottom', 
            fontsize=10
        )

def titles_in_graphic(title = 'Titulo', title_x_axis = 'Eje x', title_y_axis = 'Eje y'):
    plt.title(title)
    plt.xlabel(title_x_axis)
    plt.ylabel(title_y_axis)
    plt.xticks(rotation=45)


# Flujo principal

# Analisis de facturacion
total_billing = {name_store: sum(df['Precio']) for name_store, df in stores.items()}
total_billing_df = pd.DataFrame(list(total_billing.items()), columns=['Tienda', 'Facturacion'])

plt.figure(figsize=(15, 6))

colors = ['#d4cdc5', '#5b88a5', '#191013', '#243a69']

bars = plt.bar(total_billing.keys(), total_billing.values(), color=colors)

titles_in_graphic('Facturación total por tienda', 'Tienda', 'Total Facturado')

show_data_in_bars()

print(f'Ingresos de las tiendas\n{total_billing_df}\n')


# Ventas por categoria

sales_by_category = {}

# Agrupando los datos por categoria y almacenando en diccionario
for name_store, df in stores.items():
    count = df['Categoría del Producto'].value_counts()
    sales_by_category[name_store] = count

# Se crea el DataFrame y se llenan los espacios sin datos existentes con 0, todos los datos deben ser enteros
sales_by_category_df = pd.DataFrame(sales_by_category)
sales_by_category_df = sales_by_category_df.fillna(0).astype(int)

colors=['#e9f0c9', '#cde54e', '#3b657a', '#20130a']

ax = sales_by_category_df.plot(kind='bar', figsize=(15, 6), color=colors)

titles_in_graphic('Ventas por categoría en cada tienda', 'Categoría del Producto', 'Cantidad de productos vendidos')
plt.legend(title='Tienda', loc = 'upper left', bbox_to_anchor=(1.0, 1.0), fontsize='small', title_fontsize='medium')

for container in ax.containers:
    for bar in container:
        height = bar.get_height()
        if height > 0:
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                height + 0.5,
                str(int(height)),
                ha='center',
                va='bottom',
                fontsize=8
            )
print(f'Ventas por categoría\n{sales_by_category_df}\n')   


plt.tight_layout()
plt.show()