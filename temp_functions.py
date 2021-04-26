#fahr_to_celsius() is the function which change fahr to celsius
def fahr_to_celsius(temp_fahrenheit):
    #converted_temp is the changed variable(fahr to celsius)
    converted_temp = ( temp_fahrenheit - 32 ) / 1.8
    return converted_temp

#temp_classifier is the function that classified tempreature for 4 categories.
def temp_classifier(temp_celsius):
    #temp_celsius is the target of temperature    
    if(temp_celsius<-2):
      return 0
    elif(temp_celsius<2):
      return 1
    elif(temp_celsius<15):
      return 2
    else:
      return 3