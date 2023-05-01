# edutech
Assignment to get frequency of all words present in a static web page, given the URL

The present code file at last commit contains result for website - www.python.org

Result file 'result.json' gets updated entirely with every successful run.

Prerequisites:
The system is desired to have python libraries: requests, json, html

To check if you have a desired module: 

```

$ python3 -c "import math"
$ echo $?
0                                # math module exists in system

$ python3 -c "import numpy"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ImportError: No module named numpy
$ echo $?
1                                # numpy module does not exist in system     


```

To Install a missing module:

```
sudo apt-get install python3-<module name> ## for Python3
```

Procedure to **Run** progam:
1. Open the terminal at project directory and run command: python3 assignment.py
2. Enter the desired (VALID) URL, for example : www.google.com
3. Check the Result in file - '_result.json_'
