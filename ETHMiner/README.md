# ETH hashrate
A simple script that checks the current hashrate of my ETH miner using the [Ethermine API](https://ethermine.org/api/miner). Note that the hashrate is shown in MH/s. Clicking on the module will open ethermine in the browser.


### Setting up the module in [polybar](https://github.com/polybar/polybar):
Change ADDRESS to your ETH address.

Copy min.py into your scripts folder.  
This can be found at ~/.config/polybar/scripts/

Place this config in the modules section of your polybar config and change formatting as desired. Note that the address should be changed to your own.

```
[module/miner]
type = custom/script
interval = 300
format = <label>
format-prefix = "Ξ "
format-prefix-foreground = #00CDCF
format-underline = #00CDCF
format-foreground = ${colors.foreground}
format-background = ${colors.background}
exec = python -u ~/.config/polybar/scripts/miner.py
click-left = brave https://ethermine.org/miners/5493256F6b210a2ABa8289E41FEa50767FC28538/dashboard &
tail = true
```