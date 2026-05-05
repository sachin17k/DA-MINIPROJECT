import pandas as pd
from preprocessing import preprocess_data
from analysis import analyze_data
from visualization import *

# Load dataset
df = pd.read_csv("supply_chain_data.csv")

# Preprocess
df = preprocess_data(df)

# Analysis
analyze_data(df)

# Visualizations
plot_delivery_status(df)
plot_delay_bar(df)
plot_cost_vs_distance(df)