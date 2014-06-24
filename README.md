BrainlyLabs
===========

Some examples from Tests, written for mobile Apps (from Brainly group).
The test are written for #4 KraQA meetup: "Appium - mobile test automation".
The code above is the sample test written in pytohon to communicate with appium server and perform user actions on Android Device.


# Appium + python tests - how to set up?


- Install **Appium app** from [here:](http://appium.io/)
- Run appium app, and set all the preferences for Android. [Here is an instruction how to do it:](https://github.com/appium/appium-dot-app#parameter-guide)
- Download an [appium client for python:](https://github.com/appium/python-client), and add it to the directory with your pyton tests
- Install the Webdriver library for python
- Launch an appium server (click the **Launch button**) and try to run appium inspector, when the server starts - if you set all teh preferences, inspector should run without the problem
- Run your tests: 

```shell
  python TestAddTask.py
```

In case of any problems write to me: @marianneSiara, machluchachlumaria@gmail.com
