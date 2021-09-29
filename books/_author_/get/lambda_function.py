import json
import os
from dataclasses import asdict
from lambda_services.services import get_request_info
from pypendency.builder import container_builder
from pypendency.loaders.yaml_loader import YamlLoader

from domain.serializers.book_serializer import BookSerializer


def lambda_handler(event, context):
    YamlLoader(container_builder).load_dir('{}/domain/_dependencies/'.format(os.getcwd()))
    YamlLoader(container_builder).load_dir('{}/_dependencies/'.format(os.getcwd()))

    (user_id, body) = get_request_info(event)

    use_case = container_builder.get(
        "use_cases.get_books_by_author_use_case.GetBooksByAuthorUseCase"
    )

    try:
        author_id = UUID(event['pathParameters']['author'])
    except Exception:
        status_code = 400
        return {
            'statusCode': status_code
        }

    books = use_case.get(author_id)
    book_serializer = BookSerializer(books)
    books_json = book_serializer.serialize()

    status_code = 200

    return {
        'statusCode': status_code,
        'body': books_json
    }
