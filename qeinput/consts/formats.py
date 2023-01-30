import textwrap


class InputFormats():
    SCF = textwrap.dedent('''
&control
prefix = '{prefix}'
calculation = 'scf'
pseudo_dir = '{pseudo_dir}'
outdir = './'
/
&system
ibrav = {ibrav}
{abc}
nat = {nat}
ntyp = {ntyp}
ecutwfc = {ecutwfc}
ecutrho = {ecutrho}
occupations = '{occupations}'
/
&electrons
conv_thr        = {conv_thr}
/
ATOMIC_SPECIES
{atomic_species}
ATOMIC_POSITIONS alat
{atomic_positions}
K_POINTS automatic
{k_points}
''')
