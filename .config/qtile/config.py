# Main Qtile configuration
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

import os, subprocess
import colors

from libqtile import extension, hook, layout, qtile
from libqtile.config import Key, Screen
from libqtile.lazy import lazy

from keybinds import keybinds, mouse
from groups import groups
from layouts import layouts
from screens import screen
from rules import rules

home = os.path.expanduser("~")

mod = "mod4" # Windows key for mod key

wmname = "Qtile"

# Autostart
@hook.subscribe.startup_once
def start_once():
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# Keybinds
keys = keybinds()

# Groups
groups = groups()

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
    ]
)

# Layouts
layouts = layouts()

# Default widget settings
widget_defaults = dict(
    font="IosevkaTerm Nerd Font",
    fontsize=13,
    padding=2,
)

extension_defaults = widget_defaults.copy()

# Screen declarations
screens = screen()

# Mouse (drag floating layouts)
mouse = mouse()

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = True
floats_kept_above = True
cursor_warp = False

# Floating window rules
floating_layout = layout.Floating(
    border_focus = colors.Purple,
    border_normal = colors.Normal,
    border_width = 2,
    
    float_rules=rules()
)

auto_fullscreen = True
focus_on_window_activation = "focus" # Auto switches to assigned group on application launch
reconfigure_screens = True
auto_minimize = True