#!/usr/bin/env python

# incomplete work, WIP
# fails..
#    try using wmi lib and methods:
#      (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightness).CurrentBrightness
#      (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(3,18)


# importing the module
import screen_brightness_control as sbc
import fire

debug = False


def increase_brightness(amount=2):
    current_brightness = sbc.get_brightness()
    sbc.set_brightness(current_brightness + amount)
    if debug:
        print(f'increased current_brightness to {current_brightness}')


# # get the brightness of the primary display
# primary_brightness = sbc.get_brightness(display=0)
# print(primary_brightness)

if __name__ == '__main__':
    # fire.Fire(LogParser)
    print('in main..')
    debug = True
    fire.Fire()
