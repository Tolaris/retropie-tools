#!/usr/bin/env python
"""Backup all emulator save files into tgz archive."""

from __future__ import print_function

import argparse
import os
import re
import sys
import tarfile

# defaults
VERSION = "1.0.0"
AUTHOR = "tyler@tolaris.com"
args = None


def die(msg):
  """Print message and exit with error."""
  print(msg)
  sys.exit(1)


def get_save_files(rom_dir):
  """Walk rom directory, and return a list of save filenames relative to it."""
  # regex matching filenames ending like .state, .state1, .st2, .srm, .rtc
  save_regex = re.compile(".*\.(state|srm|st|rtc)[0-9]*$")

  save_files = []
  os.chdir(rom_dir)

  for root, dirs, files in os.walk("."):
    for filename in files:
      if save_regex.match(filename):
        save_file = os.path.join(root, filename)
        save_files.append(save_file)
  return save_files


def create_tar_file(tar_file, save_files):
  """Create a tar.gz containing save_files."""
  if tar_file[-2:].lower() == "gz":
    mode = "w:gz"
  else:
    mode = "w"
  with tarfile.open(tar_file, mode) as tar:
    for save_file in sorted(save_files):
      args.verbose and print("Adding {}".format(save_file))
      tar.add(save_file)
  args.verbose and print("Wrote {}".format(tar_file))


def extract_tar_file(tar_file, rom_dir):
  """Extract tar.gz of save_files to rom_dir. Doesn't verify tar.gz contains
     only safe paths."""
  if tar_file[-2:].lower() == "gz":
    mode = "r:gz"
  else:
    mode = "r"
  with tarfile.open(tar_file, mode) as tar:
    if args.verbose:
      tar.list()
    tar.extractall(rom_dir)
  args.verbose and print("Extracted contents of {} to {}".format(tar_file, rom_dir))

def main_app():
  """Main entry point for CLI."""
  # argparse
  global args
  usage = "%(prog)s [options] -f [TAR_FILE] -r [ROM_DIR] [backup|restore]"
  version = "%(prog)s " + VERSION + ", by " + AUTHOR
  parser = argparse.ArgumentParser(usage=usage, description=__doc__)
  parser.add_argument("cmd", help="action to take: 'backup' or 'restore'")
  parser.add_argument("--version", action="version", version=version)
  parser.add_argument("-f", "--tar-file", default="/tmp/saves.tgz", help="filename of tar.gz file to read or write (default: %(default)s)")
  parser.add_argument("-r", "--rom-dir", default="/home/pi/RetroPie/roms", help="RetroPie roms directory (default: %(default)s)")
  parser.add_argument("-v", "--verbose", action="store_true", help="display verbose output")
  parser.add_argument("-n", "--dry-run", action="store_true", help="dry run, don't write changes")
  args = parser.parse_args()

  if args.cmd == "backup":
    save_files = get_save_files(args.rom_dir)
    create_tar_file(args.tar_file, save_files)
  elif args.cmd == "restore":
    extract_tar_file(args.tar_file, args.rom_dir)
  else:
    parser.print_help()
    parser.exit(1)


if __name__ == '__main__':
  main_app()
