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

def deriv(state, t, N, beta, gamma):
    S, I, R = state
    # Change in S population over time
    dSdt = -beta * S * I / N
    # Change in I population over time
    dIdt = beta * S * I / N - gamma * I
    # Change in R population over time
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

effective_contact_rate = 0.5
recovery_rate = 1/4

# We'll compute this for fun
print("R0 is", effective_contact_rate / recovery_rate)

# What's our start population look like?
# Everyone not infected or recovered is susceptible
total_pop = 1000
recovered = 0
infected = 1
susceptible = total_pop - infected - recovered

# A list of days, 0-160
days = range(0, 160)

import pandas as pd
df = pd.read_csv('covidData.csv')

df1 = df[['PersonA', 'PersonB', 'Creator']]


# nem mukodik de probalkoztunk
import networkx as nx
G = nx.Graph()

G = nx.from_pandas_edgelist(df1, 'PersonA', 'PersonB', 'Creator')

from matplotlib.pyplot import figure
figure(figsize=(10, 8))
nx.draw_shell(G, with_labels=True)

print(nx)


df = pd.read_csv('covidData.csv', encoding='ISO-8859-1')
G = nx.from_pandas_edgelist(df, 'Reporter','Creator')

pos = nx.spring_layout(G, k=0.5, iterations=20)
plt.figure(dpi=120)
nx.draw_shell(G, node_size=50)

N = G.number_of_nodes()
rho = 10 / N
tmax = 200