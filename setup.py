from setuptools import setup

requirements = ""
with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    
setup(name='spellux',
      version='0.1.4',
      description='Automatic text normalization for Luxembourgish',
      url='https://github.com/questoph/spellux',
      author='Christoph Purschke',
      author_email='christoph@purschke.info',
      license='MIT',
      packages=['spellux'],
      install_requires=requirements,
      zip_safe=False,
      include_package_data=True,
      python_requires=">=3.6")
