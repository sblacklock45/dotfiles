# Rules configuration
# Stevan Blacklock - June 2025

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile.config import Match
from libqtile import layout

#Window and floating rules
def rules():
    return [
        # Run the utility of `xprop` to see the wm class and name of an X client
        *layout.Floating.default_float_rules,
        
        # Window classes
        Match(wm_class="dialog"), # Dialog windows
        Match(wm_class="download"), # Download windows
        Match(wm_class="error"), # Error notifications
        Match(wm_class="toolbar"), # Toolbars
        Match(wm_class="notification"), # Notifications
        Match(wm_class="file_progress"), # File progress boxes
        Match(wm_class="kitty"),  # Terminal
        Match(wm_class="nemo"),  # File Manager
        Match(wm_class="gpick"), # Color picker
        Match(wm_class="viewnior"), # Image viewer
        Match(wm_class="leafpad"), #Text Editor
        Match(wm_class="qalculate-gtk"), # Calculator
        Match(wm_class="engrampa"), # Archive manager
        Match(wm_class="pavucontrol"), # Pulseaudio control
        Match(wm_class="blueman-manager"), # Bluetooth device manager
        Match(wm_class="nm-connection-editor"), # Network management
        Match(wm_class="system-config-printer"), # Printer management
        Match(wm_class="gpartedbin"), # Gparted
        Match(wm_class="timeshift-gtk"), # Timeshift
        Match(wm_class="epdfview"), # PDF viewer
        Match(wm_class="Fuse"), # ZX Spectrum emulator
        Match(wm_class="x64sc"), # C64 emulator
        Match(wm_class="nwg-look"), # GTK theme application
        Match(wm_class="qt5ct"), # qt5 theme settings
        Match(wm_class="qt6ct"), # qt6 theme settings

        # Window titles
        Match(title="Authentication Required"),
        Match(title="About Mozilla Firefox"),
        Match(title="About Mozilla Thunderbird"),
        Match(title="Settings"),
]