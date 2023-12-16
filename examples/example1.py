from cloud_import import add_repo, add_gh_repo
# Repo: https://github.com/tomchen/example_pypi_package/tree/main
# Note that the source is in the subdir "src", so ref is set to "main/src" instead of just "main"
add_gh_repo("tomchen", "example_pypi_package", "main/src")
# ^ is equivalent to:
#add_repo("https://raw.githubusercontent.com/tomchen/example_pypi_package/main/src")

import examplepy
n1 = examplepy.Number(1)
n2 = examplepy.Number(2)
print(n1 + n2)
