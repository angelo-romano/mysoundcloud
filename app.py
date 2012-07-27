from mysoundcloud.base import app, SoundcloudConnector
#from mysoundcloud.models import Country, City
from flask import render_template

@app.route('/')
def main():
#    countries = Country.query.all()
#    return render_template('country_list.html', countries=countries)
    return 'Ciao Bella'


if __name__ == '__main__':
    app.run(debug=True)
