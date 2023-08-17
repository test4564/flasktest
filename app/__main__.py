from . import web
import os
@web.route('/', methods=['GET'])
def index():
    return 'Hello World!'

@web.route('/test')
def test():
    return 'Test'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"--Running on port {port}--")
    web.run(debug=True, port=port) # Dont use debug=True in production