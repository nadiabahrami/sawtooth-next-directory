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
"""Integration tests for role APIs"""
import requests
import pytest

from environs import Env

from rbac.common.logs import get_default_logger
from tests.rbac.api.assertions import assert_api_success
from tests.utilities.creation_utils import (
    create_next_admin,
    create_test_role,
    create_test_user,
    user_login,
)
from tests.utilities.db_queries import get_role_by_name
from tests.utils import (
    approve_proposal,
    delete_role_by_name,
    delete_user_by_username,
    get_outbound_queue_depth,
    get_outbound_queue_entry,
    get_proposal_with_retry,
    add_role_member,
)

ENV = Env()

ENABLE_LDAP_SYNC = ENV.int("ENABLE_LDAP_SYNC", 0)
ENABLE_NEXT_BASE_USE = ENV.int("ENABLE_NEXT_BASE_USE", 0)

LOGGER = get_default_logger(__name__)


@pytest.mark.skipif(
    ENABLE_NEXT_BASE_USE == 0, reason="Skipping test, NEXT base mode is not enabled"
)
def test_role_outq_insertion():
    """ Test the insertion of a new role created in NEXT-only mode.
        This test will only run if ENABLE_NEXT_BASE_USE is set to 1.
        - Create a user
        - Create a role
        - Check new entry in outbound_queue
    """
    user1_payload = {
        "name": "Test Unique User",
        "username": "testuniqueuser0501201901",
        "password": "123456",
        "email": "testuniqueuser1@biz.co",
    }
    with requests.Session() as session:
        create_next_admin(session)
        user_response1 = create_test_user(session, user1_payload)
        user1_result = assert_api_success(user_response1)
        user1_id = user1_result["data"]["user"]["id"]
        role_payload = {
            "name": "TestUniqueRole0501201903",
            "owners": user1_id,
            "administrators": user1_id,
            "description": "Test Unique Role 1",
        }
        role_response = create_test_role(session, role_payload)
        assert_api_success(role_response)

        outbound_queue_data = {
            "description": "Test Unique Role 1",
            "members": [],
            "remote_id": "",
        }
        expected_payload = {
            "data": outbound_queue_data,
            "data_type": "group",
            "provider_id": "NEXT-created",
            "status": "UNCONFIRMED",
            "action": "",
        }

        # Check status of new outbound_entry
        role_entry = get_role_by_name("TestUniqueRole0501201903")
        outbound_entry = get_outbound_queue_entry(role_entry[0])
        assert outbound_entry[0] == expected_payload

        delete_role_by_name("TestUniqueRole0501201903")
        delete_user_by_username("testuniqueuser0501201901")


def test_update_manager_outqueue():
    """ Creates a user and then updates their manager

    Manager is the second user created here."""
    # TODO: Rewrite this test after data gets sent to outbound_queue
    # after a user has their manager updated.
    user1_payload = {
        "name": "Test User 0521201901",
        "username": "test0521201901",
        "password": "123456",
        "email": "test0521201901@biz.co",
    }
    with requests.Session() as session:
        user2_response = create_next_admin(session)
        user2_result = assert_api_success(user2_response)
        user2_id = user2_result["data"]["next_id"]
        user1_response = create_test_user(session, user1_payload)
        user1_result = assert_api_success(user1_response)
        user1_id = user1_result["data"]["user"]["id"]
        start_depth = get_outbound_queue_depth()

        role_response = get_role_by_name("NextAdmins")
        add_role_member(session, role_response[0]["role_id"], {"id": user2_id})
        manager_payload = {
            "id": user2_id,
            "reason": "Integration test of adding role owner.",
            "metadata": "",
        }
        response = session.put(
            "http://rbac-server:8000/api/users/{}/manager".format(user1_id),
            json=manager_payload,
        )
        result = assert_api_success(response)
        proposal_response = get_proposal_with_retry(session, result["proposal_id"])
        assert_api_success(proposal_response)
        # Logging in as role owner
        env = Env()
        user_login(session, env("NEXT_ADMIN_USER"), env("NEXT_ADMIN_PASS"))
        # Approve proposal as role owner
        approve_proposal(session, result["proposal_id"])
        end_depth = get_outbound_queue_depth()
        assert end_depth > start_depth
        # TODO: Add tests to check for UNCONFIRMED outbound_queue entry status
        # when a user's manager gets updated.
        delete_user_by_username("test0521201901")
        delete_user_by_username("test0521201902")
        delete_role_by_name("NextAdmins")


