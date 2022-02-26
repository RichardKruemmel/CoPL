from mvc import Controller, ModelBasic, View
from dependency_injector import containers, providers

configObj = [{'name': 'bread', 'price': 0.5, 'quantity': 20},
            {'name': 'soymilk', 'price': 1.5, 'quantity': 10},
            {'name': 'beer', 'price': 1.0, 'quantity': 6},
            {'name': 'crisps', 'price': 1.1, 'quantity': 5}]

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    model = providers.Singleton(ModelBasic, configObj)
    view = providers.Singleton(View)
    controller = providers.Singleton(Controller, model, view) 

def manual_di():
    c = Controller(ModelBasic(configObj), View())
    c.show_items()
    c.insert_item(name='wine', price=10, quantity= 4)
    c.update_item(name='soymilk', price=1.4, quantity=20)
    c.show_items()

def framework_di():
    # documentation: https://python-dependency-injector.ets-labs.org/introduction/di_in_python.html
    container = Container()
    container.config.configObj(configObj)
    c = container.controller()
    c.show_items()
    c.insert_item(name='wine', price=10, quantity= 4)
    c.update_item(name='soymilk', price=1.4, quantity=20)
    c.show_items()



if __name__ == '__main__':
    manual_di()
    print("")
    print("")
    framework_di()