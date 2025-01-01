from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyrealtime",
    version="0.1.0",
    author="Xinyao Lun",
    author_email="xyaolun@163.com",
    description="一个用于实时仿真的Python模块",
    url="https://github.com/heylancee/PyRealTime",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        # 如果有依赖包，在这里列出
    ],
) 