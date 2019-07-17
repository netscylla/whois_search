from flask import  Response
from app.forms import WhoisForm
from app import app
from flask_bootstrap import Bootstrap
from whois import whois_search
from flask import Flask, request, render_template, jsonify
import json

@app.route('/', methods=["GET"])
def index():
  form = WhoisForm()
  return render_template('form.html', title='Whois Search', form=form)

@app.route('/', methods=["POST"])
def search_keyword():
  errors=""
  result_string=""
  if request.method == "POST":
    keyword = None
    try:
      keyword=request.form["keyword"]
      days=request.form["days"]
      keyword=keyword.split(None, 1)[0]
      m=re.findall( r'([\w\d]+)',keyword,re.M|re.I)
      keyword=m[0]
      if len(keyword) > 26:
        keyword = None
        raise Exception('String supplied is too big.')
    except:
      errors +="<p>Something went wrong?<br>You likely triggered the input sanitisation routine, and your query was not recognised?</p>"
    if type(days)!=int or int(days) < 0 or int(days) > 14:
      days=7
    if keyword is not None:
      results=whois_search(keyword,days)
      data = json.loads(results)
      return render_template('record.html', record=data)
  return '''
    <html><body>
      {errors}
    </body></html>
    '''.format(errors=errors)

@app.errorhandler(500)
def internal_error(error):
  return render_template('500.html', title='500 - Server Error')

@app.errorhandler(404)
def not_found(error):
  return render_template('404.html', title='404 - File Not Found')
