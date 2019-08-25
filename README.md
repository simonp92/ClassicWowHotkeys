# ClassicWowHotkeys
Adding hotkeys to the classicwow.live/leveling/ guide, so you dont have to leave the WoW Client to change steps

## Setup
This project uses Python 3.6 and Selenium with the Chrome driver

Install Python 3.6:
https://www.python.org/downloads/

Install the Chrome Selenium driver for your version of Chrome
https://chromedriver.chromium.org/downloads

Install the following Python packages:

``` console
pip install selenium

pip install pynput

pip install furl
```

## Editing the settings file
In the settings.ini file you can type the details about your faction, race and class, so the correct guide is loaded.

Values for section and step are updated automatically, so the guide loads where you left off

``` ini
[settings]
faction = horde
race = troll
class = hunter
section = 1
step = 1
```

## Starting the guide
run the command
``` console
python LaunchGuide.py
```
in the project directory to start the guide

## Hotkeys
Use the hotkey "SHIFT + A" to go back in the guide

Use the hotkey "SHIFT + S" to go forward in the guide
