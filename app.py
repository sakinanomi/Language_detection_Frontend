from flask import Flask
from flask import render_template,request,redirect
import requests

app = Flask(__name__)
ans=None
@app.route('/')
def index():
	global ans

	return render_template('index.html',text=None,ans=ans)

@app.route('/send',methods=['GET','POST'])
def send():
	text=None
	if request.method == 'POST':
		text = (request.form.get('text'))

		data={'text':text}

		language = requests.post('https://la-identification.herokuapp.com/predict', data=data)

		final = (language.json()['predicted'])

		print(final)




	return render_template('index.html',text=text,ans=final)




if __name__ == '__main__':

	app.run(debug=True )
