
def add_time(start, duration, day_of_week =""):
    day_of_week_tuple = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    new_time = ""
    extras = ""

    splitted_time  = start.split(' ')
    splitted_adder = duration.split(':')
    
    hours   = int(splitted_time[0].split(':')[0])
    minutes = int(splitted_time[0].split(':')[1])

    to_add_hr  = int(splitted_adder[0])
    to_add_min = int(splitted_adder[1])
    
    #check AM or PM and convert in a format that I can understand
    if splitted_time[1] == 'PM': 
        hours = hours + 12
    # add hours and minutes
    hours = hours + to_add_hr
    minutes = minutes + to_add_min
    # if minutes is greater than 59min    
    if minutes > 59:
        minutes = 60 - minutes
        hours = hours + 1
    
    if hours > 23:
        more_days = hours//24
        hours = hours % 24
        if more_days == 1:
            extras = extras + " (next day)"
        else:
            extras = extras + " ("+ str(more_days)+" days later)"
            
    print(hours, minutes)
    
    if hours > 12:
        hours = hours - 12
        splitted_time[1] = "PM"
    else:
        splitted_time[1] = "AM"
        
    #results
    new_time = str(hours) + ":" +  str(minutes) + " "+ str(splitted_time[1]) + str(extras)
    return new_time


if __name__ == '__main__':
    # print(add_time("3:00 PM", "3:10"))
    # print(add_time("11:43 AM", "00:20"))
    # print(add_time("10:10 PM", "3:30"))
    print(add_time("11:43 PM", "24:20"))
    # print(add_time("6:30 PM", "205:12"))