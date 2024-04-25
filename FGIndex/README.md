# Crypto Fear & Greed Index
A simple script which pulls the current crypto fear & greed index from alternative.me's [api](https://api.alternative.me/fng/)

### Setting up the module in [polybar](https://github.com/polybar/polybar):
Copy fgindex.py into your scripts folder.  
This can be found at ~/.config/polybar/scripts/

Place this config in the modules section of your polybar config and change formatting as desired.

```
[module/fgindex]
type = custom/script
interval = 20000
format = <label>
format-prefix = " "
format-prefix-foreground = ${colors.secondary}
format-underline = ${colors.secondary}
format-foreground = ${colors.foreground}
format-background = ${colors.background}
exec = python -u ~/.config/polybar/scripts/fgindex.py
tail = true
```