import json
import os
import sentry_sdk
from dataclasses import asdict
from lambda_services.services import get_request_info
from pypendency.builder import container_builder
from pypendency.loaders.yaml_loader import YamlLoader
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration
from uuid import UUID


sentry_sdk.init(
    dsn=os.getenv('SENTRY_DNS'),
    integrations=[AwsLambdaIntegration(timeout_warning=True)]
)

def lambda_handler(event, context):
    YamlLoader(container_builder).load_dir('{}/domain/_dependencies/'.format(os.getcwd()))
    YamlLoader(container_builder).load_dir('{}/_dependencies/'.format(os.getcwd()))

    (user_id, body) = get_request_info(event)

    use_case = container_builder.get(
        "use_cases.get_wa_assets_use_case.GetWAAssetsUseCase"
    )

    try:
        wa_id = UUID(event['pathParameters']['wa'])
    except Exception:
        status_code = 400
        return {
            'statusCode': status_code
        }

    assets = use_case.get(user_id, wa_id)
    assets_json = [] #TODO: Introduce serializers
    for asset in assets:
        asset.id = str(asset.id)
        assets_json.append(asdict(asset))

    status_code = 200

    return {
        'statusCode': status_code,
        'body': assets_json
    }
