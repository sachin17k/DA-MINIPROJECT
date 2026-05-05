import pandas as pd

def analyze_data(df):
    print("\n--- Basic Analysis ---")

    print("\nAverage Delivery Time:")
    print(df['Actual_Time_hr'].mean())

    print("\nAverage Delay:")
    print(df['Delay'].mean())

    print("\nDelivery Status Count:")
    print(df['Delivery_Status'].value_counts())

    print("\nAverage Transportation Cost:")
    print(df['Transportation_Cost'].mean())