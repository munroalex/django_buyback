""" Module to update Eve online SDE """

import os
import bz2
import shutil
import sqlite3
from pathlib import Path
from urllib.request import pathname2url
#import logging
import wget


def dl_and_dc(url: str, filename: str) -> None:
    """ Download new SDE from fuzzworks. Decompress to temporary file. """
    # Download the file from the URL.
    wget.download(url)
    # Extract from BZ2 format to new temporary filename.
    if Path("SDE.sqlite").is_file():
        with bz2.BZ2File(filename) as fr, open("SDEtemp.sqlite","wb") as fw:
            shutil.copyfileobj(fr,fw)
    else:
        with bz2.BZ2File(filename) as fr, open("SDE.sqlite","wb") as fw:
            shutil.copyfileobj(fr,fw)
    os.remove("sqlite-latest.sqlite.bz2")

def check_db(db: str) -> int:
    """ Attempt to connect to new SQLite file. If successful, rename and delete old """
    try:
        dburi: str = f'file:{pathname2url(db)}?mode=rw'
        conn = sqlite3.connect(dburi, uri=True)
        cur = conn.cursor()
        cur.execute("SELECT typeName, typeID FROM invTypes WHERE typeName = ?", ["Tritanium"])
        rows: list = cur.fetchall()
        for row in rows:
            if row[1] == 34:
                conn.close()
                continue
            return 0
    except sqlite3.OperationalError:
        return 0
    if Path("SDE.sqlite").is_file():
        os.rename("SDE.sqlite", "oldSDE.sqlite")
        os.rename("SDEtemp.sqlite", "SDE.sqlite")
        os.remove("oldSDE.sqlite")
    return 1

def updater() -> None:
    # URL that downloads the latest SDE version in SQLite format.
    URL = 'https://www.fuzzwork.co.uk/dump/sqlite-latest.sqlite.bz2'
    # File name that the downloaded SDE is saved as.
    FILENAME = 'sqlite-latest.sqlite.bz2'

    dl_and_dc(URL, FILENAME)
    if check_db("SDEtemp.sqlite") == 1:
        print("Update Success.")

updater()