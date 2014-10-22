DjangoRT
===========

An RT interface for your Django-powered sites

Requires: https://gitlab.labs.nic.cz/labs/python-rt

Settings:
* The included settings file (default-settings.py) has djangoRT "installed" already (listed in the INSTALLED\_APPS dealie). You need to go to the djangoRT app folder to set your RT settings
* Copy default-djangoRT\_settings.py to djangoRT\_settings.py and fill in your app settings
+ NOTE on the djangoRT RT\_QUEUE setting: this is only for the SUBMIT queue, the search function searches ALL queues by default. If this behavior is not desired you must modify djangoRT/rtUtil.py
