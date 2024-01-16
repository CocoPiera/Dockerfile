from flask import Flask

# Init flash APP
app = Flask(__name__)

# main
@app.route( '/', methods=['GET','POST'])
def main():
    return 'Hello World'


@app.route( '/hetic', methods=['GET','POST'])
def main_hetic():
    return 'Hello World Hetic'

if __name__ == '__main__':
    app.run("0.0.0.0", port=80)