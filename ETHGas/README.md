# ETH gas fees
A simple script that checks the current Ethereum gas fees using the [Etherchain API](https://etherchain.org/api/gasnow). Note that the fee shown is for "Rapid" and is in GWei. Clicking on the module will open etherchain in the browser.


### Setting up the module in [polybar](https://github.com/polybar/polybar):
Copy gas.py into your scripts folder.  
This can be found at ~/.config/polybar/scripts/

Place this config in the modules section of your polybar config and change formatting as desired. Note that brave should be changed to your current browser.

```
[module/gas]
type = custom/script
interval = 5
format = <label>
format-prefix = " "
format-prefix-foreground = #FF7133
format-underline = #FF7133
format-foreground = ${colors.foreground}
format-background = ${colors.background}
exec = python -u ~/.config/polybar/scripts/gas.py
click-left = brave https://etherchain.org/tools/gasnow &
tail = true
```
