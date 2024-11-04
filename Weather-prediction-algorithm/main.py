import requests

print("welcome to the weather predictor ")

city_name = input("Just Enter the City you want the weather report for and click on the button! It's that simple! ")



def gen_report(city_name):
  url = 'https://wttr.in/{}'.format(city_name)
  try:
    data = requests.get(url)
    t = data.text
  except:
    t = "error Occurred"
  print(t)

gen_report(city_name)
    