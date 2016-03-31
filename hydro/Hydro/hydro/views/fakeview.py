from pyramid.view import view_config

@view_config(route_name='fake', renderer='../templates/mytemplate.pt')
def fake_view(request):
    return {'project': 'Hello from fake_view!'}
