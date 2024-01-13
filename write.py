import pandas as pd
from datetime import datetime

def display_meter(value):
    # Mapping the input value to box characters
    box_characters = ['_', '▁', '▂', '▃', '▄', '▅', '▆', '▇', '█']
    index = min(int(value), len(box_characters) - 1)
    return box_characters[index]

def update_health_data():
    # Read existing data from the CSV file using pandas
    try:
        df = pd.read_csv('health.csv', parse_dates=['date'])
    except FileNotFoundError:
        # If the file doesn't exist, create an empty DataFrame
        df = pd.DataFrame(columns=['date', 'calm', 'joy', 'unified', 'reflection', 'healing', 'community', 'generosity', 'effort', 'patience', 'clarity'])

    # Get today's date as a datetime object
    today = datetime.now()

    # Check if today's date already exists in the data
    if today in df['date'].values:
        print("You've already entered data for today. Exiting...")
        return

    # Collect input from the user
    new_entry = {'date': today}
    health_variables = ['calm', 'joy', 'unified', 'reflection', 'healing', 'community', 'generosity', 'effort', 'patience', 'clarity']
    df[health_variables] = df[health_variables].astype(int)

    print("Hello! Welcome to healthmonitor, and may you be happy-minded.")
    print("mode: w\n")
    print("... ~~~ Hover your hand above the numbers, and press what feels right:\n")

    for variable in health_variables:
        value = input(f"{variable}? > ")
        new_entry[variable] = int(value)
        print(display_meter(value))

    # Append the new entry to the DataFrame
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    # Write the updated data back to the CSV file using pandas
    df.to_csv('health.csv', index=False)

    print("\nWell done! Your health is worth reflecting on, and may it blossom!")

if __name__ == "__main__":
    update_health_data()
