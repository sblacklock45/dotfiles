# Screen configuration
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

import colors

from libqtile.config import Screen
from libqtile import bar, widget, qtile
from qtile_extras import widget

from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.widget.groupbox2 import GroupBoxRule

def screen():
    return [
        # Bottom bar
        Screen(
        bottom=bar.Bar(
            [
                widget.Spacer(length = 8),
                
                # Rofi menu launcher
                widget.TextBox(
                    text = "󰣇 ",
                    font = "IosevkaTerm Nerd Font",
                    fontsize = 17,
                    foreground = colors.Blue,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("sh /home/stevan/.config/rofi/launcher/launcher.sh"),},
                    
                ),

                widget.Spacer(length = 7),

                widget.Sep(
                    foreground = colors.Seperator,
                ),
             
                # Groupbox (qtile extras)
                widget.GroupBox2(
                    fontsize = 15,
                    padding_x = 9,
                    
                    rules=[
                        GroupBoxRule(line_colour=colors.Purple, text_colour="#7FBD85").when (focused=True),
                        GroupBoxRule(text_colour="#D24E4E").when (occupied=True),
                        GroupBoxRule(text_colour="#4A4F56").when (occupied=False)
                    ]
                ),

                widget.Sep(
                    foreground = colors.Seperator,
                ),

                widget.Spacer(
                    length = 8,
                ),

                # Current layout icon
                widget.CurrentLayoutIcon(),

                # Current layout
                widget.CurrentLayout(
                    padding = 8,
                ),

                widget.Sep(
                    foreground = colors.Seperator,
                ),

                widget.Spacer(
                    length = 8,
                ),

                # Name of current open application
                widget.WindowName(
                    max_chars = 60,
                ),
                
                widget.Spacer(
                    length = 5,
                    background = colors.Dock,
                ),

                # Disk free widget
                widget.DF(
                    partition = "/",
                    visible_on_warn = False,
                    format = " {uf} {m}B {r:.0f}%",
                    font = "JetBrainsMono Nerd Font",
                    fontsize = 12,
                    padding = 8,
                    foreground = colors.Grey,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("kitty -e btop"),},
                    decorations=[
                        RectDecoration(colour=colors.Green, filled=True, radius=4)
                    ]
                ),

                widget.Spacer(
                    length = 6,
                    background = colors.Dock,
                ),
                
                # Memory widget
                widget.Memory(
                    format = '{MemUsed: .0f} {mm}iB',
                    font = "JetBrainsMono Nerd Font",
                    fontsize = 12,
                    padding = 8,
                    foreground = colors.Grey,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("kitty -e btop"),},
                    decorations=[
                        RectDecoration(colour=colors.Orange, filled=True, radius=4)
                    ]
                ),

                widget.Spacer(
                    length = 6,
                    background = colors.Dock,
                ),

                # CPU widget
                widget.CPU(
                    format = ' {freq_current} GHz {load_percent} %',
                    font = "JetBrainsMono Nerd Font",
                    fontsize = 12,
                    padding = 8,
                    foreground = colors.Grey,
                    decorations=[
                        RectDecoration(colour=colors.OffWhite, filled=True, radius=4)
                    ]
                ),

                widget.Spacer(
                    length = 6,
                    background = colors.Dock,
                ),
 
                # Wifi widget
                widget.WiFiIcon(
                    active_colour = colors.Grey,
                    interface = "wlp2s0",
                    padding_x = 13,
                    padding_y = 11,
                    foreground = colors.Grey,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("nm-connection-editor"),},
                    decorations=[
                        RectDecoration(colour=colors.Blue, filled=True, radius=4)
                    ]
                ),

                widget.Spacer(
                    length = 6,
                    background = colors.Dock,
                ),

                # Volume control widget
                widget.PulseVolume(
                    font = "IosevkaTerm Nerd Font",
                    fontsize = 15,
                    foreground = colors.Grey,
                    emoji = True,
                    emoji_list = [' ',' ',' ',' '],
                    padding = 10,
                    volume_app = "pavucontrol",
                    decorations=[
                        RectDecoration(colour=colors.Yellow, filled=True, radius=4)
                    ]
                ),

                widget.Spacer(
                    length = 6,
                    background = colors.Dock,
                ),
                
                # Bluetooth widget
                widget.Bluetooth(
                    font = "JetBrainsMono Nerd Font",
                    fontsize = 15,
                    foreground = colors.Grey,
                    menu_background = colors.Dock,
                    highlight_colour = colors.Purple,
                    menu_foreground_highlighted = colors.Grey,
                    menu_font = "Cantarell",
                    menu_fontsize = 13,
                    highlight_radius = 4,
                    default_text = "󰂯",
                    padding = 12,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("blueman-manager"),},
                    decorations=[
                        RectDecoration(colour=colors.Lavender, filled=True, radius=4)
                    ]
                ),

                widget.Spacer(
                    length = 6,
                    background = colors.Dock,
                ),

                # Clock widget
                widget.Clock(
                    format="  %H:%M",
                    font = "JetBrainsMono Nerd Font",
                    fontsize = 12,
                    padding = 8,
                    foreground = colors.Grey,
                    decorations=[
                        RectDecoration(colour=colors.Green, filled=True, radius=4)
                    ]
                ),

                widget.Spacer(
                    length = 6,
                    background = colors.Dock,
                ),

                widget.TextBox(
                    text = "",
                    font = "JetBrainsMono Nerd Font",
                    fontsize = 12,
                    padding = 12,
                    foreground = colors.Grey,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("sh /home/stevan/.config/rofi/powermenu/powermenu.sh"),},
                    decorations=[
                        RectDecoration(colour=colors.Orange, filled=True, radius=4)
                    ]
                ),
            ],
            32, # Bar height
            border_width = [5,5,5,5],
            border_color = colors.Dock,
            background = colors.Dock,
            margin = [0,8,8,8],
        ),
    ),
]