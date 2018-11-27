# About

Tools for managing Retropie or game ROMS and disk images.

# Installation

```
git clone git@github.com:Tolaris/retropie-tools.git
sudo cp retropie-tools/*.py /usr/local/bin/
```

# backup-saves.py

Backs up your save files under RetroPie/roms to a .tar.gz, or restores
them. Useful when overwriting your RetroPie with a new build. You must
still copy this file somewhere (not on the Pi itself).

## Usage

```
retropie-tools/backup-saves.py -f /tmp/saves.tgz -r /home/pi/RetroPie/roms -v backup
scp /tmp/saves.tgz $user@$somewhere:/home/$user/

# Now reinstall/reimage your Retropie, then install as above.

scp $user@$somewhere:/home/$user/ /tmp/saves.tgz
retropie-tools/backup-saves.py -f /tmp/saves.tgz -r /home/pi/RetroPie/roms -v restore
```

# rename-roms.py

A simple script to move your collection of game ROMs and disk images
into directories named for the release region.

## Usage

```
# Test first with --dry-run:
rename-roms.py --dry-run -v ~/Retropie/roms

# Read output, make sure you are happy with changes. Then do it for real:
rename-roms.py -v ~/Retropie/roms
```

For a list of options, run: rename-roms.py -h

## Adding your own rules

To modify, just add rules to get_rules(). These are executed in order,
and return the first match. For example, a ROM named

```
Example Game Name (USA, Europe, Japan).zip
```

will be moved into the USA folder because that rule comes first:

```
USA/Example Game Name (USA, Europe, Japan).zip
```

You may wish to reorder the rules to prefer your region.
