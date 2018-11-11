# uniq
import sys

if __name__ == '__main__':
    
    prevLine  = "?"
    firstTime = True

    for line in sys.stdin:
        
        #strip CR, LF
        line = line.strip('\n')
        line = line.strip('\r')

        # print 1st always
        if firstTime :
            prevLine = line
            firstTime = False
            print(line)
            continue
            
        if line != prevLine :
            prevLine = line
            print(line)
