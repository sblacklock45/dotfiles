# Layout configuration
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

from libqtile import layout
from libqtile.config import Match
from qtile_extras.layout.decorations import ConditionalBorderWidth

# Conditional border width currently used due to bug with firefox and thunderbird showing a gap
# between the application and the border (old X11 bug). Ensures no border for firefox and thunderbird only

# Default variables for all layouts
layout_vars = {"margin": 8,
               "border_focus": colors.Purple,
               "border_normal": colors.Inactive,
}

def layouts():
    return [
        layout.Max(**layout_vars,
               border_width=ConditionalBorderWidth(
                    default=2,
                    matches=[
                        (Match(wm_class="firefox"), 0),
                        (Match(wm_class="thunderbird"), 0)
                    ]
        )
    ),
    
    layout.MonadTall(**layout_vars,
                border_width=ConditionalBorderWidth(
                    default=2,
                    matches=[
                        (Match(wm_class="firefox"), 0),
                        (Match(wm_class="thunderbird"), 0)
                    ]
        )
    ),
    
    layout.MonadWide(**layout_vars,
                border_width=ConditionalBorderWidth(
                    default=2,
                    matches=[
                        (Match(wm_class="firefox"), 0),
                        (Match(wm_class="thunderbird"), 0),
                    ]
        )
    ),
    
    layout.Tile(**layout_vars,
                border_width=ConditionalBorderWidth(
                    default=2,
                    matches=[
                        (Match(wm_class="firefox"), 0),
                        (Match(wm_class="thunderbird"), 0)
                    ]
        )
    ),
]