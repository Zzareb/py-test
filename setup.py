import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='py-test',
    version='0.0.1',
    author='Zzareb',
    author_email='zzareb@email.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Zzareb/py-test',
    project_urls = {
        "Bug Tracker": "https://github.com/Zzareb/py-test/issues"
    },
    license='MIT',
    packages=['py-test'],
    install_requires=['boto3'],
)