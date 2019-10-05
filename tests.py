import unittest
import requests
import HtmlTestRunner
import conf


class TestKbitAPI(unittest.TestCase):

    def test_user_login(self):
        print("API URL: " + conf.KBIT_API_URL)
        try:
            singup_request_for_login = {
                'email': 'test-login-user@user.local',
                'password': '1234',
                'firstName': 'User first name',
                'lastName': 'User last name'
            }
            url = conf.KBIT_API_URL + "/v1/auth/signup"
            requests.post(url, json=singup_request_for_login).json()
            url = conf.KBIT_API_URL + "/v1/auth/login"
            res = requests.post(url, json=singup_request_for_login)
            print(res.json())
            self.assertEqual(200, res.status_code)
        except Exception as ex:
            self.fail(ex)

    def test_create_user(self):
        print("API URL: " + conf.KBIT_API_URL)
        try:
            singup_request = {
                'email': 'test-create-user@user.local',
                'password': '1234',
                'firstName': 'User first name',
                'lastName': 'User last name'
            }
            url = conf.KBIT_API_URL + "/v1/auth/signup"
            print("Executing API CALL: " + url)
            res = requests.post(url, json=singup_request)
            print(res.json())
            self.assertEqual(200, res.status_code)
        except Exception as ex:
            self.fail(ex)

    def test_delete_user(self):
        self.assertEqual(2, 2)


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='reports', report_title="Kbit API integration tests results"))
