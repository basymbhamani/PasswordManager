import hashlib
import random
import string
import sys

from getpass import getpass

from utils.dbconfig import dbconfig

from rich import print as printc
from rich.console import Console

console = Console()

def generateDeviceSecret(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k = length))

def config():
    # Create a database
    db = dbconfig()
    cursor = db.cursor()
    
    try:
        cursor.execute("CREATE DATABASE pm")
    except Exception as e:
        printc("[red][!] An error occured while trying to create db.")
        console.print_exception(show_locals=True)
        sys.exit(0)
    printc("[green][+][/green] Databse 'pm' created")   
    
    # Create tables
    query = "CREATE TABLE pm.secrets (masterpassword_hash TEXT NOT NULL, device_secret TEXT NOT NULL)"
    res = cursor.execute(query)
    printc("[green][+][/green] Table 'secrets' created ")
    
    query = "CREATE TABLE pm.entries (sitename TEXT NOT NULL, siteurl TEXT NOT NULL, email TEXT, username TEXT, password TEXT NOT NULL)"
    res = cursor.execute(query)
    printc("[green][+][/green] Table 'entries' created ")
    
    while 1:
        mp = getpass("Choose a MASTER PASSWORD: ")
        if mp==getpass("Re-type: ") and mp!="":
            break;
        printc("[yellow][-] Please try again.[/yellow]")
        
    # Hash the MASTER PASSWORD
    hashed_mp = hashlib.sha256(mp.encode()).hexdigest()
    printc("[green][+][/green] Generated hash of MASTER PASSWORD")
    
    # Generate a DEVICE SECRET
    ds = generateDeviceSecret()
    
    #Add them to db
    query = "INSERT INTO pm.secrets (masterpassword_hash, device_secret) values (%s, %s)"
    val = (hashed_mp, ds)
    cursor.execute(query, val)
    db.commit()
    
    printc("[green][+][/green] Added to the database")
    printc("[green][+] Configuration done![/green]")
    
    db.close()
    
    
config()