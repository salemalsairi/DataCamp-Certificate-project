import pandas as pd
import numpy as np
import random


np.random.seed(42)
random.seed(42)


def create_synthetic_data(num_rows, is_main=False):
    data = {
        'house_id': range(1000000, 1000000 + num_rows),
        'city': np.random.choice(['Silvertown', 'Riverford', 'Teasdale', 'Poppleton', '--'], num_rows,
                                 p=[0.3, 0.3, 0.2, 0.15, 0.05]),
        'sale_date': ['2023-01-05' if random.random() > 0.1 else np.nan for _ in range(num_rows)],
        'months_listed': [round(random.uniform(1.0, 12.0), 1) if random.random() > 0.05 else np.nan for _ in
                          range(num_rows)],
        'bedrooms': [random.randint(1, 6) if random.random() > 0.05 else np.nan for _ in range(num_rows)],
        'house_type': np.random.choice(['Detached', 'Semi-detached', 'Terraced', 'Det.', 'Semi', 'Terr.', np.nan],
                                       num_rows),
    }


    if is_main:
        data['area'] = [f"{round(random.uniform(50.0, 300.0), 1)} sq.m." if random.random() > 0.05 else np.nan for _ in
                        range(num_rows)]
    else:
        data['area'] = [round(random.uniform(50.0, 300.0), 1) if random.random() > 0.05 else np.nan for _ in
                        range(num_rows)]


    prices = []
    for i in range(num_rows):
        if random.random() > 0.1:
            base_price = 100000
            area_val = float(str(data['area'][i]).replace(' sq.m.', '')) if pd.notna(data['area'][i]) else 150.0
            beds = data['bedrooms'][i] if pd.notna(data['bedrooms'][i]) else 3
            prices.append(round(base_price + (area_val * 1000) + (beds * 20000) + random.uniform(-15000, 15000), 2))
        else:
            prices.append(np.nan)

    data['sale_price'] = prices
    return pd.DataFrame(data)



df_main = create_synthetic_data(1500, is_main=True)
df_main.to_csv('house_sales.csv', index=False)


df_train = create_synthetic_data(800, is_main=False)
df_train.to_csv('train.csv', index=False)


df_val = create_synthetic_data(300, is_main=False)
df_val.to_csv('validation.csv', index=False)

