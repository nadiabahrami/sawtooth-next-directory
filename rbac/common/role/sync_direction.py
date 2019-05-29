# Copyright 2019 Contributors to Hyperledger Sawtooth
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
"""Implements setting the sync_direction for roles"""
import time
import rethinkdb as r
from rbac.common.logs import get_default_logger
from rbac.providers.common.db_queries import connect_to_db

LOGGER = get_default_logger(__name__)


def set_sync_direction(role_id, direction):
    """Sets the sync_direction of role_id.

    Args:
        role_id: The next_id of the role.
        direction: str with value of "INBOUND" or "OUTBOUND"

    Returns:
        RethinkDB output of the update query.
    """
    conn = connect_to_db()
    retry = 0
    while retry < 3:
        try:
            response = (
                r.table("roles")
                .get_all(role_id, index="role_id")
                .update({"metadata": {"sync_direction": direction}})
                .run(conn)
            )
        except r.errors.ReqlOpFailedError:
            time.sleep(3)
            retry += 1
        else:
            break
    else:
        LOGGER.warning("Max retries reached when setting sync_direction. Not set.")
    conn.close()
    return response


def set_status(role_id, status):
    """Sets the status of user via next_id.
    Args:
        role_id: str: id of the role.
        status: str: with value of "CONFIRMED" or "UNCONFIRMED"

    Returns:
        RethinkDB output of the update query.
    """
    conn = connect_to_db()
    retry = 0
    while retry < 3:
        try:
            response = (
                r.table("roles")
                .get_all(role_id, index="role_id")
                .update({"metadata": {"status": status}})
                .run(conn)
            )
        except r.errors.ReqlOpFailedError:
            time.sleep(3)
            retry += 1
        else:
            break

    else:
        LOGGER.warning("Max retries reached when setting sync_direction. Not set.")
    conn.close()
    return response
