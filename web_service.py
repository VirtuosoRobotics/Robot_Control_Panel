from flask import *
import subprocess,signal,os,time

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/status')
def status():
    f = open( os.getenv("HOME") +"/status.txt", "r")
    return(f.read(1))

@app.route('/start_slam')
def start_slam():
    f = open( os.getenv("HOME") +"/status.txt", "w")
    f.write('2')
    return('start slam')

@app.route('/start_navigatoin')
def start_navigatoin():
    map_name = request.args.get('map_name')
    print('start navigation with ' + map_name)
    f = open( os.getenv("HOME") +"/status.txt", "w")
    f.write('2')
    return('start navigation')

@app.route('/choose_map')
def choose_map():
    f = open( os.getenv("HOME") +"/status.txt", "w")
    f.write('1')
    return('choose map')

@app.route('/map_options')
def map_options():
    map_list = []
    for r,d,f in os.walk(os.getenv("HOME")+'/maps'):
        for map_name in f:
            if '.yaml' in map_name:
                map_name = map_name[0:-5]
                map_list.append(map_name)
    map_list = sorted(map_list,reverse=True)
    options = ''
    for map_name in map_list:
        options = options + '<option value="' + map_name + '">' + map_name + '</option>' 
    return(options)

@app.route('/save_data')
def save_data():
    map_name = request.args.get('map_name')
    print(map_name)
    return('save data')
    
@app.route('/exit')
def exit():
    f = open( os.getenv("HOME") +"/status.txt", "w")
    f.write('0')
    return('exit')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
