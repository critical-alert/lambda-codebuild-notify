import json
import requests
import os

def notify(event, context):
    url = os.environ["WEBHOOK_URL"]

    build_result = event['detail']['build-status']
    project_name = event['detail']['project-name']
    project_link = 'https://ap-northeast-1.console.aws.amazon.com/codebuild/home?region=ap-northeast-1#/projects/{}/view'.format(project_name)

    if event['detail']['build-status'] == 'SUCCEEDED':
        color = "good"
    else:
        color = "danger"

    payload = {
        "icon_url": "https://s3-us-west-2.amazonaws.com/slack-files2/avatars/2017-06-26/204096259191_8600f2eea2765cda2210_72.png",
        "username": "CodeBuild",
        "attachments": [
            {
                "fallback": "Build " + build_result,
                "color":color,
                "title": "AWS CodeBuild Result",
                "title_link":project_link,
                "fields": [
                    {
                        "title": "Result",
                        "value":build_result,
                        "short": 'true'
                    },
                    {
                        "title": "Project Name",
                        "value":project_name,
                        "short": 'true'
                    }
                ],
            }
        ]
    }

    r = requests.post(url, json=(payload))
    return