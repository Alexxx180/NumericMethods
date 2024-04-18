$packs = @('prettytable', 'matplotlib', 'numpy', 'inquirer', 'scipy', 'sympy')
$packs | ForEach-Object { pip install $PSItem }
