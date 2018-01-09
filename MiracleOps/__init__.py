import pymysql
pymysql.install_as_MySQLdb()

def mysqldb_escape(value, conv_dict):
    from pymysql.converters import encoders
    vtype = type(value)
    # note: you could provide a default:
    # PY2: encoder = encoders.get(vtype, escape_str)
    # PY3: encoder = encoders.get(vtype, escape_unicode)
    encoder = encoders.get(vtype)
    return encoder(value)

import pymysql
setattr(pymysql, 'escape', mysqldb_escape)
del pymysql