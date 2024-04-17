#! /bin/bash
pyinstaller --add-data "cli:cli" --add-data "module:module" --add-data "model:model" --hidden-import json --hidden-import boto3  --hidden-import pydantic main.py
sudo cp -r ./dist/main/* /opt/pillow
sudo mv /opt/pillow/main /opt/pillow/pw