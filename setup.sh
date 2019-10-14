#/usr/bin/env bash -e

# Copy config.ini.default if config.ini doesn't exist.
if [ ! -e config.ini ]
then
    cp config.ini.default config.ini
fi

PYTHON=`which python3`
VENV=venv

if [ -f "$PYTHON" ]
then
    # Create a virtual environment
    $PYTHON -m venv $VENV

    # Activate the virtual environment and install requirements.
    . $VENV/bin/activate
    pip3 install -r requirements.txt

else
    >&2 echo "Cannot find Python 3. Please install it."
fi
