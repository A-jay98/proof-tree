import os
import re
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout


def create_graph(results):
    G = nx.DiGraph()
    for source in results:
        for target in results[source]:
            G.add_edge(source, target)
    return G


def find_labels_in_proofs(content):
    """Find all \cref commands in the content and extract the referenced labels."""
    cref_pattern = re.compile(r'\\[cC]ref{(.*?)}')
    matches = cref_pattern.findall(content)
    res = []
    for y in matches:
        res.extend([x for x in y.split(",") if not x.startswith("a")])
    return res


def find_environments(content):
    """Find all claim, lemma, or observation environments and their labels."""
    pattern = r"\\begin\{((claim|lemma|observation)|(corollary))\}\\label{(.*?)\}.*?\\end\{\1\}(?(3)|.*?\\begin\{proof\}(.*?)\\end\{proof\})"
    environment_pattern = re.compile(pattern, re.DOTALL)
    return [(x[0], x[3], x[4]) for x in environment_pattern.findall(content)]


def main(directory):
    results = {}
    for filename in ["proof.tex", "worstcase-steps.tex", "flags-invariant.tex", "invalidation-phase.tex",
                     "move-phase.tex", "ts-invariant.tex", "fhnt-updatesTS.tex", "move-keeps-order.tex",
                     "compare.tex"]:
        if filename.endswith('.tex'):
            with open(os.path.join(directory, filename), 'r') as f:
                content = f.read()
                environments = find_environments(content)
                if filename == "proof.tex":
                    print("YYYYY", environments)
                for env_type, label, proof in environments:
                    referenced_labels = find_labels_in_proofs(proof)
                    if label in results:
                        results[label].extend(referenced_labels)
                    else:
                        results[label] = referenced_labels
                    for referenced_label in referenced_labels:
                        if referenced_label not in results and not referenced_label.endswith("sub"):
                            print(referenced_label, "used ahead of time in", label, filename)
    return results


def draw_tree(graph):
    # Create a PyGraphviz graph
    pygraph = nx.drawing.nx_agraph.to_agraph(graph)

    # If the graph has no layout, set a default layout
    if not pygraph.has_layout:
        pygraph.layout(prog='dot')

    # Set the node positions using graphviz_layout
    positions = graphviz_layout(graph, prog='dot')

    # Set the positions in the PyGraphviz graph
    for node, pos in positions.items():
        pygraph.get_node(node).attr['pos'] = '{},{}'.format(pos[0], pos[1])

    # Set the node colors based on the root attribute
    for node in graph.nodes:
        # if graph.nodes[node]['root']:
        #     pygraph.get_node(node).attr['style'] = 'filled'
        #     pygraph.get_node(node).attr['fillcolor'] = 'lightblue'

        if node.startswith("c:"):
            pygraph.get_node(node).attr['style'] = 'filled'
            pygraph.get_node(node).attr['fillcolor'] = 'lightgreen'
        if node.startswith("o:"):
            pygraph.get_node(node).attr['style'] = 'filled'
            pygraph.get_node(node).attr['fillcolor'] = 'lightpink'

    # Draw the PyGraphviz graph and show it
    pygraph.draw('tree.png')
#%%
if __name__ == '__main__':
    results = main('.')
    G = create_graph(results)
    print(G)
    nx.write_graphml(G, 'graph.graphml')

    t = [(x, G.in_degree(x)) for x in G.nodes()]
    t.sort(key=lambda x: x[1])
    roots = [x for x, y in t if y == 0]
    attr = {r: {"root": True} for r in roots}
    nx.set_node_attributes(G, attr)

    draw_tree(G)

    # for n in G.nodes:
    #     if n in roots:
    #         continue
    #     mr, md = None, None
    #     for r in roots:
    #         try:
    #             t = nx.shortest_path_length(G, source=r, target=n)
    #             if md is None or t < md:
    #                 md = t
    #                 mr = r
    #         except nx.NetworkXNoPath:
    #             pass
    #     print(n, md, mr)
    #     if md is None:
    #         md = 1000
    #     # add info to the node
    #     nx.set_node_attributes(G, {n: {'depth': md, 'par': mr}})

