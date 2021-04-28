import time,sys
toolbar = 50

# setting up toolbar [-------------------------------------]

sys.stdout.write("[%s]"%(("-")*toolbar))
sys.stdout.flush()

# each hash represents 2 % of the progress

for i in range(toolbar):
  sys.stdout.write("\r")  # return to start of line
  sys.stdout.flush()
  sys.stdout.write("[")  # Overwrite over the existing tex from the start 
  sys.stdout.write("▮"*(i+1)) # number of ▮ denotes th progress completed 
  sys.stdout.flush()
  time.sleep(0.05)
sys.stdout.write("]")
