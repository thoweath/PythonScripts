from app import app
from flask import render_template, Markup
from app import benford
from app import choromap
from app import bokehElement
from app import simpleBokehServerStreamScraper
from bokeh.client import pull_session
from plotly.offline import plot
from bokeh.embed import autoload_server

@app.route('/')
def index():
    session = pull_session(app_path='/simpleBokehServerStreamScraper')
    bokehServer = autoload_server(None,app_path="/simpleBokehServerStreamScraper", session_id=session.id)
    return render_template('TestDashboardTemplate.html',BenfordsLaw=Markup(plot(benford.benford_fig, output_type='div'))
    ,choromap=Markup(plot(choromap.choromap, output_type='div')),
    bokehElementScript=bokehElement.script,bokehElementDiv=bokehElement.div,cdn_js=bokehElement.cdn_js,cdn_css=bokehElement.cdn_css,
    # bokehServerScript=simpleBokehServerStreamScraper.script, bokehServerDiv=simpleBokehServerStreamScraper.div,
    # wscript=simpleBokehServer4.wscript,wdiv=simpleBokehServer4.wdiv,
    bokehServer=bokehServer
    # wscript=simpleBokehServerStreamScraper.wscript,wdiv=simpleBokehServerStreamScraper.wdiv
    )
