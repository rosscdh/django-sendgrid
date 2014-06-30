from setuptools import setup

setup(
    name="django-sendgrid",
    packages=['dj_sendgrid'],
    version='0.0.1',
    author="Ross Crawford-d'Heureuse",
    license="MIT",
    author_email="ross@lawpal.com",
    url="https://github.com/rosscdh/django-sendgrid",
    description="A Django app for integrating with sendgrid webhooks",
    zip_safe=False,
    include_package_data=True,
    install_requires = [
        'django-braces',
    ]
)
