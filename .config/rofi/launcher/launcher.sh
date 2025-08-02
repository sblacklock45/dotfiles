#!/usr/bin/env bash
# Load theme style

dir="$HOME/.config/rofi/launcher"
theme='style'

## Run
rofi \
    -show drun \
    -theme ${dir}/${theme}.rasi \
    -no-levenshtein-sort \
    -disable-history \
    -hover-select -me-select-entry '' -me-accept-entry MousePrimary