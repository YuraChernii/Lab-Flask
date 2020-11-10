from app import app

@app.route('/api/v1/hello-world-29')
@app.route('/index')
def index():
    return "Hello, World 29"