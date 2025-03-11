# 📋 Conda Commands Cheat Sheet

[← Back to Main README](README.md) | [View All Cheat Sheets](cheatsheets.md)

This cheat sheet provides quick reference for the most commonly used Conda commands when setting up and managing Python environments.

## Table of Contents
- [📋 Conda Commands Cheat Sheet](#-conda-commands-cheat-sheet)
  - [Table of Contents](#table-of-contents)
  - [Environment Management](#environment-management)
  - [Package Management](#package-management)
  - [Environment Files](#environment-files)
  - [Channels and Config](#channels-and-config)
  - [Common Issues and Solutions](#common-issues-and-solutions)
  - [Tips for Workshop](#tips-for-workshop)

## Environment Management

```bash
# Create a new environment
conda create -n env_name python=3.10

# Activate an environment
conda activate env_name

# Deactivate current environment
conda deactivate

# List all environments
conda env list

# Remove an environment
conda env remove -n env_name

# Clone an environment
conda create -n new_env --clone existing_env
```

[Back to Top](#-conda-commands-cheat-sheet)

## Package Management

```bash
# Install a package
conda install package_name

# Install a specific version
conda install package_name=1.2.3

# Install multiple packages
conda install package1 package2

# Install from conda-forge channel
conda install -c conda-forge package_name

# Update a package
conda update package_name

# Update all packages
conda update --all

# List installed packages
conda list

# Search for a package
conda search package_name
```

[Back to Top](#-conda-commands-cheat-sheet)

## Environment Files

```bash
# Export environment to file
conda env export > environment.yml

# Create environment from file
conda env create -f environment.yml

# Update environment from file
conda env update -f environment.yml

# Export only manually installed packages
conda env export --from-history > environment.yml
```

[Back to Top](#-conda-commands-cheat-sheet)

## Channels and Config

```bash
# Add a channel
conda config --add channels channel_name

# Set channel priority
conda config --set channel_priority strict

# View configuration
conda config --show

# Create .condarc file (run once)
conda config --write-default
```

[Back to Top](#-conda-commands-cheat-sheet)

## Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| "conda command not found" | Add Conda to your PATH or restart your terminal |
| Environment not activating | Check if Conda is initialized (`conda init`) |
| Package conflicts | Try installing in a clean environment or use `--force` with caution |
| Slow installations | Use the faster Mamba drop-in replacement: `conda install -c conda-forge mamba` |
| Environment corruption | Create a new environment and reinstall packages from `environment.yml` |

[Back to Top](#-conda-commands-cheat-sheet)

## Tips for Workshop

- Create a dedicated environment specifically for the chatbot project
- Use `environment.yml` to share the exact environment with all participants
- Pin critical package versions to ensure compatibility
- Consider using `conda-forge` channel for more up-to-date packages

[Back to Top](#-conda-commands-cheat-sheet)

[← Back to Main README](README.md) | [View All Cheat Sheets](cheatsheets.md)