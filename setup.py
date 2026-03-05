from setuptools import setup

setup(
    name="raninfo",
    version="0.1",
    py_modules=["raninfo"],
    entry_points={
        "console_scripts": [
            "raninfo = raninfo:main",  # main() from raninfo.py
        ],
    },
)