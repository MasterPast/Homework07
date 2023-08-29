from setuptools import setup, find_namespace_packages

setup(
    name='Clean-folder_by_MasterPast',
    version='1.0.2',
    description='Sorter of temp unstructured files',
    url='https://github.com/MasterPast/Homework07/tree/29743ba34cfe3a96af5306ed55420ef9ca48f13b/clean_folder',
    author='MasterPast',
    author_email='igory733@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
)