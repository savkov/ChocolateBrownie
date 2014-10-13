ChocolateBrownie
================

IPython pygment style and stylesheet.

##Installation

Install pygments if required

```pip install pygments```

Copy _chocolatebrownie.py_ to 

><python_dir>/site-packages/pygments/styles/ 


To make _chocolatebrownie_ your default qtconsole style you need to configure a profile. Start by running the following command to create a profile if there isn't one:

```ipython profile create```

This should create several configuration files. In the qtconsole configuration file

* _Linux_ or _OS X_ - ~/.ipython/profile_default/ipython_qtconsole_config.py
* _Windows_ - %USERPROFILE%\.ipython\profile_default\ipython_qtconsole_config.py (not tested)

...set the following parameters as shown below:

>c.IPythonWidget.syntax_style = u'chocolatebrownie'

>c.IPythonQtConsoleApp.stylesheet = '<path to chocolatebrownie.css>'


##Colors
Names and HEX codes from [http://www.colourlovers.com/](http://www.colourlovers.com/)


##TODO
Add error and stack trace highlighting.