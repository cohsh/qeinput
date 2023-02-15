import textwrap

pw = {}

pw["scf"] = textwrap.dedent('''
&control
prefix = '{prefix}'
calculation = 'scf'
pseudo_dir = '{pseudo_dir}'
outdir = '{outdir}'
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
conv_thr = {conv_thr}
/
ATOMIC_SPECIES
{atomic_species}
ATOMIC_POSITIONS alat
{atomic_positions}
K_POINTS automatic
{k_points_automatic}
''')

pw["nscf"] = textwrap.dedent('''
&control
prefix = '{prefix}'
calculation = 'nscf'
pseudo_dir = '{pseudo_dir}'
outdir = '{outdir}'
/
&system
ibrav = {ibrav}
{abc}
nat = {nat}
ntyp = {ntyp}
ecutwfc = {ecutwfc}
ecutrho = {ecutrho}
occupations = '{occupations}'
nbnd = {nbnd}
/
&electrons
conv_thr = {conv_thr}
/
ATOMIC_SPECIES
{atomic_species}
ATOMIC_POSITIONS alat
{atomic_positions}
K_POINTS crystal
{k_points_crystal}
''')


pw["vc-relax"] = textwrap.dedent('''
&control
prefix = '{prefix}'
calculation = 'vc-relax'
pseudo_dir = '{pseudo_dir}'
outdir = '{outdir}'
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
conv_thr = {conv_thr}
/
ATOMIC_SPECIES
{atomic_species}
ATOMIC_POSITIONS alat
{atomic_positions}
K_POINTS automatic
{k_points_automatic}
''')
