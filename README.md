# Agent App Parallel Testing

**Tech Stack**
Python 3.8, Appium, Pytest-BDD, Allure Reports, Pytest-Xdists


## Prerequisites
1. Install Allure Reports from https://docs.qameta.io/allure/#_installing_a_commandline
2. Install Android Studio from https://developer.android.com/studio
3. Install Appium from https://appium.io/
4. Install Python from https://www.python.org/downloads/
5. Install virtualenv from https://virtualenv.pypa.io/en/latest/installation.html


##Solution Explained
This script can auto-detect the device info from environment and test the test cases
in multiple devices. As a result test execution time improves significantly. Find below
the time taken for all test case execution in local machine.

P.S: On-boarding could not be performed in multiple device due to sim card dependency
All these cases are run in previously installed and on-boarded app. If you want to perform
installing and On-boarding that should be in single device only.

#### 1 Device
203.21s
#### 2 Devices
147.81s

### Test Markers
Two markers have benn introduced.
1. agent -> Run all the test cases (without on-board)
2. on-board -> Run all the test cases including on-board




## Getting Started

#### Clone the repo
```
git clone git@github.com:<repo_name>
```

#### Create vitual environment for the project
```
virtualenv venv
```
#### Activate the virtual environment
Windows
```
venv\Scripts\activate
```
Linux
```
source venv/bin/activate
```
#### Install requirements

```
pip install -r requirements.txt
```

### Before Running the tests 
1. Start the appium server
2. Connect devices with cable 
3. Install agent app form: -> BusinessApp_debug_2.3.2-UAT-DEBUG.apk
4. On-board the Agent account according to Sim inserted that specific devices


### Run tests
To run tests, runner.py has been introduced.

usage:

```
usage: runner.py [-h] [-d {android, ios}] [-hh HUBHOST] [-hp HUBPORT] [--hubprotocol HUBPROTOCOL] [--devnum DEVNUM] [--testmarker TESTMARKER]

optional arguments:
  -h, --help            show this help message and exit
  -d {android, ios}, --device {android, ios}
                        Specify device type. supports {android, ios}
  -hh HUBHOST, --hubhost HUBHOST
                        Specify hub host. ex: 127.0.0.1
  -hp HUBPORT, --hubport HUBPORT
                        Specify hub port. ex: 4723
  --hubprotocol HUBPROTOCOL
                        Specify hub portocol. ex: http
  --devnum DEVNUM       Specify number of devices
  --testmarker TESTMARKER
                        Mark tests
```

1. Go to project root directory
2. Run runner.py with argument `devnum` if appium is running locally and connected to `4723` port
```
python3 runner.py --devnum 2
```
3. run this command to see the report
```
allure serve ./test_result
```

### New Cases will be added soon and README will be changed accordingly