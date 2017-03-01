import config

def test_5_false(my_fix):
    print __file__, config, config.my_var_abs
    assert config.my_var_abs is False, 'maybe my_var_abs is true'
