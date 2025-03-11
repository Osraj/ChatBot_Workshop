# 🃏 Conda Quick Reference Card

[← Back to Reference Cards](README.md) | [← Back to Main README](../README.md)

## Essential Environment Commands

```bash
# Create environment
conda create -n chatbot-env python=3.10

# Activate environment
conda activate chatbot-env

# Deactivate environment
conda deactivate

# List environments
conda env list
```

## Package Management

```bash
# Install package
conda install package_name

# Install from channel
conda install -c conda-forge package_name

# Install multiple packages
conda install package1 package2

# List installed packages
conda list
```

## Environment Files

```bash
# Export environment
conda env export > environment.yml

# Create from file
conda env create -f environment.yml
```

## Workshop Specific

```bash
# Create workshop environment
conda create -n chatbot-env python=3.10

# Activate workshop environment
conda activate chatbot-env

# Install required packages
pip install streamlit groq python-dotenv
```

[← Back to Reference Cards](README.md) | [← Back to Main README](../README.md)