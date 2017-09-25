from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="POST">
            <label for="rot">
            Rotate by:
            <input type="text" name="rot" id="rot"/>
            <textarea name ="text" type="text">{0}</textarea>
            <input type= "submit" name="submit"/>
        </label>
    </form>       
    </body>
</html>
"""
@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=['POST'])
def encrypt(): 
    rotation = request.form['rot']
    message = request.form['text']
    rotation = int(rotation)
    message = str(message)
    encryption = rotate_string(message, rotation)
    
    return form.format(encryption) 

app.run()