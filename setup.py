from setuptools import setup

setup(
    name='vercelDeploy',
    version='1.0.0',
    description='Deploy Lambda functions onto vercel',
    author='Abhinay',
    license='MIT',
    packages=['vercelDeploy', 'vercelDeploy/cli'],
    install_requires=['click', 'fastapi', 'uvicorn']
)
