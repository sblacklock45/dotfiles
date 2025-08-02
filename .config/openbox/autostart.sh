#!/usr/bin/env bash

# Sets the DESKTOP_ENV variable to "Openbox"
DESKTOP_ENV="Openbox"

# Turn on numlock
numlockx &

# Launch Polybar
sh $HOME/.config/polybar/launch.sh

# Launch picom compositor (background)
picom -b

# Use feh to set background wallpaper
feh --bg-scale $HOME/Pictures/Wallpaper/Nature/LavendarField.png

# Launch dunst notifications
dunst &

# Launch Gnome Policykit agent for authentication
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# Screen lock timer using betterlockscreen
xautolock -time 10 -locker "betterlockscreen --lock" &

# Launch clipboard manager
clipit &

# Network manager applet
nm-applet &

# Bluetooth manager applet
blueman-applet &