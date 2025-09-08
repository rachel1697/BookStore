import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api_helpers.helpers import APIHelpers
from api_validators.validate_apis import ValidateAPIs
import pytest

@pytest.mark.skip_or_continue_test_based_on_value("Continue")
@pytest.mark.test_marker
def test_create_user(generate_token,base_url,user_name,password,testrun):

    apihelpers = APIHelpers(generate_token,base_url,user_name,password)
    validateapis = ValidateAPIs()

    response = apihelpers.create_user()

    validateapis.validate_create_user(response)

    testrun_value = testrun

    print(testrun_value)












