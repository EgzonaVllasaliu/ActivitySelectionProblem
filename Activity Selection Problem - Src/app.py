from plotly.figure_factory import create_gantt
import server

server.Activities(server.startTime, server.endTime)      

fig = create_gantt(server.df, colors=server.colors, index_col='Resource', title='Activity Selection',
                      show_colorbar=True, show_hover_fill=True, bar_width=0.4, showgrid_x=True, showgrid_y=True)

fig.show()