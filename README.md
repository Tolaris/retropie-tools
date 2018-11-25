# About

Tools for managing Retropie or game ROMS and disk images.

# rename-roms.py

A simple script to move your collection of game ROMs and disk images
into directories named for the release region.

## Usage

usage: rename-roms.py \[options\] \[DIR\] \[...\]

For a list of options, run: rename-roms.py -h

## Adding your own rules

To modify, just add rules to get_rules(). These are executed in order,
and return the first match. For example, a ROM named

Example Game Name (USA, Europe, Japan).zip

will be moved into the USA folder because that rule comes first:

USA/Example Game Name (USA, Europe, Japan).zip

You may wish to reorder the rules to prefer your region.
