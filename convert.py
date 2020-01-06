from lxml import etree
import csv

def main():
    tree = etree.parse("Passwords.xml")

    csv_rows = []

    for entry in tree.getroot().findall('.//Entry'):
        if entry.getparent().tag == 'History':
            continue

        print('title: ' + getField('Title', entry))
        print('website: {}'.format(getField('URL', entry)))
        print('username: {}'.format(getField('UserName', entry)))
        print('password: {}'.format(getField('Password', entry)))
        print('notes: {}'.format(repr(getField('Notes', entry))))
        print('\n')

        # title,website,username,password,notes
        csv_rows += [[getField('Title', entry),
                      getField('URL', entry),
                      getField('UserName', entry),
                      getField('Password', entry),
                      getField('Notes', entry)]]

    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csv_rows)

def getField(fieldName, entry):
    all_strings = entry.findall('./String')
    matching_string = next(filter(lambda e: e.find('Key').text == fieldName, all_strings))
    return matching_string.find('./Value').text

if __name__ == "__main__":
    main()
