# config_override.py
"""
如果要部署到服务器时，需要修改host等信息，直接修改‘config_default'不好，
可以编写一个文件，来覆盖某些默认设置。
"""

configs = {
    'db': {
        'host': '47.98.217.220'
    }
}