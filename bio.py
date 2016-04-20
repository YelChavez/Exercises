
print                             "        BIODATA APP       "
dash=                              "  ----------------------"
print dash
print 								"  Personal Information"
print dash
name= 					  raw_input("  Full name: ")
address= 				  raw_input("  Address  : ")
age=                      raw_input("  Age      : ")
mobile=                   raw_input("  Mobile   : ")
hobby=                    raw_input("  Hobby    : ")
print dash
print                               "  School"
print dash
schoolName=               raw_input("  Scool Name: ")
year=                     raw_input("  Year      : ")
course=                   raw_input("  Course    : ")
print dash
print                               "  Output Message"
print dash
#output message
print "            Hi my name is %s. I live in %s. I'm %s years old. \nMy mobile number is %s. And my Hobby is %s. I'm currently studying at %s, a %s student, and taking up a course of %s " % (name, address, age, mobile,hobby,schoolName,year,course)






