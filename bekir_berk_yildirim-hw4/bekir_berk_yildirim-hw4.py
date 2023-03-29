def split_string(s):
    substrings = []
    start_index = 0
    for i in range(len(s)):
        if s[i] == ";":
            substring = s[start_index:i]
            substrings = substrings + [substring]
            start_index = i + 1
    
    substring = s[start_index:]
    substrings = substrings + [substring]
    
    return substrings

with open('Airports_Cleaned.csv') as f:
    number_of_airports = {}
    total_passengers = {}
    total_passengers_per_airport = {}
    maximum_passengers = 0
    most_crowded_airport = ''
    airport_list = []
    for line in f:
        if 'Airport;Location;Country;Passengers;Year' in line:
            continue
        line_list = split_string(line)#0:Airport Name 1:Airport Location 2:Country 3:Passengers 4:Year
        if line_list[0] not in airport_list:
            airport_list += [line_list[0]]
        if line_list[2] not in total_passengers_per_airport:
            total_passengers_per_airport[line_list[2]] = int(line_list[3])
        else:
            total_passengers_per_airport[line_list[2]] += int(line_list[3])
        if total_passengers_per_airport[line_list[2]] > maximum_passengers:
            maximum_passengers = total_passengers_per_airport[line_list[2]]
            most_crowded_airport = line_list[2]
    for country in total_passengers_per_airport:
        for airport in airport_list:
            if country in airport:
                if country in number_of_airports:
                    number_of_airports[country] += 1
                else:
                    number_of_airports[country] = 1
    print(len(airport_list))
    print('The most crowded airport in all years is',most_crowded_airport,'with',maximum_passengers,'passengers.')
    for country in total_passengers_per_airport:
        print(country,':',total_passengers_per_airport[country]//5)#5 years
    print(number_of_airports)
    


