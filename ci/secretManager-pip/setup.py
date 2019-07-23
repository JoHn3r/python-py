from setuptools import setup

setup(
    name="secret-manager",
    version="0.0.1",
	scripts=['secretmanager'],
	setup_requires=['nexus_uploader']
)