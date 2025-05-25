import os
import requests

ORION_URL = os.getenv("ORION_URL", "http://orion:1026")

session = requests.Session()
session.headers.update({"Content-Type": "application/ld+json"})
