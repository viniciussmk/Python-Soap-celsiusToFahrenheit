import requests

url="https://www.w3schools.com/xml/tempconvert.asmx"
headers = {'content-type': 'application/soap+xml'}
# headers = {'content-type': 'text/xml'}
data = input('graus Celsius  >>')
# data = '25'
body = f"""<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <CelsiusToFahrenheit xmlns="https://www.w3schools.com/xml/">
      <Celsius>{data}</Celsius>
    </CelsiusToFahrenheit>
  </soap12:Body>
</soap12:Envelope>"""

response = requests.post(url,data=body,headers=headers)
print(response.text)

with open('arq01.xml', 'w') as arquivo:
    arquivo.write(response.text)
