# -*- coding: utf-8 -*-
"""
Unit tests for pubchempy.py

Python interface for the PubChem PUG REST service.
https://github.com/mcs07/PubChemPy
"""

import unittest

from pubchempy import *


class TestPubChemPy(unittest.TestCase):
    """ These tests don't check whether the output is correct. They just check that no exception is raised. """

    def setUp(self):
        """ Define some example inputs """
        self.phenanthrolinesmiles = 'C1=CC2=C(C3=C(C=CC=N3)C=C2)N=C1'
        self.molform = 'C10H21N'
        self.rucomplex = 'tris-(1,10-phenanthroline)ruthenium'

    def test_requests(self):
        """ Test basic raw requests """
        print request('coumarin', 'name', record_type='3d')
        print request('coumarin', 'name', output='PNG', image_size='50x50')

    def test_listkeys(self):
        """ Test asynchronous listkey requests """
        print get('CC', 'smiles', operation='cids', searchtype='superstructure')
        print get(self.molform, 'formula', listkey_count=3)

    def test_properties(self):
        print get_properties('IsomericSMILES', self.rucomplex, 'name')

    def test_synonyms(self):
        print get_synonyms(self.phenanthrolinesmiles, 'smiles')

    def test_compounds(self):
        c = Compound.from_cid(1)
        print c.cid
        print c.record
        print c.atoms
        print c.bonds
        print c.charge
        print c.molecular_formula
        print c.molecular_weight
        print c.canonical_smiles
        print c.isomeric_smiles
        print c.inchi
        print c.inchikey
        print c.iupac_name
        print c.xlogp
        print c.exact_mass
        print c.monoisotopic_mass
        print c.tpsa
        print c.complexity
        print c.h_bond_donor_count
        print c.h_bond_acceptor_count
        print c.rotatable_bond_count
        print c.fingerprint
        print c.heavy_atom_count
        print c.isotope_atom_count
        print c.atom_stereo_count
        print c.defined_atom_stereo_count
        print c.undefined_atom_stereo_count
        print c.bond_stereo_count
        print c.defined_bond_stereo_count
        print c.undefined_bond_stereo_count
        print c.covalent_unit_count

        c = Compound.from_cid(1, record_type='3d')
        print c.volume_3d
        print c.multipoles_3d
        print c.conformer_rmsd_3d
        print c.effective_rotor_count_3d
        print c.pharmacophore_features_3d
        print c.mmff94_partial_charges_3d
        print c.mmff94_energy_3d
        print c.conformer_id_3d
        print c.shape_selfoverlap_3d
        print c.feature_selfoverlap_3d
        print c.shape_fingerprint_3d

    def test_csaids(self):
        print get_cids('Aspirin', 'name', 'substance')
        print get_cids('Aspirin', 'name', 'compound')
        print get_sids('Aspirin', 'name', 'substance')
        print get_aids('Aspirin', 'name', 'substance')
        print get_aids('Aspirin', 'name', 'compound')

    def test_assays(self):
        print get_assays(1, sid='67107,67121,67122')

    def test_substructure(self):
        print get_compounds('C1=CC2=C(C3=C(C=CC=N3)C=C2)N=C1', 'smiles', searchtype='substructure', listkey_count=3)


if __name__ == '__main__':
    unittest.main()

