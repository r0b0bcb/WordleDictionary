def check_input(green, yellow, exclude):
    if len(green) != 5 or len(yellow) > 5:
        return False
    elif all(x.isalpha() for x in green.translate(str.maketrans('','','?'))) != True:
        return False
    elif all(x.isalpha() for x in yellow) != True:
        return False
    elif all(x.isalpha() for x in exclude) != True:
        return False
    else:
    	return True
