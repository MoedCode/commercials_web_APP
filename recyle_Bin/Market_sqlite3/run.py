#!/usr/bin/env python3
import sys
import os

# Get the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Append the parent directory to the system path
parent_directory = os.path.join(script_directory, '..')
sys.path.append(parent_directory)

from Market import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005, debug=True)



