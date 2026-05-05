import matplotlib.pyplot as plt

def plot_delivery_status(df):
    df['Delivery_Status'].value_counts().plot(
        kind='pie', autopct='%1.1f%%'
    )
    plt.title("Delivery Status Distribution")
    plt.ylabel("")
    plt.show()


def plot_delay_bar(df):
    df['Delivery_Status'].value_counts().plot(kind='bar')
    plt.title("On-Time vs Delayed Deliveries")
    plt.xlabel("Delivery Status")
    plt.ylabel("Count")
    plt.show()


def plot_cost_vs_distance(df):
    plt.scatter(df['Distance_km'], df['Transportation_Cost'])
    plt.title("Distance vs Transportation Cost")
    plt.xlabel("Distance (km)")
    plt.ylabel("Cost")
    plt.show()