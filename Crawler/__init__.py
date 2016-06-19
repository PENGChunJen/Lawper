from flask import Flask
from flask import request
from flask import render_template
from search import search 
import json

app = Flask(__name__)
app.debug = True

@app.route('/')
def my_form():
   #return render_template('index.html')
   return render_template('my_form.html')

@app.route('/', methods=['POST'])
def my_form_post():
       text = request.form['text']
       #print text
       jsons = search(text)
       #print json.dumps(jsons, ensure_ascii=False, encoding='utf8', indent=4)
       json_str = json.dumps(jsons, ensure_ascii=False, encoding='utf8', indent=4)
       results = json.loads(json_str) 
       return render_template('my_form.html', results = results)

if __name__ == '__main__':
   app.run(host='140.112.42.124')
