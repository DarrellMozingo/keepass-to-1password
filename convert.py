from lxml import etree

def main():
    tree = etree.parse("Passwords.xml")

    for entry in tree.getroot().findall('.//Entry'):
        if entry.getparent().tag == 'History':
            continue

        # title,website,username,password,notes
        print('title: ' + getField('Title', entry))
        print('website: ' + getField('URL', entry))
        print('username: ' + getField('UserName', entry))
        print('password: ' + getField('Password', entry))
        print('notes: ' + repr(getField('Notes', entry)))
        print('\n')

def getField(fieldName, entry):
    all_strings = entry.findall('./String')
    matching_string = next(filter(lambda e: e.find('Key').text == fieldName, all_strings))
    return matching_string.find('./Value').text or '<empty>'

if __name__ == "__main__":
    main()
