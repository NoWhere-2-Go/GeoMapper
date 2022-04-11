from flask import Flask, render_template, request, send_file
from geopy.geocoders import Nominatim
import pandas
from web_functions import create_map

app = Flask(__name__)


# this will be the ugly base web page
@app.route('/')
def base_page():
    return render_template("base_page.html")


# will display the new .cvs file once user submits their own .cvs file
# this file will contain the longitude and latitude though
@app.route('/success-table', methods=['POST'])
def success_table():
    geo = Nominatim(user_agent="GeoMapper")
    if request.method == "POST":
        file = request.files['file']
        try:
            # noinspection PyTypeChecker
            df = pandas.read_csv(file)
            gc = geo.scheme('http')
            df["coordinates"] = df["Address"].apply(gc.geocode)
            df['Latitude'] = df['coordinates'].apply(lambda x: x.latitude if x != None else None)
            df['Longitude'] = df['coordinates'].apply(lambda x: x.longitude if x != None else None)
            df = df.drop("coordinates", 1)
            create_map(df)
        except Exception as exp:
            return render_template("base_page.html", text=exp)


@app.route("/download-file/")
def download_map():
    return send_file('Map1.html', attachment_filename='your_map.csv', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
