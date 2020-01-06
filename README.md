# Keepass -> 1Password Converter

Specifically tested with [MacPass](https://macpassapp.org). Writes out the title, url, username, password, and notes for each entry. Doesn't attempt anything fancy like tagging or converting into different 1Password types.

Usage:

1. In MacPass, `File` -> `Export` -> `XML`. Save in this folder (named `Passwords.xml`, or update the script)
1. `pip install -r requirements.txt`
1. `python convert.py`
1. Import `output.csv` into 1Password
