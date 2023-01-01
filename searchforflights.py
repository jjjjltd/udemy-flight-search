import requests

url = "https://compare-flight-prices.p.rapidapi.com/GetPricesAPI/StartFlightSearch.aspx"

querystring = {"lapinfant":"0","child":"1","city2":"CDG","date1":"2021-01-01","youth":"0","flightType":"2","adults":"2","cabin":"1","infant":"0","city1":"LAX","seniors":"0","islive":"true"}

headers = {
	"X-RapidAPI-Key": "434eebaf4emshabf92a47af052bap193734jsna217fe1abbe9",
	"X-RapidAPI-Host": "compare-flight-prices.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)