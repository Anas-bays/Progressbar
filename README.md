# Progressbar
## Introduction
A text progress bar is typically used to display the progress of a long running operation, providing a visual cue that processing is underway.
## What we use?
* [progress.bar](https://www.example.com)
    #### How do we install?
      pip install progress.bar
* You can use the 'progress.bar' package to add a simple progress bar to your code like this:
```
with Bar('Progress:', fill='#', suffix='%(percent).1f%% Complete') as bar:
    for i in range(100):
        sleep(0.02)
        bar.next()
bar.finish()
```
which will give you a dynamic output which will look like this:
 `Progress: |▋▋▋▋▋▋▋▋▋                                      | 60.0% complete` 


Enjoy!

