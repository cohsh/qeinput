import re

from qeinput.material import Material
from qeinput.inputs import InputBase
import qeinput.formats as formats


class InputPW(InputBase):
    def __init__(self, material: Material,
                 calculation: str, pseudo_dir: str, k_points: list,
                 ecutwfc: int, conv_thr="1.D-12", do_shift=False):
        super().__init__()

        atomic_species = ""
        for element in material.elements:
            atomic_species += "{element} {mass} {pseudo}\n".format(
                    element=element.symbol,
                    mass=re.sub("amu", "", str(element.atomic_mass)),
                    pseudo=element.symbol+".upf"
                    )

        atomic_positions = ""
        for site in material.sites:
            atomic_positions += "{species} {a} {b} {c}\n".format(
                    species=re.sub("[0-9]", "", site.species.reduced_formula),
                    a=site.a,
                    b=site.b,
                    c=site.c
                    )

        if do_shift:
            shift = [1, 1, 1]
        else:
            shift = [0, 0, 0]

        if not material.is_metal:
            occupations = "fixed"
        else:
            occupations = "smearing"

        if calculation == "scf":
            str_k_points = "{kx} {ky} {kz} {sx} {sy} {sz}".format(
                    kx=k_points[0],
                    ky=k_points[1],
                    kz=k_points[2],
                    sx=shift[0],
                    sy=shift[1],
                    sz=shift[2]
                    )
            self.text = formats.pw["scf"].format(
                    prefix=material.formula_pretty,
                    pseudo_dir=pseudo_dir,
                    ibrav=material.ibrav,
                    abc="a = {a}".format(a=material.a),
                    nat=material.nsites,
                    ntyp=material.nelements,
                    ecutwfc=ecutwfc,
                    ecutrho=ecutwfc*4,
                    occupations=occupations,
                    conv_thr=conv_thr,
                    atomic_species=atomic_species,
                    atomic_positions=atomic_positions,
                    k_points_automatic=str_k_points
                    ).strip()
        elif calculation == "nscf":
            pass
