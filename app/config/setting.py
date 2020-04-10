# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/4/2.
  Flask 对配置项的限制，你必须保证命名全都大写，才能注入到current_app.config中
"""
__author__ = 'Allen7D'

'''
应用于Swagger的URL，会自动添加协议前缀(http://或者https://)，因为会切换协议前缀
local_setting.py中 SERVER_URL = '127.0.0.1:8010'
'''
SERVER_URL = 'server.mini-shop.ivinetrue.com'  # 外部（云服务器）地址

IMG_PREFIX = SERVER_URL + '/static/images'
UPLOAD_FOLDER = 'app/static/files'
# 默认文件上传配置
FILE = {
    "STORE_DIR": 'app/static/files',
    "SINGLE_LIMIT": 1024 * 1024 * 2,
    "TOTAL_LIMIT": 1024 * 1024 * 20,
    "NUMS": 10,
    "INCLUDE": set(['jpg', 'png', 'jpeg']),
    "EXCLUDE": set([])
}

# flask-admin配置
FLASK_ADMIN_SWATCH = 'cerulean'

# Swagger配置
version = "0.3.0"  # 项目版本
description = """API接口分为cms版本和v1版本，大部分接口需要token权限才能访问。
访问之前，先使用/v1/token查询token，并将token放入Authorize中。
"""

'''
内部只支持http
外部（云服务器）支持 https 和 http 协议
local_setting.py中 
  SERVER_SCHEMES = ["http"] # 内部只支持http
'''
SERVER_SCHEMES = ["https", "http"]

SWAGGER_TAGS = []  # 在'/app/api/__init__.py'中create_blueprint_list设置
SWAGGER = {
"swagger_version": "2.0",
"info": {
    "title": "微信小程序商城: API",
    "version": version,
    "description": description,
    "contact": {
        "responsibleOrganization": "Shema(聆听)",
        "responsibleDeveloper": "Allen7D",
        "email": "bodanli159951@163.com",
        "url": "http://ivinetrue.com"
    },
    "termsOfService": "http://ivinetrue.com"
},
"host": SERVER_URL,  # "api.ivinetrue.com",
"basePath": "/",  # base bash for blueprint registration
"tags": SWAGGER_TAGS,
"schemes": SERVER_SCHEMES,
"operationId": "getmyData",
"securityDefinitions": {
    'basicAuth': {
        'type': 'basic'
    }
}
}

# SWAGGER的安全访问方式
SPECS_SECURITY = [
{
    "basicAuth": []
}
]

# all model by module for flask-admin
ALL_MODEL_BY_MODULE = {
'user': ['User'],
'user_address': ['UserAddress'],
'order': ['Order'],
'banner': ['Banner'],
'banner_item': ['BannerItem'],
'theme': ['Theme'],
'category': ['Category'],
'product': ['Product'],
'image': ['Image']
}

# all api by module(version)
# 可以控制Swagger API文档的显示顺序
ALL_RP_API_LIST = \
    ['v1.token'] + \
    ['cms.admin', 'cms.group', 'cms.auth'] + \
    ['v1.user', 'v1.address',
'v1.banner', 'v1.theme', 'v1.category', 'v1.product', 'v1.order', 'v1.pay'] + \
    ['cms.user', 'cms.file']

# 所有endpoint的meta信息
EP_META = {}
EP_INFO_LIST = []
EP_INFOS = {}

# 项目的github地址
GITHUB_URL = 'https://github.com/Allen7D/mini-shop-serve'
# 项目文档地址
DOC_URL = 'http://doc.mini-shop.ivinetrue.com'
