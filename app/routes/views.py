from flask import Blueprint, render_template, redirect, url_for
from app.routes.forms import SearchCity
from app.routes.parse.parse_amindi_ge import parse_amindi_ge





home_blueprint = Blueprint('home',
                           __name__,
                           template_folder='templates',
                           static_folder='static',url_prefix='/')


@home_blueprint.route('/<city>')
def home(city):
    form = SearchCity()
    parse = parse_amindi_ge(city)
    weekly_weather = parse[0]
    cities = parse[1]
    data_today = []




    for today in weekly_weather.items():
        data_today.append(today)

    if city not in cities:
        return 'Not Found'

    return render_template('home.html', form=form, cities=cities,main_city=city,data_today=data_today,weekly_weather=weekly_weather)



@home_blueprint.route('/')
def index():
    return redirect(url_for('home.home', city='თბილისი'))


@home_blueprint.app_errorhandler(404)
def not_found(e):
    return 'Page not found'
