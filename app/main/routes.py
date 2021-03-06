from flask import flash, redirect, render_template, request, url_for,send_from_directory,current_app
from app.api.routes import SensorListAPI,DataListAPI
from app.main import bp
from flask_restful import Api

@bp.route('/index', methods=['GET', 'POST'])
@bp.route('/', methods=['GET', 'POST'])
def index():
    auth = url_for('main.index',  _external=True)+'api/users'
    return render_template('main/index.html', title='Home',auth=auth)

@bp.route('/relationship', methods=['GET', 'POST'])
def relationship():
    auth = url_for('main.index',  _external=True)+'api/users'
    return render_template('main/relationship.html', title='Relationship',auth=auth)

@bp.route('/chart', methods=['GET', 'POST'])
def chart():
    auth = url_for('main.index',  _external=True)+'api/users'
    sensor = url_for('main.index',  _external=True)+'api/sensors'
    dataset = url_for('main.index',  _external=True)+'api/dataset'
    return render_template('main/chart.html', title='Chart',auth=auth,sensor=sensor,dataset=dataset)

@bp.route('/mannual', methods=['GET', 'POST'])
def mannual():
    auth = url_for('main.index',  _external=True)+'api/users'
    sensor = url_for('main.index',  _external=True)+'api/sensors'
    dataset = url_for('main.index',  _external=True)+'api/dataset'
    return render_template('main/mannual.html', title='mannual',auth=auth,sensor=sensor,dataset=dataset)
    # return render_template('main/mannual.html', title='mannual',tmp=tmp,light=light)

@bp.route('/table', methods=['GET', 'POST'])
def table():
    auth = url_for('main.index',  _external=True)+'api/users'
    sensor = url_for('main.index',  _external=True)+'api/sensors'
    dataset = url_for('main.index',  _external=True)+'api/dataset'
    return render_template('main/table.html', title='Table',auth=auth,sensor=sensor,dataset=dataset)



