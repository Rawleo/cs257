# Main file for Climate Canvas, contains code to run Flask server.

from flask import Flask
from flask import render_template, redirect, request, url_for
import psycopg2
from psycopg2._psycopg import AsIs
import folium
import json

app  = Flask(__name__)
conn = psycopg2.connect(host="localhost",
                        port=5432,
                        database="sigmondm",
                        user="sigmondm",
                        password="pies347cash")
cur = conn.cursor()


@app.route('/', methods=("GET", "POST"))
def welcome():

    if request.method == 'POST':
        abbr = request.form['airports']
        url_to_redirect = "/weather/" + abbr
        return redirect(url_to_redirect)
    
    map = folium.Map(
        location=[38.5, -95],
        control_scale=True,
        zoom_start=4
    )

    atl_html = '''
        <p class="marker">
            ATL Airport Weather Data
        </p>
        <a href='/tables/atl' target='_parent'>ATL Airport Table</a>
    '''
    bos_html = '''
        <p class="marker">
            BOS Airport Weather Data
        </p>
        <a href='/tables/bos' target='_parent'>BOS Airport Table</a>
    '''
    den_html = '''
        <p class="marker">
            DEN Airport Weather Data
        </p>
        <a href='/tables/den' target='_parent'>DEN Airport Table</a>
    '''
    dfw_html = '''
        <p class="marker">
            DFW Airport Weather Data
        </p>
        <a href='/tables/dfw' target='_parent'>DFW Airport Table</a>
    '''
    lax_html = '''
        <p class="marker">
            LAX Airport Weather Data
        </p>
        <a href='/tables/lax' target='_parent'>LAX Airport Table</a>
    '''
    msp_html = '''
        <p class="marker">
            MSP Airport Weather Data
        </p>
        <a href='/tables/msp' target='_parent'>MSP Airport Table</a>
    '''

    folium.Marker(
        location=[33.636667, -84.428056],
        tooltip="ATL Airport",
        popup=atl_html,
        icon=folium.Icon(color="green"),
    ).add_to(map)

    folium.Marker(
        location=[42.36306, -71.00639],
        tooltip="BOS Airport",
        popup=bos_html,
        icon=folium.Icon(color="green"),
    ).add_to(map)

    folium.Marker(
        location=[39.861667, -104.673056],
        tooltip="DEN Airport",
        popup=den_html,
        icon=folium.Icon(color="green"),
    ).add_to(map)

    folium.Marker(
        location=[32.918705, -97.05901],
        tooltip="DFW Airport",
        popup=dfw_html,
        icon=folium.Icon(color="green"),
    ).add_to(map)

    folium.Marker(
        location=[33.9425, -118.408056],
        tooltip="LAX Airport",
        popup=lax_html,
        icon=folium.Icon(color="green"),
    ).add_to(map)

    folium.Marker(
        location=[44.881944, -93.221667],
        tooltip="MSP Airport!",
        popup=msp_html,
        icon=folium.Icon(color="green"),
    ).add_to(map)

    map.get_root().width = "100%"
    map.get_root().height = "400px"

    iframe = map.get_root()._repr_html_()

    return render_template("homepage.html", iframe=iframe)

@app.route('/weather/<city>')
def weather(city):
    sqlTableName = city + "_weather"
    cur.execute("SELECT date, tmax FROM %s ORDER BY tmax DESC", [AsIs(sqlTableName)], )
    row = cur.fetchone()
    while row[1] is None:
        row = cur.fetchone();
    
    return render_template("weather.html", topmonth=row[0], toptemp=row[1])

@app.route('/tables', methods=("GET", "POST"))
def tables():
    if request.method == "POST":
        abbr, sqlTableName, startdate, enddate = get_airport_table(request)
        if request.form['yearb'] != "" and request.form['yeare'] != "":
            startdateformatted, enddateformatted = get_user_date_limits(request)
            html_table = create_html_table(sqlTableName, startdateformatted, enddateformatted)

            return render_template("tables.html",
                                   daterange="Data at " + abbr.upper() + " is available from " + str(
                                       startdate) + " through " + str(enddate), tabledata="Data at " + abbr.upper() + " from " + startdateformatted + " to " + enddateformatted + ":", table_html=html_table)
        else:
            return render_template("tables.html", daterange="Date range will appear here.",
                                   tabledata="Error: Please enter both a start and end date.")
    else:
        return render_template("tables.html", daterange="Date range will appear here.", tabledata="Table will be populated when form is submitted.")

