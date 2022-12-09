# Stable Coding Challenge

In this repository you will find Xavier Civit's solution to three problems proposed by the [stable](https://www.stableprice.com/) company to assess its level as a software developer.

## Comments to the reviewer

I have solved both q1 and q2 without consulting the internet. Their solutions are O(n) and I think they are the most optimal.

The first solution I did for q3 was the greedy one, finally I implemented an O(nW) solution where n is the number of stocks and W is the saving.
The algorithm implemented is the 0-1 knapsack based on the Wikipedia pseudocode which I had to [correct](https://en.wikipedia.org/w/index.php?title=Knapsack_problem&diff=1126513814&oldid=1123980612).

## Repo structure

- questions statement: `questions/q{i}/README.md`
- solutions: `questions/q{i}/q{i}.py`
- tests on pytests framework: `tests/q{i}.py`

## Run tests

The tests are implemented with the pytests library and can be run with the `pytest .` command.
Black has been used as a formatter.
All the functions have been typed, you can run the mypy test with
`mypy .`
The code also passes the `pylint` test. I disabled C0114 so as not to comment the modules. `pylint questions tests`

## Comments

- The names proposed in the statements for functions or variables have been modified to comply with pep8.
- The solutions are implemented with python 3.9 without any additional library. There are development dependencies which you will find in `dev-requirements.txt`.
- There are github actions that run the tests on push and pull_requests to the main branch.
