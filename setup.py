from distutils.core import setup
setup(name='chrono',
      version='0.0.1',
      py_modules=["chrono", "today"],
      install_requires=["humanize==0.5.1"],
      entry_points={
          'console_scripts': [
              'chrono = chrono:launch',
              'leftofday = today:main',
              ],
          },
      )

