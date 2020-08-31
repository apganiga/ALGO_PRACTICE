def isMonotonic(array):
	if len(array) <= 2 : 
		return True
	
	trend = 0 
	prev_trend = 0 
	for i in range(len(array)-1) : 
		if trend != 0 : 
			prev_trend = trend
		numerator = array[i] - array[i+1]
		if numerator == 0 : 
			continue 
			
		trend = numerator/abs(numerator)
		if ( trend !=0 and prev_trend != 0 ) and  trend != prev_trend :
			return False
	if trend == 0 or prev_trend == 0 : 
		return True
return True