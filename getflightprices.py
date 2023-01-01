import requests

url = "https://compare-flight-prices.p.rapidapi.com/GetPricesAPI/GetPrices.aspx"

querystring = {"SearchID":"<REQUIRED>"}

headers = {
	"X-RapidAPI-Key": "434eebaf4emshabf92a47af052bap193734jsna217fe1abbe9",
	"X-RapidAPI-Host": "compare-flight-prices.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)