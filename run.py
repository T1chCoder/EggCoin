from app import app
import config

def init():
    app.run(debug=config.DEBUG)

if __name__ == '__main__':
    init()