from flask import Blueprint, render_template,redirect,url_for
from app.routes.forms import SearchCity
from app.routes.parse.parse_amindi_ge import parse_amindi_ge


home_blueprint = Blueprint('home',
                           __name__,
                           template_folder='templates',
                           static_folder='static')

@home_blueprint.route('/<city>')
def home(city):
    form = SearchCity()
    parse = parse_amindi_ge(city)
    data = parse[0]
    cities = parse[1]

    if city not in cities:
        return 'Not found bitch'



    return render_template('home.html', form=form,data=data,cities=cities)

@home_blueprint.route('/')
def index():

    return redirect(url_for('home.home',city='თბილისი'))

@home_blueprint.app_errorhandler(404)
def not_found(e):

    return 'Page not found'
