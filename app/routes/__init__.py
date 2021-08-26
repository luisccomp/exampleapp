# Miguel's and other tutorial's approach: put view functions inside of one file
# My approach: create a module folder and put view functions inside files
# according to their responsibillities: index, user, posts, etc.

from importlib import import_module

route_module_names = [
    'app.index'
]


def register_blueprints(app):
    for module_name in route_module_names:
        module = import_module(module_name)
        module.register_blueprint(app)
