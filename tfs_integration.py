from vsts.vss_connection import VssConnection
from msrest.authentication import BasicAuthentication
import pprint

class TFS_Integration():
    def __init__(self, organization_url, PAT):
        # Fill in with your personal access token and org URL
        self.personal_access_token = PAT
        self.organization_url = organization_url

        # Create a connection to the org
        credentials = BasicAuthentication('', self.personal_access_token)
        self.connection = VssConnection(base_url=self.organization_url, creds=credentials)

        # Get a client (the "core" client provides access to projects, teams, etc)
        self.core_client = self.connection.get_client('vsts.core.v4_0.core_client.CoreClient')

    def get_projects(self):
        return self.core_client.get_projects()

    def get_teams(self, project_id):
        return self.core_client.get_teams(project_id)

    def get_team_members(self, project_id, team_id):
        return self.core_client.get_team_members(project_id,team_id)