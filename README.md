# Vercel Deploy 

## Introduction

Use this Library to build and deploy your functions as API's onto vercel easily.
Check the [deployed example API here](https://verceldeploy-two.vercel.app/)

## Setup
- This library is similar to all other python packages but this is not hosted on pip. So in order to use this make sure you add this library to the root directory of your project where the code is present.

- run `npm i -g @vercel/python` to install the vercel@python npm package.

- run `pip install -r requirements.txt` to build the environment required.

## Usage Instructions
- Go to the directory where the code is located and run `python vercelDeploy build --path <filename>.py` to build the API file.

- run `python vercelDeploy deploy` to deploy the API onto the vercel using vercel CLI.
