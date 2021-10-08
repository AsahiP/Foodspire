"""drop db, create db, automatically populate db with data """

import os
import json

from random import choice, randint
from datetime import datetime

import crud
import model
import server

