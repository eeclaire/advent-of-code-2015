#!/usr/bin/env python
import sys

# main: this is the main function of this Python
#
def main(argv):

    floor = 0;    # Keeps track of the floor Santa is visiting
    pos = 0;    # Counter for the character position
    
    # Define the input file name from which to read the parentheses
    filename="day1star1.txt"

    # Try to open the file and read each character until the end of file.
    # If the read character is '(', increment the floor on which Santa is.
    # If the read character is ')', decrement the floor on which Santa is.
    # If the try fails, print out a warning to the user.
    try:
        with open(filename) as f:
            while True:
                c = f.read(1)
                if not c:
                    print "End of file"
                    break
                else:
                    pos += 1 
                    if (c == '('):
                        floor += 1
                    elif(c == ')'):
                        floor -= 1
                        
                        # Catch the moment Santa enters the basement
                        if(floor == -1):
                            break
        # Print out the final floor
        print ("Santa entered the basement on visit number %d" %(pos))

    except IOError:
        print("ERROR >> Missing file day1star1.txt")

# begin gracefully
#
if __name__ == "__main__":
    main(sys.argv[0:])

#
# end of file

                        
                
                
