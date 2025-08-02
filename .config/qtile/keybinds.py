# Keybinds configuration
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

import os

from libqtile.config import Key, Click, Drag
from libqtile.utils import guess_terminal
from libqtile.lazy import lazy

mod = "mod4"

terminal = guess_terminal()
webBrowser = "firefox"
mailClient = "thunderbird"
fileManager = "nemo"
home = os.path.expanduser("~")

def keybinds():
    return [
        # Application keybinds
        Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
        Key([mod], "f", lazy.spawn(webBrowser), desc="Web Browser"),
        Key([mod], "t", lazy.spawn(mailClient), desc="Mail Client"),
        Key([mod], "p", lazy.spawn(fileManager), desc="File Manager"),
        Key([mod], "c", lazy.spawn("code"), desc="Visual Studio Code"),

        # Multimedia and brightness keys
        Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 5%+"), desc = "Increase brightness"),
        Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%-"), desc = "Decrease brightness"),
        Key([], "XF86AudioRaiseVolume", lazy.spawn("wpctl set-volume -l 1 @DEFAULT_AUDIO_SINK@ 5%+"), desc = "Increase volume"),
        Key([], "XF86AudioLowerVolume", lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-"), desc = "Decrease volume"),
        Key([], "XF86AudioMute", lazy.spawn("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle"), desc = "Mute audio"),
        Key([], "XF86AudioMicMute", lazy.spawn("wpctl set-mute @DEFAULT_AUDIO_SOURCE@ toggle"), desc = "Mute microphone"),

        # Switch between windows
        Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
        Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    
        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
        Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
        Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    
        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
        Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
        Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
        Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    
        # Toggle between different layouts as defined below
        Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
        Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
        Key([mod, "shift"], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
        Key([mod, "shift"], "space", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
        Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
        Key([mod, "shift"], "0", lazy.spawn(home + "/.config/rofi/powermenu/powermenu.sh")),
        Key([mod], "r", lazy.spawn(home + "/.config/rofi/launcher/launcher.sh")),
]

def mouse():
    return [
        Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
        Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
        Click([mod], "Button2", lazy.window.bring_to_front()),
]