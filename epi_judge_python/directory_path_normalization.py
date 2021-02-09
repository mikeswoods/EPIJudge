from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    path = path.strip()
    is_absolute = path[0] == "/"
    components = [p.strip() for p in path.split("/") if len(p.strip()) > 0 and p.strip() != "."]

    shortest_path = []
    for component in components:
      if component == "..":
        # If the stack is empty, treat it as its own component:
        if len(shortest_path) > 0 and shortest_path[-1] != "..":
          shortest_path.pop()
        else:
          shortest_path.append(component)
      else:
        shortest_path.append(component)

    new_path = "/".join(shortest_path)
    if is_absolute:
      new_path = "/" + new_path

    return new_path


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
