doubleMe x = x + x
doubleUs x y = doubleMe x + doubleMe ly
doubleSmallNumber x = if x > 100
			then x
			else x*2

