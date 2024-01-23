import asana


class Asana:
    def __init__(self, token) -> None:
        self.client = asana.Client.access_token(token)

    def get_a_project(self, project_gid):
        return self.client.projects.get_project(project_gid)

    def get_tasks_in_project(self, project_gid):
        return self.client.tasks.get_tasks_for_project(project_gid)
