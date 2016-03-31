from pyramid.view import view_config

@view_config(route_name='home', renderer='../templates/mytemplate.pt')
def hydro_view(request):
    return {'project': 'Hydro'}

@view_config(route_name='poop', renderer='../templates/mytemplate.pt')
def poop_view(request):
    return {'project': 'Poop'}
