from distutils.core import setup
setup(name='chrono',
      version='0.0.1',
      entry_points={
          'console_scripts': [
              'chrono = chrono:launch',
              'leftofday = today:main',
              ],
          },
      )

