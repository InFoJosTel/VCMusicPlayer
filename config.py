#!/usr/bin/env python3
# Copyright (C) @ZauteKm
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import os
import re
from youtube_dl import YoutubeDL
ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
C_PLAY=False
Y_PLAY=False
STREAM=os.environ.get("STREAM_URL", "https://t.me/tgbotsproject")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
regex_ = r"http.*"
match_ = re.match(regex_,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[-1]
elif STREAM.startswith("https://t.me/tgbotsproject"):
    try:
        msg_id=STREAM.split("/", 4)[4]
        finalurl=int(msg_id)
        Y_PLAY=True
    except:
        finalurl="https://eu10.fastcast4u.com/clubfmuae"
        print("Unable to fetch youtube playlist, starting CLUB FM")
        pass
elif match_:
    finalurl=STREAM 
else:
    C_PLAY=True
    finalurl=STREAM

class Config:
    ADMIN = os.environ.get("ADMINS", '')
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("26741385", ''))
    CHAT = int(os.environ.get("CHAT", ""))
    LOG_GROUP=os.environ.get("1002072954694", "")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL=finalurl
    CPLAY=C_PLAY
    YPLAY=Y_PLAY
    SHUFFLE=bool(os.environ.get("SHUFFLE", True))
    DELETE_HISTORY=bool(os.environ.get("DELETE_HISTORY", True))
    LIMIT=int(os.environ.get("LIMIT", 1500))
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "N")
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    if REPLY_MESSAGE:
        REPLY_MESSAGE=REPLY_MESSAGE
    else:
        REPLY_MESSAGE=None
    EDIT_TITLE = os.environ.get("EDIT_TITLE", True)
    if EDIT_TITLE == "NO":
        EDIT_TITLE=None
    DURATION_LIMIT=int(os.environ.get("MAXIMUM_DURATION", 120))
    DELAY = int(os.environ.get("DELAY", 10))
    API_HASH = os.environ.get("8221180729601e66281bff01dcc7d9ec", "")
    BOT_TOKEN = os.environ.get("6743972045:AAH-NVrWa508y0FxEC88-QjWNpYpoZR80eY", "")     
    SESSION = os.environ.get("BQGYCokAdke2AeQRwgiJBZMBmAEToOUsi5DIdO5772q9qW0bvKGJ3UgJ6fRLQG-hfdKbtdqmWkhqFQkKE1m1NUjzvBRyJ_CetvAkxBQm6VakwPIe9xMv5w2H1c00Pht-WmAWtXX8AMZAy04Zt2UAZ15TAmRC02wNzc2xYsfkaZiVDl2nHyQpeLg_qhVg90xEuENS_G1UFGf_tpWrx8_pQ26_xQ0KY9RwA55lZEBhgjN_P8rKZYfwog6-JWjL3--6WwDqzqWl941jj0BPY2MkugUEMOlrjr5joeSrKxaAvJF5hrfRTd8IR2RkybnVrm7UVD5qV4fW4YleuFRIhgeCDqHbu8nvnQAAAAGR-NjNAQ", "")
    playlist=[]
    msg = {}
    CONV = {}
