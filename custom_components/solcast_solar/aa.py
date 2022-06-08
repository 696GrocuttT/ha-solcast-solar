from datetime import datetime, timedelta


def setup_dummy_data():
        temp = {
            '00': {'pv_estimate': 0.0},
            '01': {'pv_estimate': 0.0},
            '02': {'pv_estimate': 0.0}
        }
        temp1 = {
            '00': {'pv_estimate': 0.0},
            '01': {'pv_estimate': 0.0},
            '02': {'pv_estimate': 0.0}
        }
        return  dict({'today':temp, 'tomorrow':temp1, 'energy':{}, 'api_used':0, 'last_updated': ''})

def merges(old,new):
    for k,v in new.items():
        old[k] = v

#


data = setup_dummy_data()


wh_hours = {}

today = datetime.now()
tomorrow = datetime.now() + timedelta(days=1)

for k,v in data['today'].items():
    # print(today.year, today.month, today.day, int(k), 0, 0, 0).isoformat()
    d = datetime(today.year, today.month, today.day, int(k), 0, 0, 0).isoformat()
    wh_hours[d] = v
a = wh_hours

wh_hours = {}
for k,v in data['tomorrow'].items():
    # print(today.year, today.month, today.day, int(k), 0, 0, 0).isoformat()
    d = datetime(tomorrow.year, tomorrow.month, tomorrow.day, int(k), 0, 0, 0).isoformat()
    wh_hours[d] = v
b = wh_hours 



print(a|b)