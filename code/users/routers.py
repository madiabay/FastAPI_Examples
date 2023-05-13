from fastapi import APIRouter

from . import handlers


handler = handlers.UserHandler()
router = APIRouter(prefix='/users', tags=['users'])

router.add_api_route(
    '/',
    endpoint=handler.create_user,
    methods=['post'],
    response_model_exclude={'username'},
)
