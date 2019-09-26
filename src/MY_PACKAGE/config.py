import json

class _Config:
    """The config object to use throughout the code, since it's easier than using a dictionary.

    This class should never be used directly. Use get_config instead.

    :param conf_file_path: the path to a JSON conf file. All entry in the conf file will be 
        accessible as an attribute of this class
    :type conf_file_path: str 
    """
    def __init__(self, conf_file_path):
        with open(conf_file_path, 'r') as conf_file:
            content = json.load(conf_file)
        
        for k in content.keys():
            setattr(self, k, content[k])


def get_config(path=None):
    """Returns a Config object. You only need to give the path to a JSON conf file the first time 
    this method is called, and then it simply returns the same object.

    :param path: path to a JSON config file, only the first time this method is called
    :type path: str    
    """
    global _cfg
    if "_cfg" in globals():
        return _cfg
    elif not path:
        raise ValueError(
            "Path to a conf file must be passed the first time that get_config is called."
            )
    _cfg = _Config(path)
    return _cfg