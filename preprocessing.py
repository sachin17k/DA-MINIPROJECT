import pandas as pd

def preprocess_data(df):
    df = df.copy()

    # Handle missing values
    df.dropna(inplace=True)

    # Create Delay column
    df['Delay'] = df['Actual_Time_hr'] - df['Expected_Time_hr']

    # Create Delivery Status (Target)
    df['Delivery_Status'] = df['Delay'].apply(lambda x: "Delayed" if x > 0 else "On-Time")

    return df