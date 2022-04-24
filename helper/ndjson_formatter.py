import json


def format_and_add_index():
    _index = 1
    with open("cities.json", encoding='utf8') as f:
        _jsonData = f.readlines()
        _updatedJsonData = []
        for data in _jsonData:
            _index_string = '{"index":{}}\n'
            _curDataStr = json.loads(data)
            _curDataStr['id']= _index
            _updatedCurDataStr = json.dumps(_curDataStr)
            _updatedJsonData.append(_index_string)
            _updatedJsonData.append(_updatedCurDataStr + "\n")
            _index += 1

    with open("cities_index.json", 'w+') as f:
        for data in _updatedJsonData:
            f.writelines(data)


if __name__ == "__main__":
    format_and_add_index()
