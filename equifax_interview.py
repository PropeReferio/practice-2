# A digital clock has times between 12:00 and 11:59. A 'clocksum' is the sum 
# of each individual number which makes up the time. So the clocksum of 
# 12:00 is 3 (1 + 2 + 0 + 0). The clocksum of 11:59 is 16 (1 + 1 + 5 + 9)

# Write a function that prints out the minimum and maximum clocksum.
input = '12:00'

def clock_sum():
		hours = list(range(1,13))
		hour_possibilities = []
		string_hours = list(map(lambda x: str(x), hours))
		for hour in string_hours:
				hour_possibilities.append(sum([int(char) for char in hour]))
		
		# hours_1st_digit = list(range(2))
		# hours_2nd_digit = list(range(10)) # This allows for 13 - 19 in the hour
		minutes_1st_digit = list(range(6))
		minutes_2nd_digit = list(range(10))
		minute_possibilities = []
		# for i in hours_1st_digit:
		# 		for j in hours_2nd_digit:
		# 				hour_possibilities.append(i + j)
		max_hour = max(hour_possibilities)
		min_hour = min(hour_possibilities)
		for i in minutes_1st_digit:
				for j in minutes_2nd_digit:
						minute_possibilities.append(i + j)
		max_minute = max(minute_possibilities)
		min_minute = min(minute_possibilities)
		# print('max and min minutes: ', max_minute, min_minute)
		# print('max and min hours: ', max_hour, min_hour)
		# Made an array
		print('Minimum clocksum: ', min_hour + min_minute)
		print('Maximum clocksum: ', max_hour + max_minute)

clock_sum()