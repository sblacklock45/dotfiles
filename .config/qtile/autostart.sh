#!/usr/bin/env bash

# Sets the DESKTOP_ENV variable to "Qtile"
DESKTOP_ENV="Qtile"

# Turn on number lock
numlockx &

# Use feh to set background wallpaper
feh --bg-fill $HOME/Pictures/Wallpaper/Nature/Toadstool.jpg &

# Start picom compositor
picom -b

# Launch dunst notification daemon
dunst &

# Launch Gnome PolicyKit agent
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# Screen lock timer using betterlockscreen
xautolock -time 10 -locker "betterlockscreen --lock" &