# Copyright 2018 Contributors to Hyperledger Sawtooth
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -----------------------------------------------------------------------------
"""Fixtures for creating objects during testing"""
from environs import Env
import logging
import requests

from rbac.server.api.utils import check_admin_status
from tests.utils import (
    add_role_member,
    create_test_role,
    create_test_user,
    get_user_in_db_by_email,
)

def create_admin_user():
    """Creates admin user for user creation in tests"""
    logging.critical("CREATING ADMIN")
    admin_id = ""
    env = Env()
    admin_user = {
        "name": env("NEXT_ADMIN_NAME"),
        "username": env("NEXT_ADMIN_USER"),
        "email": env("NEXT_ADMIN_EMAIL"),
        "password": env("NEXT_ADMIN_PASS"),
    }
    with requests.Session() as session:
        logging.critical("0th line")
        try:
            logging.critical("1st line")
            admin_id = create_test_user(session, admin_user).json()["data"]["user"]["id"]
            logging.critical("2nd line")

            next_admins_role = {
                "name": "NextAdmins",
                "owners": admin_id,
                "administrators": admin_id,
            }
            logging.critical("right before sending payload")

            role_id = create_test_role(session, next_admins_role).json()["data"]["id"]
            logging.critical("ROLE ID: " + role_id)

            add_role_member(session, role_id, admin_id)
            logging.critical("CREATION OF ADMIN: " + admin_id)

            print("CREATION OF ADMIN: " + admin_id)
        except:
            logging.critical("Admin user already exists!")
            print("ADMIN USER ALREADY EEXISTS!")
            admin_id = get_user_in_db_by_email(env("NEXT_ADMIN_EMAIL"))

    return admin_id
        

