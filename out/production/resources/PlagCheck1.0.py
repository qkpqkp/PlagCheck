import ast
import sys

def parse_tree(tree, TREE_Values):
    tree_hash = hash(tree.__class__)
    node_num = 1

    for f in tree._fields:
        field = tree.__dict__.get(f)
        if type(field) is list:
            for node in field:
                if issubclass(node.__class__, ast.AST):
                    t, n = parse_tree(node, TREE_Values)
                    tree_hash += t
                    node_num += n
                    if "lineno" in dir(node):
                        TREE_Values[node.lineno] = (t, n)

        elif issubclass(field.__class__, ast.AST):
            t, n = parse_tree(field, TREE_Values)
            tree_hash += t
            node_num += n
            if "lineno" in dir(field):
                TREE_Values[field.lineno] = (t, n)
    return tree_hash, node_num


def main():
    f = open("C:\\Users\\Doly\\PlagCheck\\src\\main\\resources\\code1.py", "r")
    susp_code = f.read()
    tree1 = ast.parse(susp_code)
    TREE_Values1 = dict()

    for node in tree1.body:
        if (node.__class__ == ast.ImportFrom or node.__class__ == ast.Import):
            continue
        t1, n1 = parse_tree(node, TREE_Values1)
        TREE_Values1[node.lineno] = (t1, n1)

    f = open("C:\\Users\\Doly\\PlagCheck\\src\\main\\resources\\code2.py", "r")
    src_code = f.read()
    tree2 = ast.parse(src_code)
    TREE_Values2 = dict()

    for node in tree2.body:
        if (node.__class__ == ast.ImportFrom or node.__class__ == ast.Import):
            continue
        t2, n2 = parse_tree(node, TREE_Values2)
        TREE_Values2[node.lineno] = (t2, n2)
    # Sort the list
    TREE_Values1 = sorted(TREE_Values1.items(), key=lambda kv: kv[1][0])
    TREE_Values2 = sorted(TREE_Values2.items(), key=lambda kv: kv[1][0])

    i = 0
    j = 0

    suspected_lines = dict()
    while i < len(TREE_Values1) and j < len(TREE_Values2):
        if TREE_Values1[i][1][0] > TREE_Values2[j][1][0]:
            j += 1
        elif TREE_Values1[i][1][0] < TREE_Values2[j][1][0]:
            i += 1
        elif TREE_Values1[i][1][0] == TREE_Values2[j][1][0]:
            temp_j = j
            while j < len(TREE_Values2) and TREE_Values1[i][1][0] == TREE_Values2[j][1][0]:
                if TREE_Values1[i][1][1] == TREE_Values2[j][1][1]:
                    if TREE_Values1[i][0] in suspected_lines.keys():
                        suspected_lines[TREE_Values1[i][0]].append(TREE_Values2[j][0])
                    else:
                        suspected_lines[TREE_Values1[i][0]] = [TREE_Values2[j][0]]
                j += 1
            if i + 1 < len(TREE_Values1) and TREE_Values1[i + 1][1][0] == TREE_Values2[temp_j][1][0]:
                j = temp_j
                i += 1
                continue
            else:
                i += 1
    print(dict(sorted(suspected_lines.items())))

main()