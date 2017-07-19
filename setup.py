from setuptools import setup

setup(
    name='feature-requests',
    version='1.0',
    long_description=__doc__,
    packages=['feature_requests'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'flask-sqlalchemy',
        'pymysql',
        'requests',
        'pytest',
        'mock',
        'dateutils',
    ]
)
