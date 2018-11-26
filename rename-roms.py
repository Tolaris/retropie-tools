#!/usr/bin/env python
"""Move ROMs into folders by country."""

from __future__ import print_function

import argparse
import os
import re
import sys

# defaults
VERSION = "1.1.1"
AUTHOR = "tyler@tolaris.com"
args = None

def die(msg):
  """Print message and exit with error."""
  print(msg)
  sys.exit(1)

def get_rules():
  """Return a 2-dimensional list of rename rules to be parsed in order.
  [[regex, directoryname], ...]
  """
  rules = [
    [re.compile(r'^.*\[BIOS\].*$', re.I), 'BIOS'],
    [re.compile(r'^.*\[T-Eng.*\].*$', re.I), 'Translations'],
    [re.compile(r'^.*\(.*Unl.*\).*$', re.I), 'Unlicensed'],
    [re.compile(r'^.*\(.*Hack.*\).*$', re.I), 'Hacks'],
    [re.compile(r'^.*\((Beta|(Putative )?Proto).*\).*$', re.I), 'Prototype'],
    [re.compile(r'^.*\((.*(USA|Canada|World).*|J?UE?)\).*$', re.I), 'USA'],
    [re.compile(r'^.*\((.*(Europe|Denmark|France|Germany|Italy|Netherlands|Spain|Sweden).*|J?E\)).*$', re.I), 'Europe'],
    [re.compile(r'^.*\((.*Japan.*|J)\).*$', re.I), 'Japan'],
    [re.compile(r'^.*\(.*(Asia|China|Hong Kong|Korea|Taiwan).*\).*$', re.I), 'Asia'],
    [re.compile(r'^.*\(.*(Latin|Brazil).*\).*$', re.I), 'Latin'],
    [re.compile(r'^.*\(.*Australia.*\).*$', re.I), 'Australia'],
    [re.compile(r'^.*\(.*Unknown.*\).*$', re.I), 'Unknown'],
  ]
  return rules

def get_directory_name(filename, rules):
  """Return the destination directory for a ROM."""
  for rule in rules:
    if rule[0].match(filename):
      return rule[1]
  return None

def move_file(filename, rules):
  """Move a ROM to its correct destination directory."""
  global args
  if os.path.isfile(filename):
    subdirname = get_directory_name(filename, rules)
    head, tail = os.path.split(filename)
    if head is not None and subdirname is not None:
      filename_new = os.path.join(head, subdirname, tail)
      args.verbose and print("{}\t->\t{}".format(filename, filename_new))
      if not args.dry_run:
        os.renames(filename, filename_new)

def main_app():
  """Main entry point for CLI."""
  # argparse
  global args
  usage = "%(prog)s [options] [DIR] [...]"
  version = "%(prog)s " + VERSION + ", by " + AUTHOR
  parser = argparse.ArgumentParser(usage=usage, description=__doc__)
  parser.add_argument("roms", metavar="DIR", nargs="*", help="filenames of ROMs to process")
  parser.add_argument("--version", action="version", version=version)
  parser.add_argument("-v", "--verbose", action="store_true", help="display verbose output")
  parser.add_argument("-n", "--dry-run", action="store_true", help="dry run, don't rename files")
  args = parser.parse_args()
  if not args.roms:
    parser.print_help()
    parser.exit(1)

  rules = get_rules()

  for filename in args.roms:
    move_file(filename, rules)

if __name__ == '__main__':
  main_app()
