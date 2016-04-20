
choice = raw_input("Enter if convert to Fahrenheit or Celcius, F/C?")
conv = raw_input("Enter a NUMBER to be converted: ")
if conv.isalpha():
   print "Please enter only the things that is asked :) "
else:  
   
   if choice.lower() == "f":
       ansf = (1.8 * float(conv)) + 32
       print str(float(ansf)) + " F"
   elif choice.lower() == "c":
       ansc = (float(conv) - 32) * 0.56
       print str(float(ansc)) + " C"
   else:
       print "Please enter only the things that is asked :) "
       

