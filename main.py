from flask import Flask, jsonify, render_template
import pprint
import requests
from numerize.numerize import numerize

CHANNELS = {
    'mezzo':'UCX6OQ3DkcsbYNE6H8uQQuVA'
}

pp = pprint.PrettyPrinter(indent=1)

app = Flask(__name__)
 

@app.route('/')
def index():
    url = "https://youtube138.p.rapidapi.com/channel/videos/"
    
    querystring = {"id": CHANNELS['mezzo'], "hl":"en","gl":"US"}
    
    headers = {
        "X-RapidAPI-Key": "4f052fce8emsh2c1bbf3d21591e6p144720jsn40f00bb1b690",
        "X-RapidAPI-Host": "youtube138.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    
    data = response.json()

    contents = data['contents']

    videos = [video['video'] for video in contents if video['video']['publishedTimeText']]

    print(videos)

    video = videos[0]

    return render_template('index.html', videos=videos, video=video)

@app.template_filter()
def numberize(views):
    return numerize(views, 1)

@app.template_filter()
def highest_quality_image(images):
    return images[3]['url'] if len(images) >= 4 else images[0]['url']

app.run(host='0.0.0.0', port=81)