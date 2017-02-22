import fetch_data
from markov_python.cc_markov import MarkovChain

mc = MarkovChain()
mc.add_string(fetch_data.return_string())
# print mc.generate_text()

print " ".join(str(x) for x in mc.generate_text())