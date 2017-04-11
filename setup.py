"""
Sanic-JWT-Extended
-------------------
"""
from setuptools import setup

setup(name='Sanic-JWT-Extended',
      description='Extended JWT integration with Sanic',
      long_description='Extended JWT integration with Sanic',
      keywords = ['sanic', 'jwt', 'json web token'],
      packages=['sanic_jwt_extended'],
      zip_safe=False,
      platforms='any',
      install_requires=['Sanic', 'PyJWT', 'simplekv', 'six', 'werkzeug'])
