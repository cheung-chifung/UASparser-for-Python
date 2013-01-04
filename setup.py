from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='uasparser',
      version='0.1',
      description='Browser User Agent parser',
      long_description=readme(),
      url='https://github.com/keekun/UASparser-for-Python',
      author='Chifung Cheung',
      author_email='Chifung.Cheung@gmail.com',
      packages=['uasparser'],
      zip_safe=True)
