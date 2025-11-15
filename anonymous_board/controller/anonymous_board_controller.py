from typing import List

from fastapi import APIRouter, HTTPException

from anonymous_board.entity.anonymous_board import AnonymousBoard

from anonymous_board.controller.request.create_anonymous_board_request import CreateAnonymousBoardRequest
from anonymous_board.controller.response.anonymous_board_response import AnonymousBoardResponse

from anonymous_board.service.anonymous_board_service_impl import AnonymousBoardServiceImpl



anonymous_board_controller = APIRouter(prefix="/board")
anonymous_board_service = AnonymousBoardServiceImpl.getInstance()

# @PostMapping("/create") 
@anonymous_board_controller.post(
    "/create", response_model=AnonymousBoardResponse
) 
def create_anonymous_board(request: CreateAnonymousBoardRequest): 

    createdBoard = anonymous_board_service.create(request.title, request.content)

    return AnonymousBoardResponse( 
        id=createdBoard.id, 
        title=createdBoard.title, 
        content=createdBoard.content, 
        created_at=createdBoard.created_at 
    )

@anonymous_board_controller.get(
    "/list", response_model=List[AnonymousBoardResponse]
)
def list_anonymous_board():
    boardList = anonymous_board_service.list()
    return [
        AnonymousBoardResponse.model_validate(anonymous_board) for anonymous_board in boardList
    ]


@anonymous_board_controller.get(
    "/{board_id}", response_model=AnonymousBoardResponse
)
def get_anonymous_board(board_id: str):
    try:
        anonymous_board = anonymous_board_service.read(board_id=board_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Board Not Found")
    return AnonymousBoardResponse.model_validate(anonymous_board)