def get_airport_table(request):
    abbr = request.form['airports']
    sqlTableName = abbr + "_weather"
    cur.execute("SELECT * FROM %s ORDER BY date ASC", [AsIs(sqlTableName)])
    row = cur.fetchone()
    startdate = row[0]
    cur.execute("SELECT * FROM %s ORDER BY date DESC", [AsIs(sqlTableName)])
    row = cur.fetchone()
    while row[1] is None:
        row = cur.fetchone()
    enddate = row[0]
    
    return [abbr, sqlTableName, startdate, enddate]

def get_user_date_limits(request):
    startdateformatted = request.form['yearb'] + "-" + request.form['monthb'] + "-01"
    enddateformatted = request.form['yeare'] + "-" + request.form['monthe'] + "-01"

    return [startdateformatted, enddateformatted]

def create_html_table(sqlTableName, startdateformatted, enddateformatted): 
    cur.execute("Select * FROM %s LIMIT 0", [AsIs(sqlTableName)])
    colnames = [desc[0] for desc in cur.description]
    html_table = '''<table class="table"><tr>'''
    for col in colnames:
        html_table += ('''<th id='columnName' onmouseover="hoverDescription('%s')">''' % col) + col.upper() + "</th>"
        # html_table += ("<div class='hideDescription' value=%s>Column description.</div>" % col)
    html_table += "</tr>"
    cur.execute("SELECT * FROM %s WHERE date BETWEEN %s AND %s ORDER BY date DESC",
                [AsIs(sqlTableName), startdateformatted, enddateformatted])
    rows = cur.fetchall()
    for row in rows:
        html_table += "<tr>"
        for item in row:
            html_table += "<td>" + str(item) + "</td>"
        html_table += "</tr>"
    return html_table

@app.route('/tables/<airport>', methods=("GET", "POST"))
def marker_link(airport):
    if len(airport) == 3:
        if request.method == "POST":
            return tables()
        else: 
            obj = airport_daterange(airport)
            startdate = obj[1]
            enddate = obj[2]
            table_html = max_range_table(airport)

            return render_template("tables.html", daterange="Data at " + airport.upper() + " is available from " + str(startdate) + " through " + str(enddate), tabledata="Data at " + airport.upper() + " from " + startdate + " to " + enddate + ":", table_html=table_html)
    else:
        return tables()

@app.route('/lookup/<airport>')
def lookup(airport):
    sqlTableName = airport + "_weather"
    cur.execute("SELECT * FROM %s ORDER BY date ASC", [AsIs(sqlTableName)])
    row = cur.fetchone()
    startdate = str(row[0])
    cur.execute("SELECT * FROM %s ORDER BY date DESC", [AsIs(sqlTableName)])
    row = cur.fetchone()
    while row[1] is None:
        row = cur.fetchone()
    enddate = str(row[0])
    json_answer = {
        "abbr": airport.upper(),
        "startdate": startdate,
        "enddate": enddate
    }
    return json.dumps(json_answer)

@app.route('/columndescription/<columnName>')
def get_column_description(columnName):
    cur.execute("SELECT * FROM gsom_abbr_info WHERE column_abbr = '%s';" % columnName)
    row = cur.fetchall()
    print(row)
    print(columnName)
    print(request.path)
    json_answer = {
        "column":(row[0][0]).upper(),
        "description":row[0][1]
    }
    
    return json.dumps(json_answer)

def airport_daterange(airport):
    sqlTableName = airport + "_weather"
    jsonfile = json.loads(lookup(airport))
    start = jsonfile["startdate"]
    end = jsonfile["enddate"]

    return [sqlTableName, start, end]

def max_range_table(airport):
    sqlTableName, startdateformatted, enddateformatted = airport_daterange(airport)
    html_table = create_html_table(sqlTableName, startdateformatted, enddateformatted, "desc")

    return html_table

@app.route('/about-us')
def about_us():

    return render_template("about-us.html")

if __name__ == '__main__':
    my_port = 5132
    app.run(host='0.0.0.0', port=my_port, debug=True)