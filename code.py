from time import sleep
from progress.bar import Bar

with Bar('Progress:', fill='#', suffix='%(percent).1f%% Complete') as bar:
    for i in range(100):
        sleep(0.02)
        # Do Work here.
        bar.next()
bar.finish()
