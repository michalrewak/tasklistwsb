import setuptools

setuptools.setup(
    name="takslistwsb-app",
    version="0.1.0",
    description="The package to use YOLO via browser",
    author="Michal Rewak",
    author_email="michalrewak@gmail.com",
    license="MIT",
    packages=setuptools.find_packages(),
    package_data={"": ["*.json"]},
    entry_points={
        "console_scripts": [
            "takslistwsb-app=app:main",
        ],
    },
)
