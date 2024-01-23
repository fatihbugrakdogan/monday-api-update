from monday_class import Monday
from asana_class import Asana


class Migrator:
    def __init__(self, monday_token, asana_token) -> None:
        self.monday_client = Monday(monday_token)
        self.asana_client = Asana(asana_token)

    def create_monday_board_with_asana_project(
        self, asana_project_id, monday_workspace_id
    ):
        asana_project_data = self.asana_client.get_a_project(asana_project_id)
        return self.monday_client.create_board(
            asana_project_data["name"], monday_workspace_id
        )
