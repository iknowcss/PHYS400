# If you run a 10 kilometer race in 43 minutes 30 seconds, what is your average
# time per mile? What is your average speed in miles per hour? (Hint: there are
# 1.61 kilometers in a mile).

race_dist = 10               # race distance in km
race_time_min = 43.5         # race time in minutes
print "I finished a " + str(race_dist) + "km race in " + str(race_time_min) + " minutes"

kph_speed = race_dist / (race_time_min / 60) # speed in kph
mph_speed = kph_speed / 1.61                 # speed in mph
mi_time = 1 / mph_speed                      # time to run 1 mi in hours
print "That means I can run 1 mile in " + str(mi_time * 60) + " minutes"
print "My average speed is about " + str(round(mph_speed,2)) + "mph"
