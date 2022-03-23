import json
import requests
from flask import Flask, render_template


app = Flask('app')

@app.route('/')
def home():

  return render_template('index.html')

@app.route('/index2')
def data():
  url ='https://www.balldontlie.io/api/v1/season_averages?season=2020&player_ids[]=140&player_ids[]=145'
#store API response in a json file
  r = requests.get(url).json()

  filename = 'data.json'
  with open(filename, 'w') as outfile:
    json.dump(r, outfile, indent=2)
      
  with open(filename) as file_object:
    all_city_data = json.load(file_object)

  durant, embiid = [], []
  extract = ['stl', 'ftm', 'games_played', 'fgm', 'pts' ]

  for item in extract:
    data = all_city_data['data'][0][item]
    durant.append(data)

  for item in extract:
    data = all_city_data['data'][1][item]
    embiid.append(data)
  
  url2 = 'https://www.balldontlie.io/api/v1/stats/?seasons[]=2021&seasons[]=2020&player_ids[]=237&postseason=true'

  r = requests.get(url2).json()

  filename = 'data1.json'
  with open(filename, 'w') as outfile:
    json.dump(r, outfile, indent=2)
      
  with open(filename) as file_object:
    lebronstats = json.load(file_object)

  lebron = []
  points = ['pts']

  lebrond = lebronstats['data'][0][item]
  lebrond2 = lebronstats['data'][1][item]
  lebrond3 = lebronstats['data'][2][item]
  lebrond4 = lebronstats['data'][3][item]
  lebrond5 = lebronstats['data'][4][item]
  lebrond6 = lebronstats['data'][5][item]
  lebrond7 = lebronstats['data'][6][item]

  lebron.append(lebrond)
  lebron.append(lebrond2)
  lebron.append(lebrond3)
  lebron.append(lebrond4)
  lebron.append(lebrond5)
  lebron.append(lebrond6)
  lebron.append(lebrond7)
  
  url3 = 'https://www.balldontlie.io/api/v1/stats/?seasons[]=2021&seasons[]=2020&player_ids[]=140&postseason=true'
  #store API response in a json file
  r = requests.get(url3).json()

  filename = 'data3.json'
  with open(filename, 'w') as outfile:
    json.dump(r, outfile, indent=2)
      
  with open(filename) as file_object:
    matchdata = json.load(file_object)

  points  = []

  durnatd = matchdata['data'][0][item]
  points.append(durnatd)

  url4 = 'https://www.balldontlie.io/api/v1/stats/?seasons[]=2021&seasons[]=2020&player_ids[]=145&postseason=true'
  #store API response in a json file
  r = requests.get(url4).json()

  filename = 'data4.json'
  with open(filename, 'w') as outfile:
    json.dump(r, outfile, indent=2)
      
  with open(filename) as file_object:
    pdata = json.load(file_object)


  emd = pdata['data'][0][item]
  points.append(emd)
  points.append(lebrond)


  return render_template('index2.html', points=points, lebron=lebron, extract=extract, durant=durant, embiid=embiid)

@app.route('/page')
def page():
  
  url5 ='https://www.balldontlie.io/api/v1/season_averages?season=2020&player_ids[]=140&player_ids[]=145'
  #store API response in a json file
  r = requests.get(url5).json()

  filename = 'data5.json'
  with open(filename, 'w') as outfile:
    json.dump(r, outfile, indent=2)
      
  with open(filename) as file_object:
    all_data = json.load(file_object)

  durant2, embiid2 = [], []
  info2 = ['stl', 'reb', 'dreb', 'ast', 'blk', 'turnover']

  for item in info2:
    data7 = all_data['data'][0][item]
    durant2.append(data7)

  for item in info2:
    data7 = all_data['data'][1][item]
    embiid2.append(data7)


  url6 = 'https://www.balldontlie.io/api/v1/season_averages?season=2020&player_ids[]=237'

  r = requests.get(url6).json()

  filename = 'data6.json'
  with open(filename, 'w') as outfile:
    json.dump(r, outfile, indent=2)
      
  with open(filename) as file_object:
    lebronst = json.load(file_object)

  lebron7 = []
  info3 = ['pts']

  for item in info3:
    data9 = lebronst['data'][0][item]
    lebron7.append(data9)
  
  for item in info3:
    data2 = all_data['data'][0][item]
    lebron7.append(data2)

  for item in info3:
    data2 = all_data['data'][1][item]
    lebron7.append(data2)



  return render_template("page.html", durant2=durant2, embiid2=embiid2, info2=info2, lebron7=lebron7)


app.run(host='0.0.0.0', port=8080, debug=True)