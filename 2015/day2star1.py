#!/usr/bin/env python
import sys

# main: this is the main function of this Python
#
def main(argv):

    sum = 0    # sum of the wrapping paper area
    
    # Define the input file name from which to read the parentheses
    # I really need a way of defining this that isn't hardcoding
    filename="day2star1.txt"
    
    # Try to open the file and read each line. Split up each line using the x as a token
    # to separate out the length, width, and height. Convert the line length, width, and height
    # to integers and call the getWrappingPaperArea function to obtain the required wrapping
    # paper area for each present.
    try:
        with open(filename) as f:
            for line in f:

                try:
                    # split up each line
                    (ls,ws,hs) = line.split('x')

                    # convert to int
                    l = int(ls)
                    w = int(ws)
                    h = int(hs)

                    # function call to get this present's wrapping paper area
                    area = getWrappingPaperArea(l,w,h)

                    # Add this present's wrapping paper area
                    sum += area
                    
                except ValueError:
                    print("ERROR >> Value")
                    
            # Print result
            print("The elves need %d square feet of wrapping paper" %(sum))
            
        # Print out the total wrapping paper needed
        #print("The elves need %d square feet of wrapping paper" %(sum))
        
    except IOError:
        print("ERROR >> Missing file day2star1.txt")


        
# Method to find the total box surface area as well as the "little extra" paper needed
# INPUT : l - length
# INPUT : w - width 
# INPUT : h - height
# OUTPUT :  the area of wrapping paper needed for this present
def getWrappingPaperArea(l,w,h):

    # Box surface area
    boxArea = 2*l*w + 2*w*h + 2*h*l

    # Find the side with the smallest area
    # Return the box total area + the area of the smallest side

    # Cases where all sides have unique area
    if(l*w < w*h and l*w < h*l):
        return(l*w + boxArea)
    elif(w*h < l*w and w*h < h*l):
        return (w*h + boxArea)
    elif(h*l < l*w and h*l < w*h):
        return(h*l + boxArea)
    # Cases where 2 sides have equal areas
    elif(l*w == w*h and l*w < h*l):
        return(l*w + boxArea)
    elif(w*h == h*l and w*h < l*w):
        return (w*h + boxArea)
    elif(h*l == l*w and h*l < w*h):
        return(h*l + boxArea)
    # Case where everything is equal
    else:
        return(h*l + boxArea)


# begin gracefully
#
if __name__ == "__main__":
    main(sys.argv[0:])

#
# end of file

                        
                
                
