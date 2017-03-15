from bokeh.plotting import figure
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool, ColumnDataSource
from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.client import pull_session
from bokeh.sampledata.periodic_table import elements

#define ColumnDataSource from elements dataframe
source = ColumnDataSource(elements)

# select the tools we want
TOOLS="pan,wheel_zoom,box_zoom,reset,save,crosshair"

hover = HoverTool(
        tooltips=[
            ("Index", "$index"),
            ("Atomic Mass", "@{atomic mass}"),
            ('Atomic Radius','@{atomic radius}')
        ]
    )


# build our figures
p1 = figure(tools=[hover,TOOLS], plot_width=650, plot_height=372)
p1.scatter('atomic mass', 'atomic radius', size=12, color="red", alpha=0.5,source=source)
p1.line('atomic mass','atomic radius',color='blue', source=source)

#p1.add_tools(HoverTool())

script, div = components(p1)

cdn_css = CDN.css_files[0]
cdn_js = CDN.js_files[0]
