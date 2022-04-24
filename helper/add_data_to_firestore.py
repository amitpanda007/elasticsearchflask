import json

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('firebase_key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

BASE_DATA = '''
{
   "contactInfos":{
      "centralNumbers":[],
      "majorHelplines":[],
      "userProvidedNumbers":[]
   },
   "location":[]
}
'''


def format_data(location, centralNumbers, majorHelplines, userProvidedNumbers):
    dataAsJson = json.loads(BASE_DATA)

    if type(location) is list:
        dataAsJson['location'] = location
    else:
        dataAsJson['location'] = [location]

    if type(centralNumbers) is list:
        dataAsJson['contactInfos']['centralNumbers'] = centralNumbers
    else:
        dataAsJson['contactInfos']['centralNumbers'] = [centralNumbers]

    if type(majorHelplines) is list:
        dataAsJson['contactInfos']['majorHelplines'] = majorHelplines
    else:
        dataAsJson['contactInfos']['majorHelplines'] = [majorHelplines]

    if type(userProvidedNumbers) is list:
        dataAsJson['contactInfos']['userProvidedNumbers'] = userProvidedNumbers
    else:
        dataAsJson['contactInfos']['userProvidedNumbers'] = [userProvidedNumbers]

    return dataAsJson


def add_data(data: dict):
    col_ref = db.collection(u'contacts')
    col_ref.add(data)


if __name__ == "__main__":
    location = ["Cuttack"]
    centralNumbers = [{
        "name": "Police",
        "description": "Central Police Station",
        "telephone": "100",
    },
    {
        "name": "Women Help Line",
        "description": "Women Help Line",
        "telephone": "1091",
    }
    ]
    majorHelplines = [{
        "name": "Blue Line Hospital",
        "description": "Medicine Hospital / Best ICU in Cuttack / Best Cardiology Hospital in Cuttack",
        "telephone": "06712363333",
    },
    {
        "name": "Out Patient Department of SCB",
        "description": "Out Patient Department of SCB",
        "telephone": "06712414355",
    }
    ]
    userProvidedNumbers = [{
        "name": "Scb Mc Hospital Society",
        "description": "Scb Mc Hospital Society",
        "telephone": "06712414355",
    },
    {
        "name": "Kalupada Seka Kendra",
        "description": "Kalupada Seka Kendra",
        "telephone": "09437319135",
    }
    ]

    data = format_data(location, centralNumbers, majorHelplines, userProvidedNumbers)
    print(data)
    add_data(data)