import pandas as pd
from datetime import datetime, timedelta

# Define box characters
box_characters = ['_', '▁', '▂', '▃', '▄', '▅', '▆', '▇', '█']

def read_health_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['date'])
    return df

def calculate_diff(current, previous):
    return current - previous

def display_health_data(df):

    print("mode: r")
    print("~" * 50)
    print("~" * 15, " reflect on the past ", "~" * 15)
    print("~" * 50)

    for variable in df.columns[1:]:
        print(variable)
        values = df[variable].tail(14).tolist()
        diff = int(calculate_diff(values[-1], values[-2]))
        display = ''.join([box_characters[int((len(box_characters) - 1) * (value / 9.0))] for value in values])
        print(display, f"{diff:+d}")

    print("Thank you for taking the time to check in! May you be happy-minded.")

if __name__ == "__main__":
    file_path = "health.csv"
    df = read_health_data(file_path)
    display_health_data(df)
