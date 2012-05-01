import math

# 1) The volume of a sphere with radius r is 4/3 pi r3. What is the volume of a 
#    sphere with radius 5? Hint: 392.6 is wrong!
print "Volume of a sphere with radius 5: " + str(4.0 / 3 * math.pi * 5 ** 3)

# 2) Suppose the cover price of a book is $24.95, but bookstores get a 40%
#    discount. Shipping costs $3 for the first copy and 75 cents for each
#    additional copy. What is the total wholesale cost for 60 copies?
cover_price = 24.95
discount_price = 24.95 * (1 - 0.40)
ship_init = 3.0
ship_add = 0.75
num_copies = 60
book_cost = discount_price * num_copies
shipping_cost = ship_init + (num_copies - 1) * ship_add
wholesale_cost = book_cost + shipping_cost
print "The wholesale cost to have 60 books shipped is $" + str(wholesale_cost)

# 3) If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per
#    mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace
#    again, what time do I get home for breakfast?
time = 6 + 52/60.
time += (8/60. + 15/3600.) * 2 # Easy pace; 8min 15sec per mile
time += (7/60. + 12/3600.) * 3 # Tempo pace; 7min 12sec per mile
time_hour = int(time)
time_min = int((time - time_hour) * 60)
print "After my run, I arrived home at " + str(time_hour) + ":" + str(time_min) + " am"
