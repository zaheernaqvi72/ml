import sys
import cowsay

if len(sys.argv) > 1:
    cowsay.trex("Hello, " + sys.argv[1] + "!")
    
    