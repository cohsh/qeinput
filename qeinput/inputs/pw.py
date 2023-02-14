import re

from qeinput.material import Material
from qeinput.inputs import InputBase
import qeinput.formats as formats


class InputPW(InputBase):
    def __init__(self, material: Material):
        super().__init__()

        self.atomic_species = ""
        for element in material.elements:
            self.atomic_species += "{element} {mass} {pseudo}\n".format(
                    element=element.symbol,
                    mass=re.sub("amu", "", str(element.atomic_mass)),
                    pseudo=element.symbol+".upf"
                    )

        self.atomic_positions = ""
        for site in material.sites:
            self.atomic_positions += "{species} {a} {b} {c}\n".format(
                    species=re.sub("[0-9]", "", site.species.reduced_formula),
                    a=site.a,
                    b=site.b,
                    c=site.c
                    )

        if not material.is_metal:
            self.occupations = "fixed"
        else:
            self.occupations = "smearing"


class InputPWSCF(InputPW):
    def __init__(self, material: Material,
                 pseudo_dir: str, outdir: str, ecutwfc: int,
                 k_points: list,
                 conv_thr="1.D-12", do_shift=False):
        super().__init__(material)

        if do_shift:
            shift = [1, 1, 1]
        else:
            shift = [0, 0, 0]

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
                outdir=outdir,
                ibrav=material.ibrav,
                abc="a = {a}".format(a=material.a),
                nat=material.nsites,
                ntyp=material.nelements,
                ecutwfc=ecutwfc,
                ecutrho=ecutwfc*4,
                occupations=self.occupations,
                conv_thr=conv_thr,
                atomic_species=self.atomic_species,
                atomic_positions=self.atomic_positions,
                k_points_automatic=str_k_points
                ).strip()


class InputPWNSCF(InputPW):
    def __init__(self, material: Material,
                 pseudo_dir: str, outdir: str, ecutwfc: int,
                 k_points: list, nbnd: int,
                 conv_thr="1.D-10"):
        super().__init__(material)

        str_k_points = "{n}\n".format(n=str(len(k_points)))
        for k_point in k_points:
            str_k_points += "{kx} {ky} {kz} 1.0\n".format(
                    kx=k_point[0],
                    ky=k_point[1],
                    kz=k_point[2]
                    )

        self.text = formats.pw["nscf"].format(
                prefix=material.formula_pretty,
                pseudo_dir=pseudo_dir,
                outdir=outdir,
                ibrav=material.ibrav,
                abc="a = {a}".format(a=material.a),
                nat=material.nsites,
                ntyp=material.nelements,
                ecutwfc=ecutwfc,
                ecutrho=ecutwfc*4,
                occupations=self.occupations,
                nbnd=nbnd,
                conv_thr=conv_thr,
                atomic_species=self.atomic_species,
                atomic_positions=self.atomic_positions,
                k_points_crystal=str_k_points
                ).strip()
