## Outline
- Command Line Interface
- Take master password, validate and show/save entries
- Automtically copy password to clipboard
- Generate random password (alphabets, numbers and special chars)


## Implentation

## Configure
- MASTER PASSWORD is first inputted while configuring, and the hash of it is saved in a file
- DEVICE SECRET is generated randomly, also stored in a file
- MASTER PASSWORD + DEVICE SECRET is passed into a hashing function(pbkdf) to create a valid key for AES-256. This is called Master Key
- The Master Key is then used to encrypt/decrypt new entries
- Encrypted fields: email, username, password
- Plain fields : sitename, url

## Add new entries
- Ask for MASTER PASSWORD
- Validate MASTER PASSWORD by hashing and checking with existing hash
- Make hash(DEVICE SECRET + MASTER PASSWORD) = Master Key
- Input fields of the entry - site name, site url, username, password
- Encrypt email, username, and password with MASTER KEY and save the fields into the database

## Get entry
- Input the field to search for. Like site name, site url, email, username
- Display all the entries that match the search. Password hidden by default.
- If user chooses to get the password (with -c flag), then
- Ask for MASTER PASSWORD
- Validate MASTER PASSWORD by hashing and checking with existing hash
- Make hash(DEVICE SECRET + MASTER PASSWORD) = Master key
- Decrypt the password and copy to the clipboard