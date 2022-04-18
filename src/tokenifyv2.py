import requests
import json


def tokenify(username, password):
    with requests.session() as req:
        
        userInfoReq = req.post(
            "https://api.prodigygame.com/game-auth-api/v4/user",
            headers={"content-type": "application/json"},
            data=json.dumps(
                {
                    "identityToken": "", # Some sort of indentification token that isn't the main token,
                    "userID": "" # username of account,
                }
            ),
        )

        # Objective: userInfoReq.json()['token']
