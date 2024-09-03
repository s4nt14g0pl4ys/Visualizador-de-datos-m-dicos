import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Importamos el archivo csv
df = pd.read_csv('D:\\USUARIO\\Documents\\Santiago\\FreeCodeCamp\\ProyectosCv\\Visualizador de datos médicos\\medical_examination.csv')

# Calculamos el overweight con la formula de IMC
df['Overweight'] = df['weight']/(df['height']/100)**2

df.loc[df['Overweight'] < 25, 'Overweight' ] = 0
df.loc[df['Overweight'] >= 25, 'Overweight'] = 1

# Normalizando los datos
df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0

df.loc[df['gluc'] > 1, 'gluc'] = 1
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1

def draw_cat_plot():
    df_cat = df[['cholesterol', 'gluc', 'smoke', 'active', 'Overweight', 'cardio']]
    df_cat = pd.melt(df_cat, id_vars=['cardio'], var_name='variable', value_name='value')

    plt.figure(figsize=(10,6))
    sns.catplot(y='value', x='variable', col='cardio', data=df_cat, kind='bar', aspect=1.2)
    plt.show()

def draw_heat_map():
    # Limpiar los datos
    df_heat = df[
        (df['height'] >= df['height'].quantile(0.025)) & 
        (df['height'] <= df['height'].quantile(0.975)) & 
        (df['weight'] >= df['weight'].quantile(0.025)) & 
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calcular la matriz de correlación
    corr = df_heat.corr()

    # Crear una máscara para el triángulo superior
    mask = np.triu(np.ones_like(corr, dtype=np.bool))

    # Configurar la figura de matplotlib
    plt.figure(figsize=(10, 8))

    # Graficar la matriz de correlación
    sns.heatmap(corr, mask=mask, annot=True, cmap='coolwarm', square=True)
    plt.show()
