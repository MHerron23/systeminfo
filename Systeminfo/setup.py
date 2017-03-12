from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="basic system info",
      url="",
      author="michael herron",
      author_email="michael.herron@ucdconnect.ie",
      licence="GPL3",
      packages=['Systeminfo'],
      entry_points={
          'consolse_scripts':['comp30670_Systeminfo=Systeminfo.main:main']
          }
      
      )