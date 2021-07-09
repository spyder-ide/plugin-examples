# Spyder 5 plugins by example

This repository contains several plugin examples for the new Spyder 5 API.


## Get started

To see any of the plugin examples in action, you need to run the following commands in a system terminal:

```bash
# Clone the repository
git clone https://github.com/spyder/plugin-examples.git spyder-plugin-examples

# Go to the examples folder
cd spyder-plugin-examples

# Create a new environment
conda env create

# Activate the environment
conda activate spyder-plugin-examples

# Go to one of the examples folder
cd status-bar-widgets

# Install the plugin in development mode
python -m pip install -e .

# Start Spyder
spyder
```


## Examples

* [Custom layout](./spyder-custom-layout): It shows how to add a custom window layout to the interface and place dockable plugins next to others using the `TABIFY` attribute.
* [Status bar widgets](./status-bar-widgets): It shows how to add different kinds of widgets to the status bar.
