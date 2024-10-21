# Brian Lesko
# Monty Hall Simulation
# The Monty Hall problem is the classic probability problem where a contestant is presented with three doors.
# Behind one door is a car, and behind the other two are goats. The contestant picks a door, and then the host
# opens one of the other two doors to reveal a goat. The contestant is then given the option to switch doors.

import random
import plotly.express as px
import pandas as pd
import streamlit as st
import time

def monty_hall(switch):
    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)
    contestant_pick = random.randint(0, 2)
    host_reveal = random.choice([i for i in range(3) if doors[i] == 'goat' and i != contestant_pick])
    if switch:
        contestant_pick = [i for i in range(3) if i != contestant_pick and i != host_reveal][0]
    return doors[contestant_pick] == 'car'

st.title('Monty Hall Simulation')

Results = st.empty()
Plot = st.empty()
st.write("The Monty Hall problem is the classic probability problem where a contestant is presented with three doors. Behind one door is a car, and behind the other two are goats. The contestant picks a door, and then the host opens one of the other two doors to reveal a goat. The contestant is then given the option to switch doors.")

n = 2500
switch_results = []
stay_results = []
for i in range(1,n):
  switch_results.append(monty_hall(True))
  stay_results.append(monty_hall(False))
  if i % 1 == 0 or i == n:   
        switch_win_count = switch_results.count(True)
        stay_win_count = stay_results.count(True)
        df = pd.DataFrame({
            'Simulation': list(range(1, i + 1)),
            'Switch Wins': [switch_results[:x].count(True) for x in range(1, i + 1)],
            'Stay Wins': [stay_results[:x].count(True) for x in range(1, i + 1)]
        })
        fig = px.line(df, x='Simulation', y=['Switch Wins', 'Stay Wins'],
                      labels={'value': 'Number of Wins', 'variable': 'Strategy'},
                      title='Monty Hall Simulation - Wins Over Time')
        Plot.plotly_chart(fig)
  time.sleep(0.001)

Results.write('### Switch Win Percentage: {:.2f}%'.format(100 * switch_results.count(True) / n))