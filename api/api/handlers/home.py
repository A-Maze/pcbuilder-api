from pyramid.view import view_config


@view_config(route_name='home', renderer='json')
def root_view(request):
    return {"api": 0.1}
