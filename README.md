# Language_detection_Frontend

This is the client side for the language detection API that is [This repo](https://github.com/sakinanomi/Language-detection-api)
<br>

## About the project
- This is a Flask website
- The HTML contains the form which takes one input i.e the string whose language has to be detected, the fields name is 'text' as the api requires
- On submitting the form redirects to '/send' route, which sends the text string in the form of json to the api and recieves the answer from api with the key 'predicted' 
- This answer is then sent to the html page using render_template and displayed.

#### gunicorn in requirements.txt and procfile is added so that we can deploy on heroku


This is hosted on heroku<br>
[Link](https://lang-detection-ui.herokuapp.com/)
