
class ValidateAPIs:

    def validate_create_user(self,response):
        assert response.status_code == 201, f"Resource not created. Status code is {response.status_codee}"

    def validate_delete_user(self,response):
        try:
            assert response.status_code == 204
            response_json = response.json()
            print(response_json)

        except AssertionError as e:
            print(f"Assertion Error: {e}")
            response_json = response.json()
            print('response json: ',response_json)
            assert response.status_code == 401
            assert response_json["message"] == "User not authorized!", "Displayed message is not correct"


