import setuptools
from setuptools import find_packages
with open("README.md",'r',encoding='utf-8') as f:
    long_description=f.read()
__version__='0.0.0'

REPO_NAME='End-to-End-chest-cancer-classification-using-mlflow'
AUTHOR_USER_NAME='SHREYA3999'
SRC_REPO='cnnClassifier'
AUTHOR_EMAIL='shreyajhansi3999@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    email=AUTHOR_EMAIL,
    description="A small python package for chest cancer classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
)