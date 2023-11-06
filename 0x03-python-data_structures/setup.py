from setuptools import setup, Extension
import os.path

extensions = [
    Extension(
        'my_package.hello_world',
        [os.path.join('my_package', 'hello_world.c')]
    )
]
setup(name="my_package", ext_modules=extensions)
