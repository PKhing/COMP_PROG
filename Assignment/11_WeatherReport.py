# Prog-11: Weather report (EP.2)
# 6?3?????21 Name ?
import json
import math
def top_K_max_temp_by_region(data, K):
    data_by_region = {}

    for city in data.values():
        cityData = city["city"]
        for tempData in city["list"]:
            if not cityData["region"] in data_by_region:
                data_by_region[cityData["region"]] = []
            data_by_region[cityData["region"]].append((tempData["main"]["temp"],cityData["name"],tempData["dt_txt"]))
    
    def sorting_func(a):
        return(-a[0],a[1],a[2])

    for region in data_by_region:
        data_by_region[region] = sorted(data_by_region[region],key=sorting_func)[:K]

    return data_by_region

def average_temp_by_date(data, region):
    temp_by_date = {}

    for city in data.values():
        cityData = city["city"]
        if region!="ALL" and cityData["region"]!=region:
            continue

        for tempData in city["list"]:
            date = tempData["dt_txt"][:10]
            if not date in temp_by_date:
                temp_by_date[date]=[]
            temp_by_date[date].append(tempData["main"]["temp"])

    average_temp_by_date = []
    for date,tempList in temp_by_date.items():
        average_temp_by_date.append((date,sum(tempList)/len(tempList)))
    
    return sorted(average_temp_by_date)
    
def max_rain_in_3h_periods(data, region, date):

    rain_in_3h_periods = {}

    for city in data.values():
        cityData = city["city"]
        if region!="ALL" and cityData["region"]!=region:
            continue

        for tempData in city["list"]:
            thisDate = tempData["dt_txt"][:10]
            time = int(tempData["dt_txt"][11:13])
            if(thisDate!=date):
                continue

            if not time in rain_in_3h_periods:
                rain_in_3h_periods[time] = []
            if "rain" in tempData:
                rain_in_3h_periods[time].append(tempData["rain"]["3h"])

    max_rain_in_3h_periods = []
    for time,rainList in rain_in_3h_periods.items():
         max_rain_in_3h_periods.append((time,max(rainList)))
    
    return sorted(max_rain_in_3h_periods)

def AM_PM_weather_description_by_region(data, date):
    
    result = {}

    for city in data.values():
        cityData = city["city"]
        region = cityData["region"]

        for tempData in city["list"]:
            thisDate = tempData["dt_txt"][:10]
            time = int(tempData["dt_txt"][11:13])
            if time<12:
                time = "AM"
            else: 
                time="PM"
            if thisDate!=date:
                continue
            
            
            weatherList = tempData["weather"]
            for weather in weatherList:
                if not region in result:
                    result[region] = {}
                if not time in result[region]:
                    result[region][time] = {}
                if not weather["description"] in result[region][time]:
                    result[region][time][weather["description"]] = 0
                result[region][time][weather["description"]]+=1  

    def sorting_func(a):
        return (-a[1],a[0])

    for region in result.values():
        for time,weatherList in region.items():
            region[time] = sorted(weatherList.items(),key=sorting_func)[0][0]
    
    return result

def most_varied_weather_provinces(data):
    
    result = {}

    for city in data.values():
        cityData = city["city"]
        name = cityData["name"]

        for tempData in city["list"]:
            
            weatherList = tempData["weather"]
            for weather in weatherList:
                if not name in result:
                    result[name] = set()
                result[name].add(weather["description"])

    def sorting_func(a):
        return (-a[1],a[0])

    for name,weatherList in result.items():
        result[name] = len(weatherList)
    
    result = sorted(result.items(),key=sorting_func)

    most_varied_weather = result[0][1]
    return set([i[0] for i in result if i[1]==most_varied_weather])
def main():
    # put your own testing codes in this function
    data = json.load(open('Assignment/th_weather_39.json'))    
    print(top_K_max_temp_by_region(data, 2))
main()
