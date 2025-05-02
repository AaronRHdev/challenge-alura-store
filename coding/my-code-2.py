import pandas as pd
import matplotlib.pyplot as plt

url_1 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url_2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url_3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url_4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

store_1 = pd.read_csv(url_1)
store_2 = pd.read_csv(url_2)
store_3 = pd.read_csv(url_3)
store_4 = pd.read_csv(url_4)

stores = {'Store_1': store_1, 'Store_2': store_2, 'Store_3': store_3, 'Store_4': store_4}

total_billing = {name: sum(df['Precio']) for name, df in stores.items()}
total_billing_df = pd.DataFrame(list(total_billing.items()), columns=['Tienda', 'Facturacion'])

plt.figure(figsize=(8, 5))
bars = plt.bar(total_billing.keys(), total_billing.values(), color='indigo')
plt.bar(total_billing.keys(), total_billing.values(), color='indigo')
plt.title('Facturación total por tienda')
plt.xlabel('Tienda')
plt.ylabel('Total facturado')
plt.xticks(rotation=45)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval:.2f}', ha='center', va='bottom', fontsize=10)



print("Ingresos de las tiendas")
print(total_billing_df)

plt.tight_layout()
plt.show()