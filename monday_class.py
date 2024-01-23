from monday import MondayClient
from monday.resources.types import BoardKind


class Monday:
    def __init__(self, token):
        self.monday_client = MondayClient(token)

    def create_board(self, board_name, workspace_id):
        self.monday_client.boards.create_board(
            board_name, BoardKind.SHARE, workspace_id
        )
