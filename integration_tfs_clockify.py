from tfs_integration import TFS_Integration

tfs = TFS_Integration('')

projects = tfs.get_projects()

# Pegando os times e os membros de cada time
for project in projects:
    print ("ID: "+ project.id+" - "+project.name)
    teams = tfs.get_teams(project_id=project.id)
    for team in teams:
        print ("Team Name:" + team.name)
        team_members = tfs.get_team_members(project_id=project.id, team_id=team.id)
        for team_member in team_members:
            print("--->"+team_member.display_name)
            print(team_member)








