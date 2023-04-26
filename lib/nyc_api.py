import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

    response = requests.get(URL)
    return response.content

  def program_school(self):
    return [program['agency'] for program in json.loads(self.get_programs())]

prog = GetPrograms()
schools = prog.program_school()

for school in set(schools):
  print(school)