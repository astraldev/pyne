import os
from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent
os.chdir(here)

icons = {
    "64": ["ui/icons/64x64/apps/"+x for x in os.listdir("ui/icons/64x64/apps")],
    "128": ["ui/icons/128x128/apps/"+x for x in os.listdir("ui/icons/128x128/apps")],
    "256": ["ui/icons/256x256/apps/"+x for x in os.listdir("ui/icons/256x256/apps")],
    "512": ["ui/icons/512x512/apps/"+x for x in os.listdir("ui/icons/512x512/apps")],
    "scalable": ["ui/icons/scalable/apps/"+x for x in os.listdir("ui/icons/scalable/apps")],
}
action_icons = ["ui/icons/scalable/action/" +
                x for x in os.listdir("ui/icons/scalable/action")]

setup(
    name="pynes",
    version="1.0.0",
    author="AstralDev",
    author_email="ekureedem480@gmail.com",
    description='A simple python mine game',
    long_description=str(open('README.md').read()),
    long_description_content_type="text/markdown",
    license="GPL v3",
    keywords="mines bomb",
    python_requires=">=3",
    install_requires=["timeutilities"],
    scripts=["scripts/pynes"],
    data_files=[
        ("share/applications", ["org.astralco.pyne.desktop"]),
        ("share/icons/hicolor/512x512/apps", icons["512"]),
        ("share/icons/hicolor/128x128/apps", icons["128"]),
        ("share/icons/hicolor/256x256/apps", icons["256"]),
        ("share/icons/hicolor/64x64/apps", icons["64"]),
        ("share/icons/hicolor/scalable/apps", icons["scalable"]),
        ("share/icons/hicolor/scalable/actions", action_icons)
    ]
)
