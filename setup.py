from setuptools import setup, find_packages

setup(
    name="imdb-metadata-extractor",
    version='0.0.1',
    packages=find_packages(),
    author="Frederico Schmitt Kremer",
    author_email="fred.s.kremer@gmail.com",
    description="imdb-metadata-extractor",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    keywords="web",
    entry_points = {'console_scripts':[
        'imdb-metadata-extractor   = imdb_metadata_extractor.ime:main',
        ]},
    install_requires = [
        requirement.strip('\n') for requirement in open("requirements.txt")
    ]
)