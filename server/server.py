import json
import ConfigParser
import subprocess
from flask import Flask, request, jsonify, render_template

"""config = ConfigParser.ConfigParser()
config.read('config.ini')
DB_IP = config.get('Database', 'IP', 0)
DB_USER = config.get('Database', 'USER', 0)
DB_PWD = config.get('Database', 'PWD', 0)
DB_NAME = config.get('Database', 'NAME', 0)
USERNAME = config.get('Signup', 'USERNAME', 0)
"""

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


"""
def connect_db():
    return psycopg2.connect(database=app.config['DB_NAME'],
                            user=app.config['DB_USER'],
                            password=app.config['DB_PWD'],
                            host=app.config['DB_IP'])


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
"""


def check_params(args, keys):
    res = {}

    for key in keys:
        value = args.get(key)
        if value is None:
            raise InvalidUsage('Error key: %s not found' % key)
        res[key] = value
    return res


def check_params_json(json, keys):
    res = {}

    if json is None:
        raise InvalidUsage('Error no inputs')
    for key in keys:
        if key not in json:
            raise InvalidUsage('Error key: %s not found' % key)
        if not json[key]:
            raise InvalidUsage('Error wrong value for key: %s ' % key)
        res[key] = json[key]
    return res

# ALL

@app.route('/', methods=['GET'])
def root():
    return render_template('login.html')

@app.route('/courses', methods=['GET'])
def courses():
    return render_template('courses.html')

@app.route('/folder', methods=['GET'])
def folder():
    return render_template('folder.html')

@app.route('/irc', methods=['GET'])
def irc():
    return render_template('irc.html')

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/createvm', methods=['GET'])
def createvm():
    return render_template('createvm.html')


@app.route('/listvm', methods=['GET'])
def listvm():
    return render_template('listvm.html')

@app.route('/listuser', methods=['GET'])
def listuser():
    return render_template('listUser.html')

@app.route('/createuser', methods=['GET'])
def createuser():
    return render_template('createuser.html')

@app.route('/list_group_doc', methods=['GET'])
def get_list_group_doc():
    inputs = check_params(request.args, ['token'])

    res = { 'tree' : [{
        'type' : "folder",
        'name': "folder1",
        'children': [
            {
                'type': "folder",
                'name': "folder2",
                'children': [
                    {
                        'type': "folder",
                        'name': "images",
                        'children': [
                            {
                            'type': "file",
                            'name': "image3",
                            }, {
                            'type': "file",
                            'name': "image4",
                            }
                        ]
                    },
                    {
                        'type': "folder",
                        'name': "images2",
                        'children': [
                            {
                            'type': "file",
                            'name': "image1",
                            }, {
                            'type': "file",
                            'name': "image2",
                            }
                        ]
                    },
                    {
                        'type': "file",
                        'name': "file3",
                    }
                ]
            },
            {
                'type': "file",
                'name': "file4",
            },
            {
                'type': "file",
                'name': "file5",
            },
            {
                'type': "file",
                'name': "file6",
            },
            {
                'type': "file",
                'name': "file7",
            }
        ]
      }
    ]}
    print(inputs)
    print(res)
    return json.dumps(res)


class Test(object):
    i = 0
    vms = {}


@app.route('/list_vm', methods=['GET'])
def get_list_vm():
    inputs = check_params(request.args, ['token'])
    res = {'list_vm': Test.vms[inputs['token']]}
    print(inputs)
    print(res)
    return json.dumps(res)


@app.route('/connect', methods=['POST'])
def post_connect():
    inputs = check_params_json(request.get_json(), ['user', 'pwd'])
    res = {'token': 'TEST',
            'ok' : '1',
           'type': 'user'}
    print(inputs)
    print(res)
    return json.dumps(res)


@app.route('/create_vm', methods=['POST'])
def post_create_vm():
    inputs = check_params_json(request.get_json(), ['token', 'os',
                                                    'ram', 'proc',
                                                    'hdd_size'])
    cmd = ['sudo', 'docker', 'run', '-d', '-P', '--name',
           'ubuntu_%s' % Test.i, 'eg_sshd']
    subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
    cmd = ['sudo', 'docker', 'port', 'ubuntu_%d' % Test.i, '22']
    output = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
    Test.i += 1
    Test.vms[inputs['token']] = {'os': 'ubuntu_%d' % Test.i,
                                'ip':output,
                                'status': 'launch'}
                                
    res = {'ip': output}
    return json.dumps(res)

# ADMIN


@app.route('/list_accounts', methods=['GET'])
def get_list_accounts():
    inputs = check_params(request.args, ['token'])
    res = {'accounts': [{'name': 'test',
                         'type': 'user'}]}
    print(inputs)
    print(res)
    return json.dumps(res)


@app.route('/get_auth', methods=['GET'])
def get_auth():
    inputs = check_params(request.args, ['token', 'user'])
    res = {'auth': ['SysAdmin', 'Adm']}
    print(inputs)
    print(res)
    return json.dumps(res)


@app.route('/change_pwd', methods=['POST'])
def post_change_pwd():
    inputs = check_params_json(request.get_json(), ['token', 'user', 'pwd'])
    res = {'status': 'ok'}
    print(inputs)
    print(res)
    return json.dumps(res)


@app.route('/create_account', methods=['POST'])
def post_create_account():
    inputs = check_params_json(request.get_json(), ['token', 'user', 'pwd'])
    res = {'status': 'ok'}
    print(inputs)
    print(res)
    return json.dumps(res)


@app.route('/change_auth', methods=['POST'])
def post_change_auth():
    inputs = check_params_json(request.get_json(), ['token', 'user',
                                                    'group', 'auth'])
    res = {'status': 'ok'}
    print(inputs)
    print(res)
    return json.dumps(res)


@app.route('/change_vm', methods=['POST'])
def post_change_vm():
    inputs = check_params_json(request.get_json(), ['token', 'vm', 'status'])
    res = {'status': 'ok'}
    print(inputs)
    print(res)
    return json.dumps(res)


def main(args=None):
    app.run(debug=True)


if __name__ == '__main__':
    main()
