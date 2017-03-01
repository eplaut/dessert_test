import slash
from . import config


@slash.yield_fixture
def my_fix():
    config.my_var_abs = False
    print __file__, config, config.my_var_abs
    yield 'my_fix'
    config.my_var_abs = True
