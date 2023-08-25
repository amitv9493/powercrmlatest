import os
from rest_framework.response import Response

import requests

class Token:
    url = "https://api.amazon.com/auth/o2/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    def __init__(
        self,
    ) -> None:
        self._user_data = None
        self._access_token = None
        self._refresh_token = None
        
        
    def initial_data(self):
        self._access_token = self._user_data.access_token
        self._refresh_token = self._user_data.refresh_token  

    def GenerateAccessToken(self, grant_type: str) -> None:
        if grant_type == "authorization_code":
            token = self._user_data.code
            type = "code"
        elif grant_type == "refresh_token":
            token = self._user_data.refresh_token
            type = "refresh_token"

        payload = f"grant_type={grant_type}&{type}={token}&client_id={os.getenv('client_id')}&client_secret={os.getenv('client_secret')}"

        response = requests.post(self.url, headers=self.headers, data=payload)

        token_data = response.json()

        if token_data.get("error"):
            return Response(token_data, status=400)

        self._access_token = token_data.get(
            "access_token"
        )
        self._refresh_token = token_data.get(
            "refresh_token"
        )

    @property
    def access_token(self) -> str:
        return self._access_token

    @property
    def refresh_token(self) -> str:
        return self._refresh_token
    
    @property
    def user_data(self):
        return self._user_data
    
    @user_data.setter
    def user_data(self,user_data):
        self._user_data = user_data
        