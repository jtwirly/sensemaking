# -----------------------------------------------
#  7. Data Visualization:
#  Objective: Visualize the word frequencies
#  using a visualization library.
# 
#  Tools/Resources: Examples of visualization 
#  libraries D3, Plotly, and Chart.JS.
#     D3, https://d3js.org/
#     Plotly, https://plotly.com/
#     Chart.JS, https://www.chartjs.org/
#     Google Charts, https://developers.google.com/chart/
# -----------------------------------------------

import plotly.graph_objects as go

# Read in the word frequencies
with open("word_frequencies.txt", "r") as file:
    lines = file.readlines()

# Parse the word frequencies into separate lists for words and counts
words = []
counts = []
for line in lines:
    word, count = line.strip().split(": ")
    words.append(word)
    counts.append(int(count))

# Create a bar chart
fig = go.Figure(data=[go.Bar(x=words, y=counts)])

# Customize the layout
fig.update_layout(
    title="Word Frequencies in Course Titles",
    xaxis_title="Word",
    yaxis_title="Frequency",
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#7f7f7f"
    )
)

# Display the chart
fig.show()