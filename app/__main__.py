from . import web

@web.route('/', methods=['GET'])
def index():
    return 'Hello World!'

@web.route('/test')
def test():
    return 'Test'


if __name__ == '__main__':
    web.run(debug=True) # Dont use debug=True in production