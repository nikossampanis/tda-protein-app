import matplotlib.pyplot as plt

def plot_persistence_diagram(diagrams):
    fig, ax = plt.subplots()
    for dim, dgm in enumerate(diagrams):
        ax.scatter(dgm[:, 0], dgm[:, 1], label=f'H{dim}')
    ax.plot([0, 1], [0, 1], 'k--')
    ax.set_xlabel("Birth")
    ax.set_ylabel("Death")
    ax.set_title("Persistence Diagram")
    ax.legend()
    return fig
