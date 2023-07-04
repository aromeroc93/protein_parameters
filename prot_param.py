from Bio.SeqUtils.ProtParam import ProteinAnalysis
import pyperclip

prot = input("Insert protein sequence: ")
protein = ProteinAnalysis(prot)

epsilon = protein.molar_extinction_coefficient()
mw = protein.molecular_weight()

print("Number of residues: ", sum(protein.count_amino_acids().values()))
print("Mw: ""%0.2f" % mw)
print("IP: ""%0.2f" % protein.isoelectric_point())
if epsilon[0] == 0:
    print("No Trp resiudes, can't compute Extinction coefficient")
else:
    print("Extinction coefficient:", epsilon[0], "(reduced), ", epsilon[1], "(oxidized)", "\nAbs280nm (1g/l):", epsilon[0]/mw, " // ")#, 1/(epsilon[0]/mw))
print("Copied to clipboard!")
# pyperclip.copy("Mw: ""%0.2f" % mw, "\nIP: ""%0.2f" % protein.isoelectric_point(), "\nExtinction coefficient:", epsilon[0], "(reduced), ", epsilon[1], "(oxidized)", "\nAbs280nm (1g/l):", epsilon[0]/mw, " // ", 1/(epsilon[0]/mw))
pyperclip.copy("Mw: ""%0.2f" % mw + "\nIP: " + str(protein.isoelectric_point()))