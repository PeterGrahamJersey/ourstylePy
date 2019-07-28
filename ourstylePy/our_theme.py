# Custom Plotly Theme
import plotly.graph_objects as go
import plotly.io as pio
from ourstylePy import our_colours, our_palettes

#pio.templates["our_theme"] = go.layout.Template(

our_theme = go.layout.Template(
    layout = go.Layout(
        # -- Font Anotations --
        font ={
            'color': our_colours.our_colors('text'),
            'family': 'Lato, Sans'
        },
        title={'x': 0.05},
        hoverlabel = {'align': 'left'},
        hovermode = 'closest',
        annotationdefaults = {'arrowcolor': our_palettes.our_palettes('default', 1), 'arrowhead': 0, 'arrowwidth': 1}, # Plotly White
        shapedefaults = {'line': {'color': our_palettes.our_palettes('default', 1)}}, # E.g. vertical lines
        # -- Colours for Data --
        colorscale = {'diverging': [[0, '#8e0152'], [0.1, '#c51b7d'], [0.2, # Plotly White
                                     '#de77ae'], [0.3, '#f1b6da'], [0.4, '#fde0ef'],
                                     [0.5, '#f7f7f7'], [0.6, '#e6f5d0'], [0.7,
                                     '#b8e186'], [0.8, '#7fbc41'], [0.9, '#4d9221'],
                                     [1, '#276419']],
                       'sequential': [[0.0, '#0d0887'], [0.1111111111111111, # Plotly White
                                      '#46039f'], [0.2222222222222222, '#7201a8'],
                                      [0.3333333333333333, '#9c179e'],
                                      [0.4444444444444444, '#bd3786'],
                                      [0.5555555555555556, '#d8576b'],
                                      [0.6666666666666666, '#ed7953'],
                                      [0.7777777777777778, '#fb9f3a'],
                                      [0.8888888888888888, '#fdca26'], [1.0,
                                      '#f0f921']],
                       'sequentialminus': [[0.0, '#0d0887'], [0.1111111111111111, # Plotly White
                                           '#46039f'], [0.2222222222222222, '#7201a8'],
                                           [0.3333333333333333, '#9c179e'],
                                           [0.4444444444444444, '#bd3786'],
                                           [0.5555555555555556, '#d8576b'],
                                           [0.6666666666666666, '#ed7953'],
                                           [0.7777777777777778, '#fb9f3a'],
                                           [0.8888888888888888, '#fdca26'], [1.0,
                                           '#f0f921']]},
        colorway = our_palettes.our_palettes('default'),
        # -- Axes --
        xaxis = {'automargin': True,
                  'gridcolor': our_colours.our_colors('grid'),
                  'linecolor': our_colours.our_colors('grid'),
                  'ticks': '',
                  'zerolinecolor': our_colours.our_colors('grid'),
                  'zerolinewidth': 2,
                  'title':{'xanchor':'left'}
        },
        yaxis = {'automargin': True,
                  'gridcolor': our_colours.our_colors('grid'),
                  'linecolor': our_colours.our_colors('grid'),
                  'ticks': '',
                  'zerolinecolor': our_colours.our_colors('grid'),
                  'zerolinewidth': 2
        },
        polar = dict(
            {
                axis:{'gridcolor': our_colours.our_colors('grid'), 'linecolor': our_colours.our_colors('grid'), 'ticks': ''}
                for axis in ['angularaxis', 'radialaxis']
            },
            bgcolor = 'white'
        ),
        scene = { # 3D plots
            axis:{
                'backgroundcolor': 'white',
                'gridcolor': our_colours.our_colors('grid1'),
                'gridwidth': 2,
                'linecolor': our_colours.our_colors('grid'),
                'showbackground': True,
                'ticks': '',
                'zerolinecolor': our_colours.our_colors('grid')
            } for axis in ['xaxis', 'yaxis', 'zaxis']
        },
        ternary = dict( # Triangle shaped plots
            {
                axis:{'gridcolor': our_colours.our_colors('grid1'), 'linecolor': our_colours.our_colors('grid'), 'ticks': ''}
                for axis in ['aaxis', 'baxis', 'caxis']
            },
            bgcolor='white'
        ),
        # Background
        paper_bgcolor = 'white',
        plot_bgcolor = 'white',
    )
)
