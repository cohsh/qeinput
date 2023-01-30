from mp_api.client import MPRester
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer


class Material:
    def __init__(self, api_key, material_id):
        with MPRester(api_key) as mpr:
            docs = mpr.summary.search(
                    material_ids=[material_id],
                    fields=["elements", "nsites", "nelements",
                            "formula_pretty", "structure", "is_metal"]
                    )

        self.elements = docs[0].elements
        self.nsites = docs[0].nsites
        self.nelements = docs[0].nelements
        self.formula_pretty = docs[0].formula_pretty
        self.is_metal = docs[0].is_metal
        structure = docs[0].structure
        analyzer = SpacegroupAnalyzer(structure)
        self.space_group = analyzer.get_space_group_symbol()
        self.ibrav = self._get_ibrav()
        refined_structure = analyzer.get_refined_structure()
        self.a = refined_structure.lattice.a
        self.b = refined_structure.lattice.b
        self.c = refined_structure.lattice.c
        self.sites = structure.sites

    def _get_ibrav(self):
        sg = self.space_group

        # Not yet support the cases ibrav = 0 and ibrav > 4.
        if sg in ["Pm-3m"]:
            return 1
        elif sg in ["Fm-3m", "Fd-3m", "F-43m"]:
            return 2
        elif sg in ["Im-3m"]:
            return 3
        else:
            return None
