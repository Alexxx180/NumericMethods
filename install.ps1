$packs = @('prettytable', 'matplotlib', 'numpy', 'inquirer', 'scipy')
$packs | ForEach-Object { pip install $PSItem }
