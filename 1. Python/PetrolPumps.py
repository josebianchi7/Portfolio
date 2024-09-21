# Author: Jose Bianchi
# GitHub username: josebianchi7


def truckTour(petrolpumps):
    """
    Given a circle with N petrol stations around the circle.
    Petrol stations are numbered from 0 to (N-1), inclusive.
    You are given the amount of petrol each pump has and
    the distance to the next pump.
    
    You begin with an empty tank to hold infinite petrol,
    You can start at any petrol station.
    Calculate the first point from where the truck will
    be able to complete the circle.
    
    Consider the truck will stop at each petrol station.
    The truck will move 1km for each liter attained.
    
    At each station, remember that are two values:
        1. amount of petrol in liters
        2. distance to next station in km
    
    param petrolpumps: arr containing lists with 2 elements each    
    return int: index of petrol pump to start at
    """
    # Find petrol station with greatest difference of liter on hand to km to next station
    max_stations = len(petrolpumps)
    
    
    for i in range(len(petrolpumps)):
        curr_station = petrolpumps[i]
        fuel = curr_station[0]
        distance = curr_station[1]
        fuel_left = fuel - distance
        station_counter = 1
        j = i + 1
        # Continue driving until run out of gas
        # Ensure to reach all stations
        while fuel_left > 0 and station_counter < max_stations:  
            
            # Ensure to loop around if needed,
            if j >= max_stations:
                j -= max_stations
            
            next_station = petrolpumps[j]
            fuel_left += next_station[0]
            fuel_left -= next_station[1]
                
            station_counter += 1
            j+= 1

            # If we can make it to the last station, loop was successful from current starting station 
            # VERIFY IF NEED TO GET BACK TO FIRST STATION OR CAN STOP AT LAST STATION
            # IF CAN STOP AT LAST STATION, change left of comparison to max_stations - 1
            if station_counter == (max_stations):
                return i 
            

if __name__ == '__main__':
    stations1 = [[1,5], [10,3], [3,4]] 
    print(truckTour(stations1))