def test_add_role_owner_outqueue():
    """Test adding an owner to a role.

    Creates two test users and a role with user1 as owner/admin,
    then adds the second user as role owner."""
    user1_payload = {
        "name": "Test User 0521201903",
        "username": "test0521201903",
        "password": "123456",
        "email": "test0521201903@biz.co",
    }
    user2_payload = {
        "name": "Test User 0521201904",
        "username": "test0521201904",
        "password": "123456",
        "email": "test0521201904@biz.co",
    }
    with requests.Session() as session:
        create_next_admin(session)
        user_response1 = create_test_user(session, user1_payload)
        user1_result = assert_api_success(user_response1)
        user1_id = user1_result["data"]["user"]["id"]
        user2_response = create_test_user(session, user2_payload)
        user2_result = assert_api_success(user2_response)
        user2_id = user2_result["data"]["user"]["id"]
        role_payload = {
            "name": "TestRole0521201901",
            "owners": user1_id,
            "administrators": user1_id,
            "description": "Test Role 1",
        }
        role_response = create_test_role(session, role_payload)
        role_result = assert_api_success(role_response)
        role_id = role_result["data"]["id"]
        start_depth = get_outbound_queue_depth()
        role_update_payload = {
            "id": user2_id,
            "reason": "Integration test of adding role owner.",
            "metadata": "",
        }
        response = session.post(
            "http://rbac-server:8000/api/roles/{}/owners".format(role_id),
            json=role_update_payload,
        )
        result = assert_api_success(response)
        proposal_response = get_proposal_with_retry(session, result["proposal_id"])
        assert_api_success(proposal_response)
        # Logging in as role owner
        user_login(session, user1_payload["username"], user1_payload["password"])
        # Approve proposal as role owner
        approve_proposal(session, result["proposal_id"])
        end_depth = get_outbound_queue_depth()
        assert end_depth > start_depth

        # Check status of new outbound_entry
        role_entry = get_role_by_name("TestRole0521201901")
        outbound_entry = get_outbound_queue_entry(role_entry[0])
        assert outbound_entry[0]["status"] == "UNCONFIRMED"

        delete_role_by_name("TestRole0521201901")
        delete_user_by_username("test0521201903")
        delete_user_by_username("test0521201904")


def test_add_role_member_outqueue():
    """Test adding a new member to a role.

    Creates two test users and a role using the first user,
    then adds the second user as member to role."""
    user1_payload = {
        "name": "Test Owner 0521201905",
        "username": "test0521201905",
        "password": "123456",
        "email": "testowner@biz.co",
    }
    user2_payload = {
        "name": "Test Member 0521201906",
        "username": "test0521201906",
        "password": "123456",
        "email": "testmember@biz.co",
    }
    with requests.Session() as session:
        create_next_admin(session)
        user1_response = create_test_user(session, user1_payload)
        user1_result = assert_api_success(user1_response)
        user1_id = user1_result["data"]["user"]["id"]
        user2_response = create_test_user(session, user2_payload)
        user2_result = assert_api_success(user2_response)
        user2_id = user2_result["data"]["user"]["id"]
        role_payload = {
            "name": "TestRole0521201902",
            "owners": user1_id,
            "administrators": user1_id,
            "description": "Test Role 3",
        }
        role_response = create_test_role(session, role_payload)
        role_result = assert_api_success(role_response)
        role_id = role_result["data"]["id"]
        start_depth = get_outbound_queue_depth()
        role_update_payload = {
            "id": user2_id,
            "reason": "Integration test of adding a member.",
            "metadata": "",
        }
        response = session.post(
            "http://rbac-server:8000/api/roles/{}/members".format(role_id),
            json=role_update_payload,
        )
        result = assert_api_success(response)
        proposal_response = get_proposal_with_retry(session, result["proposal_id"])
        assert_api_success(proposal_response)
        # Logging in as role owner
        user_login(session, user1_payload["username"], user1_payload["password"])
        # Approve proposal as role owner
        approve_proposal(session, result["proposal_id"])
        end_depth = get_outbound_queue_depth()
        assert end_depth > start_depth

        # Check status of new outbound_entry
        role_entry = get_role_by_name("TestRole0521201902")
        outbound_entry = get_outbound_queue_entry(role_entry[0])
        assert outbound_entry[0]["status"] == "UNCONFIRMED"

        delete_role_by_name("TestRole0521201902")
        delete_user_by_username("test0521201905")
        delete_user_by_username("test0521201906")
