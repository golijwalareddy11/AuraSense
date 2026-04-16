from setuptools import setup, find_packages

setup(
    name='aurasense',
    version='1.0.0',
    description='Mental Health Detection System',
    packages=find_packages(),
    install_requires=[
        'flask==3.0.0',
        'opencv-python-headless',
        'numpy>=2',
        'librosa==0.10.1',
        'deepface==0.0.92',
        'tensorflow==2.16.1',
        'pydub==0.25.1',
    ],
    python_requires='>=3.8',
)
