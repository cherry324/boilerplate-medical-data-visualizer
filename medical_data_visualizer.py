import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import math

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
#df['overweight'] = (df['weight']/math.sqrt(df['height']//100).astype(int))>25
df['overweight']=(df['weight'] / ((df['height'] / 100)**2) > 25).astype(int)
print(df['overweight'])

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


# Draw Categorical Plot
def draw_cat_plot():
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=[
            'active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'
        ])
    # print(df_cat)

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat = pd.DataFrame(
        df_cat.groupby(['cardio', 'variable',
                        'value'])['value'].count()).rename(columns={
                            'value': 'total'
                        }).reset_index()
    # print(df_cat)

    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='bar')

    fig = g.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig



# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None,None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    #fig.savefig('heatmap.png')
    return fig
