"""
.. See the NOTICE file distributed with this work for additional information
   regarding copyright ownership.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from flask import Flask
from flask_restful import Api, Resource

from rest.mg_auth import authorized

APP = Flask(__name__)

class TokenCheck(Resource):
    """
    Class to handle checking if the token returns a valid user name
    """

    @authorized
    def get(self, user_id):
        """
        Test to see if it is possible to get the user_id
        """
        msg = "Congratulations, welcome to the MuG VRE"
        if user_id is None:
            msg = "Are you sure that you have a valid token?"

        return {
            'user_id': user_id,
        }

# Define the URIs and their matching methods
REST_API = Api(APP)

#   Token Checker
REST_API.add_resource(TokenCheck, "/mug/api/check", endpoint='token-check')


# Initialise the server
if __name__ == "__main__":
    APP.run(port=5000, debug=True, use_reloader=False)
