# Brian Lesko
# Monty Hall Simulation
# The Monty Hall problem is the classic probability problem where a contestant is presented with three doors.
# Behind one door is a car, and behind the other two are goats. The contestant picks a door, and then the host
# opens one of the other two doors to reveal a goat. The contestant is then given the option to switch doors.


import random
import plotly.express as px
import pandas as pd

# Function to simulate the Monty Hall problem
def monty_hall(switch):
    # Initialize the doors
    doors = ['car', 'goat', 'goat']
    # Shuffle the doors
    random.shuffle(doors)
    # Contestant picks a door
    contestant_pick = random.choice(doors)
    # Host reveals a door
    host_reveal = random.choice([i for i in range(3) if doors[i] == 'goat' and doors[i] != contestant_pick])
    # Contestant switches doors
    if switch:
        contestant_pick = [i for i in range(3) if i != host_reveal and i != doors.index(contestant_pick)][0]
    # Return the result
    return doors[contestant_pick] == 'car'

# Number of simulations
n = 1000
# Run the simulations
switch_results = [monty_hall(True) for i in range(n)]
stay_results = [monty_hall(False) for i in range(n)]

# Create a DataFrame
df = pd.DataFrame({'Switch': switch_results, 'Stay': stay_results})
# Melt the DataFrame
df = df.melt(var_name='Strategy', value_name='Win')
# Group by the strategy and calculate the win rate
df = df.groupby('Strategy')['Win'].mean().reset_index()

# Create a bar chart
fig = px.bar(df, x='Strategy', y='Win', text='Win', labels={'Win': 'Win Rate', 'Strategy': 'Strategy'}, title='Monty Hall Simulation')
# Show the chart
fig.show()
