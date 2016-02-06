from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import requests
import re

app = Flask(__name__)


url = 'https://api.indiegogo.com/1/campaigns.json?api_token=e377270bf1e9121da34cb6dff0e8af52a03296766a8e955c19f62f593651b346'
response = requests.get(url)
filters = [dict()]

app = Flask(__name__)
app.config.from_object(__name__)
#get request
@app.route('/')
def index():
	data = response.json()
	return render_template('index.html',data=data)
#post request- choice being title and choice2 being tagline
@app.route('/', methods=['POST'])
def search():
    data = response.json()
    choice = request.form['text1']
    choice2 = request.form['text2']
    newResp = []
    if choice != '' and choice2 == '':
    	title = re.sub('[^a-z\ \']+', " ", choice.lower())
        for x in data['response']:
            tt = x['title'].lower()
            tt =re.sub('[^a-z\ \']+', " ", tt)
            if title in tt:
                newResp.append(x)
    elif choice2 != '' and choice == '':
        tagline = re.sub('[^a-z\ \']+', " ", choice2.lower())
        for x in data['response']:
            tg = x['tagline'].lower()
            tg =re.sub('[^a-z\ \']+', " ", tg)
            if tagline in tg:
                newResp.append(x)
    elif choice!='' and choice2!='':
        tagline = re.sub('[^a-z\ \']+', " ", choice2.lower())
        title = re.sub('[^a-z\ \']+', " ", choice.lower())
        for x in data['response']:
            tg = x['tagline'].lower()
            tg =re.sub('[^a-z\ \']+', " ", tg)
            tt = x['title'].lower()
            tt =re.sub('[^a-z\ \']+', " ", tt)
            if tagline in tg and title in tt:
                newResp.append(x)
    else:
    	newResp = data['response']

    data['response'] = newResp
    return render_template('index.html', title='', tagline='', data=data)

#runs application
if __name__ == "__main__":
	app.run()





