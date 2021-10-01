import json
from typing import Dict
from uuid import UUID


def get_request_info(event: Dict) -> (UUID, Dict):
    if (
        "requestContext" in event and
        "authorizer" in event['requestContext'] and
        "claims" in event['requestContext']['authorizer'] and
        "sub" in event['requestContext']['authorizer']['claims'] and
        isinstance(event['requestContext']['authorizer']['claims']['sub'], str)
    ):
        user_id = UUID(event['requestContext']['authorizer']['claims']['sub'])
    else:
        user_id = None

    if 'body' in event and isinstance(event['body'], str):
        body = json.loads(event['body'].replace("\\n", ""))
    else:
        body = None

    return (user_id, body)
