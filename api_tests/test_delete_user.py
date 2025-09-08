from api_helpers.helpers import APIHelpers
from api_validators.validate_apis import ValidateAPIs
import pytest

@pytest.mark.skip_or_continue_test_based_on_value("Continue")
def test_delete_user(generate_token, base_url, user_name, password):

    apihelpers = APIHelpers(generate_token, base_url, user_name, password)
    validateapis = ValidateAPIs()

    response = apihelpers.create_user()

    validateapis.validate_create_user(response)

    delete_response = apihelpers.delete_user_without_auth_header(response)

    validateapis.validate_delete_user(delete_response)

    delete_response = apihelpers.delete_user(response)

    validateapis.validate_delete_user(delete_response)






