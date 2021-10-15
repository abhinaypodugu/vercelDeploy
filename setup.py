from setuptools import setup

setup(
    name='vercelDeploy',
    version='0.1.0',
    description='Deploy Lambda functions to vercel',
    author='Abhinay',
    license='MIT',
    packages=['vercelDeploy', 'vercelDeploy/cli'],
    install_requires=['click']
)
