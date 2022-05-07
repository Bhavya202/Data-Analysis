# Importing Modules
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Initializing Data
df = pd.read_csv("data.csv")
df.sort_values( [df.columns[0], df.columns[1]],
                    axis=0,
                    ascending=[True, True], 
                    inplace=True
                )

# Finding Mean          ---Central Tendancy
student_mean = df.groupby("level")["attempt"].mean()

# Graph Showing Each Student Performing At Each Level
print("Plotting Graph..")
figure = px.scatter(df, 
        y = "level",
        x = "student_id",
        color = "student_id",
        size="attempt",
        size_max=15,
        title="Graph Showing Each Student Performing At Each Level"
    )

# Graph Showing Mean Of All Students Performaing At Each Level
fig = go.Figure(go.Scatter(
                        x = ['Level 1', 'Level 2', 'Level 3', 'Level 4'],
                        y = student_mean,
                        orientation="v"
                        ))

fig.update_layout(
    title='Graph Showing Mean Of All Students Performaing At Each Level',
    plot_bgcolor='rgb(230, 230,230)'
)

# Plotting Graph
figure.show()
fig.show()