from pathlib import Path

HOMEDIR = Path('.').resolve()
BUILDDIR = HOMEDIR / 'build'
print(BUILDDIR)
# DATA_CSV = 'bd_lab_small_sample.csv'
# DATA_PARQUET = DATA_CSV.with_suffix('.parquet')
