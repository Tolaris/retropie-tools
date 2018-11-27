# About

Tools for managing Retropie or game ROMS and disk images.

# backup-saves.py

Backs up your save files under RetroPie/roms to a .tar.gz, or restores
them. Useful when overwriting your RetroPie with a new build. You must
still copy this file somewhere (not on the Pi itself).

## Usage

```
git clone git@github.com:Tolaris/retropie-tools.git
retropie-tools/backup-saves.py -f /tmp/saves.tgz -r /home/pi/RetroPie/roms -v backup
scp /tmp/saves.tgz $user@$somewhere:/home/$user/

# Now reinstall/reimage your Retropie

scp $user@$somewhere:/home/$user/ /tmp/saves.tgz
git clone git@github.com:Tolaris/retropie-tools.git
retropie-tools/backup-saves.py -f /tmp/saves.tgz -r /home/pi/RetroPie/roms -v restore
```

# rename-roms.py

A simple script to move your collection of game ROMs and disk images
into directories named for the release region.

## Usage

```
usage: rename-roms.py \[options\] \[DIR\] \[...\]
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
