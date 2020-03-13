"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from DataProject import app
import pandas as pd






@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/dataMenu')
def data_menu():
    
    return render_template('DataMenu.html')






def color_negetiv(val):
    color = 'red' if '-' in str(val) else 'green'
    return 'color: %s' % color


def highlight_max(s):
    '''
    highlight the maximum in a Series yellow.
    '''
    is_max = s == s.max()
    return ['background-color: yellow' if v else '' for v in is_max]
    
@app.route('/dataPage1')
def usd_eur():
    df = pd.read_csv('DataProject/datafiles/UsdEur.csv')

    
    df['תאריך'] = pd.to_datetime(df['תאריך'])
    df['שינוי %'] = (df['שינוי %'].str.replace('%', '')).astype('float')
    
    df = df.groupby(df['תאריך'].dt.year)[df.columns].agg('mean').reset_index()

    s = df.style.applymap(color_negetiv,subset=['שינוי %']).apply(highlight_max).format({'שינוי %':'{:.2%}'}).hide_index().render()

    
    return render_template('datapage.html',Table=s,table_title="Usd / Euro")

@app.route('/dataPage2')
def usd_ils():
    df = pd.read_csv('DataProject/datafiles/UsdIls.csv')


    df['תאריך'] = pd.to_datetime(df['תאריך'])
    df['שינוי %'] = (df['שינוי %'].str.replace('%', '')).astype('float')
    
    df = df.groupby(df['תאריך'].dt.year)[df.columns].agg('mean').reset_index()

    s = df.style.applymap(color_negetiv,subset=['שינוי %']).apply(highlight_max).format({'שינוי %':'{:.2%}'}).hide_index().render()
    
    return render_template('datapage.html',Table=s,table_title="Usd / Ils")

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
