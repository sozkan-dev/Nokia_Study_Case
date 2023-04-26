import csv

all_devices = ['SERVER1', 'SERVER22', 'SERVER_X']

all_data = {}
for device in all_devices:
    all_data[device] = {'Card': [], 'Temperature': []}

with open('Cards.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        device = row['Device']
        card = row['Card']
        temperature = int(row['Temperature'])
        all_data[device]['Card'].append(card)
        all_data[device]['Temperature'].append(temperature)


TOTAL_DEVICES = len(all_devices)
TOTAL_CARDS = len(all_data["SERVER1"]['Card']) + len(all_data["SERVER22"]['Card']) + len(all_data["SERVER_X"]['Card'])
SERVER1_COUNT = len(all_data["SERVER1"]['Card'])
SERVER22_COUNT= len(all_data["SERVER22"]['Card'])
SERVER_X_COUNT= len(all_data["SERVER_X"]['Card'])
MAX_HEAT = max(all_data["SERVER1"]["Temperature"] + all_data["SERVER22"]["Temperature"] + all_data["SERVER_X"]["Temperature"])

html = f"<table border=1><h1>SUMMARY</h1><tr><th>Total Devices</th><th>Total Cards</th><th>Max Card Temperature</th><th>Hottest Card/Device</th></tr><tr><td>{TOTAL_DEVICES}</td><td>{TOTAL_CARDS}</td><td>{MAX_HEAT}</td><td>X/Y</tr></table>"
html2 = f"<table border=1> <h1>Devices</h1> <thead> <tr> <th>Device</th> <th>Total # of Cards</th> <th>High Temp. Cards #</th> <th>Max Temperature</th> <th>Avg. Temperature</th> </tr> </thead> <tbody> <tr> <td>SERVER1</td> <td>{len(all_data['SERVER1']['Card'])}</td> <td>{len([i for i in all_data['SERVER1']['Temperature'] if i >=70])}</td> <td>{max(all_data['SERVER1']['Temperature'])}</td> <td>{sum(all_data['SERVER1']['Temperature'])/len(all_data['SERVER1']['Temperature'])}</td> </tr> <tr> <td>SERVER22</td> <td>{len(all_data['SERVER22']['Card'])}</td> <td>{len([i for i in all_data['SERVER22']['Temperature'] if i >=70])}</td> <td>{max(all_data['SERVER22']['Temperature'])}</td> <td>{sum(all_data['SERVER22']['Temperature'])/len(all_data['SERVER22']['Temperature'])}</td> </tr> <tr> <td>SERVER_X</td> <td>{len(all_data['SERVER_X']['Card'])}</td> <td>{len([i for i in all_data['SERVER_X']['Temperature'] if i >=70])}</td> <td>{max(all_data['SERVER_X']['Temperature'])}</td> <td>{sum(all_data['SERVER_X']['Temperature'])/len(all_data['SERVER_X']['Temperature'])}</td> </tr> </tbody></table>"

html3 = html + html2

with open("table.html", "w") as html_file:
    html_file.write(html3)
    print("DONE!")


