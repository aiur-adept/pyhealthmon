import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

# Read the CSV file
df = pd.read_csv("health.csv", parse_dates=["date"])

# Select only the health variables columns
health_variables = df.columns[1:]

# Set up the matplotlib figure
plt.figure(figsize=(12, 8))

# Plot normal distribution approximations for each health variable
for variable in health_variables:
    # Plot normal distribution curve
    mu, std = df[variable].mean(), df[variable].std()
    x = np.linspace(df[variable].min(), df[variable].max(), 100)
    p = norm.pdf(x, mu, std)
    
    # Plot the curve
    plt.plot(x, p, label=variable, linewidth=2)

    # Add a line from the curve to the legend
    plt.annotate(variable, xy=(mu, 0), xytext=(mu, 0.01),
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 horizontalalignment='center', verticalalignment='bottom')

# Add legend and labels
plt.legend()
plt.xlabel("Health Variable Values")
plt.ylabel("Density")
plt.title("Normal Distribution Approximations for Health Variables")

# Show the plot
plt.show()

