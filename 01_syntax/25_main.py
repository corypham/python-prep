# if __name__ == __main__: 
#   this script can be imported OR can run standalone
#   functions and classes in this module can be reused without
#   the main block of code executing

# ex. Library = Import library for functionality
#               When running library directly, display help page
#

# It is commony used for the main() block. If the file is being
# imported as a module, __name__ is set to the file's name.
# Ensures certain code (testing, initialization) only rungs when the
# file/script is being executed directly, not imported 
def main():
  print("main executing")
  pass


if __name__ == "__main__":
  main()
