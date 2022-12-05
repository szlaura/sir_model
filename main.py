import networkx as nx
import matplotlib.pyplot as plt
import EoN


def sir_plot(t, S, I, R):
    plt.plot(t, S, label='S')
    plt.plot(t, I, label='I')
    plt.plot(t, R, label='R')
    plt.xlabel('Time')
    plt.ylabel('Number of people')
    plt.legend()
    plt.show()


n = 10 ** 3
p1 = 5 / (n - 1)

graph = nx.fast_gnp_random_graph(n, p1)

rho = 0.005
p2 = 0.3

t, S, I, R = EoN.basic_discrete_SIR(graph, p=p2, rho=rho)

sir_plot(t, S, I, R)

plt.semilogy(t, S, label='S')
plt.semilogy(t, I, label='I')
plt.semilogy(t, R, label='R')
plt.xlabel('Time')
plt.show()
