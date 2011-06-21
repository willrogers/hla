import os
import sipconfig

# The name of the SIP build file generated by SIP and used by the build
# system.
build_file = "pytracy.sbf"

# Get the SIP configuration information.
config = sipconfig.Configuration()

# Run SIP to generate the code.
os.system(" ".join([config.sip_bin, "-c", ".", "-b", build_file, "pytracy.sip"]))

# Create the Makefile.
makefile = sipconfig.SIPModuleMakefile(config, build_file)

# Add the library we are wrapping.  The name doesn't include any platform
# specific prefixes or extensions (e.g. the "lib" prefix on UNIX, or the
# ".dll" extension on Windows).
makefile.extra_libs = ["tracy -lTPSALib -lnum_rec"]

# Generate the Makefile itself.
makefile.generate()

mod = []
try:
# file = open("hello", "r")
# for line in file:
# mod.append(line)

  mod = open("sippytracycmodule.cpp", "r").readlines()
# file.close()
except IOError:
  print "Couldn't open file"

mod[8]= mod[8].replace("\n","int no_tps=1;\n\n")
# I then did my regex matching on the mod array, before commiting back to a file using

try:
  file = open("sippytracycmodule.cpp", "w")
  file.writelines(mod)
  file.close()
except IOError:
  print "Couldn't save file"

mod = []
try:
# file = open("Makefile", "r")
# for line in file:
# mod.append(line)

  mod = open("Makefile", "r").readlines()
# file.close()
except IOError:
  print "Couldn't open file"

mod[10]= mod[10].replace("\n"," -L../tracy-3.5/tracy/src -L../tracy-3.5/TPSA -L../../num_rec/src\n");
# I then did my regex matching on the mod array, before commiting back to a file using

try:
  file = open("Makefile", "w")
  file.writelines(mod)
  file.close()
except IOError:
  print "Couldn't save file"
