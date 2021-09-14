# athan-module
A simple script that checks the time until the next Islamic prayer by making use of the [Prayer Times API](https://prayertimes.date/api).


### Setting up the module in [polybar](https://github.com/polybar/polybar):
Copy athan.py into your scripts folder.  
This can be found at ~/.config/polybar/scripts/

Inside athan.py, change the CITY and SCHOOL variables to match your location and prayer time calculation method accordingly. More information regarding these variables can be found [here](https://prayertimes.date/api/docs/today). 

Finally place this config in the modules section of your polybar config

```
[module/athan]
type = custom/script
interval = 60
format = <label>
format-prefix = " "
format-prefix-foreground = #9345ee
format-underline = #9345ee
format-foreground = ${colors.foreground}
format-background = ${colors.background}
exec = python -u ~/.config/polybar/scripts/athan.py
```
