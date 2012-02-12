from setuptools import setup, find_packages

version = '0.1a1'

requires = [
    'python-gnupg>=0.2.8',
]

setup(name='epoint.client',
      version=version,
      description='Bob is selling various physical and digital goods over http/https',
      author='Andrey Martyanov',
      author_email='andrey@martyanov.com',
      url='https://www.epointsystem.org/trac/vending_machine/wiki/WebShop',
      license='GNU GPL',
      packages=find_packages(),
      namespace_packages=['epoint'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      test_suite = "tests",
)