from pyramid.view import view_config


@view_config(route_name='home', renderer='json',
                        request_method='GET')
def root_view(request):
    return {"api": 1.1}
