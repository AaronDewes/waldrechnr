import pytest

from api import eval_input

cases = [
    ('242/33',
     [{'title': 'SymPy', 'input': '242/33', 'output': {'type': 'Tex', 'tex': '\\frac{22}{3}'}},
      {'name': 'float_approximation', 'variable': 'None', 'title': 'Floating-point approximation',
       'input': '(22/3).evalf()', 'pre_output': '', 'parameters': ['digits']}]),
    ('12',
     [{'title': 'SymPy', 'input': '12', 'output': {'type': 'Tex', 'tex': '12'}},
      {'name': 'digits', 'variable': 'None', 'title': 'Digits in base-10 expansion of number',
       'input': 'len(str(12))', 'pre_output': '', 'parameters': []},
      {'name': 'factorization', 'variable': 'None', 'title': 'Factors',
       'input': 'factorint(12)', 'pre_output': '', 'parameters': []},
      {'name': 'factorizationDiagram', 'variable': 'None', 'title': 'Factorization Diagram',
       'input': 'factorint(12)', 'pre_output': '', 'parameters': []}]),
    ('div(x**2 - 4 + x, x-2)',
     [{'input': 'div(x**2-4+x,x-2)',
       'output': {'tex': '\\mathrm{div}(x^{2} + x - 4, x - 2)', 'type': 'Tex'},
       'title': 'SymPy'},
      {'input': 'div(x**2-4+x,x-2)',
       'output': {'list': [{'tex': 'x + 3', 'type': 'Tex'}, {'tex': '2', 'type': 'Tex'}], 'type': 'List'},
       'title': 'Result'}]),
    ('factor(x**2 - 1)',
     [{'input': 'factor(x**2-1)', 'title': 'SymPy',
       'output': {'tex': '\\mathrm{Factorization~of~}x^{2} - 1', 'type': 'Tex'}},
      {'input': 'factor(x**2-1)', 'title': 'Result',
       'output': {'tex': '\\left(x - 1\\right) \\left(x + 1\\right)', 'type': 'Tex'}}]),
    ('solve(x**2 + 4*x + 181, x)',
     [{'title': 'SymPy', 'input': 'solve(x**2+4*x+181,x)',
       'output': {'type': 'Tex', 'tex': '\\mathrm{solve}\\;x^{2} + 4 x + 181=0\\;\\mathrm{for}\\;x'}},
      {'title': 'Result', 'input': 'solve(x**2+4*x+181,x)',
       'output': {'type': 'List',
                  'list': [{'type': 'Tex', 'tex': '-2 - \\sqrt{177} i', 'numeric': True,
                            'expression': '-2 - sqrt(177)*I', 'approximation': '-2.0 - 13.3041346956501 i'},
                           {'type': 'Tex', 'tex': '-2 + \\sqrt{177} i', 'numeric': True,
                            'expression': '-2 + sqrt(177)*I', 'approximation': '-2.0 + 13.3041346956501 i'}]}}]),
    ('sin(2*x)',
     [{'title': 'SymPy', 'input': 'sin(2*x)', 'output': {'type': 'Tex', 'tex': '\\sin{\\left(2 x \\right)}'},
       'num_variables': 1, 'variables': ['x'], 'variable': 'x'},
      {'name': 'trig_alternate', 'variable': 'x', 'title': 'Alternate forms', 'input': None, 'pre_output': '',
       'parameters': []},
      {'name': 'plot', 'variable': 'x', 'title': 'Plot', 'input': None, 'pre_output': '',
       'parameters': ['xmin', 'xmax', 'tmin', 'tmax', 'pmin', 'pmax']},
      {'name': 'roots', 'variable': 'x', 'title': 'Roots', 'input': 'solve(sin(2*x), x)', 'pre_output': 'x',
       'parameters': []},
      {'name': 'diff', 'variable': 'x', 'title': 'Derivative', 'input': 'diff(sin(2*x), x)',
       'pre_output': '\\frac{d}{d x} \\sin{\\left(2 x \\right)}', 'parameters': []},
      {'name': 'integral_alternate', 'variable': 'x', 'title': 'Antiderivative forms', 'input': None, 'pre_output': '',
       'parameters': []},
      {'name': 'series', 'variable': 'x', 'title': 'Series expansion around 0', 'input': 'series(sin(2*x), x, 0, 10)',
       'pre_output': '', 'parameters': []}]),
    ('diff(f(x)*g(x)*h(x))',
     [{'input': "diff(Function('f')(x)*Function('g')(x)*Function('h')(x))", 'num_variables': 1,
       'output': {'tex': '\\frac{d}{d x} f{\\left(x \\right)} g{\\left(x \\right)} h{\\left(x \\right)}',
                  'type': 'Tex'}, 'title': 'SymPy', 'variable': 'x', 'variables': ['x']},
      {'name': 'diff', 'input': 'diff(f(x)*g(x)*h(x), x)', 'parameters': [], 'title': 'Derivative', 'variable': 'x',
       'pre_output': '\\frac{d}{d x} f{\\left(x \\right)} g{\\left(x \\right)} h{\\left(x \\right)}'}]),
    ('integrate(tan(x))',
     [{'input': 'integrate(tan(x))', 'output': {'tex': '\\int \\tan{\\left(x \\right)}\\, dx', 'type': 'Tex'},
       'num_variables': 1, 'title': 'SymPy', 'variable': 'x', 'variables': ['x']},
      {'name': 'integral_alternate_fake', 'input': None, 'parameters': [], 'pre_output': '',
       'title': 'Antiderivative forms', 'variable': 'x'},
      {'name': 'intsteps', 'input': 'integrate(tan(x), x)', 'parameters': [],
       'pre_output': '', 'title': 'Integral Steps', 'variable': 'x'}]),
    ('10!!',
     [{'title': 'SymPy', 'input': 'factorial2(10)', 'output': {'type': 'Tex', 'tex': '3840'}},
      {'name': 'digits', 'variable': 'None', 'title': 'Digits in base-10 expansion of number',
       'input': 'len(str(3840))', 'pre_output': '', 'parameters': []},
      {'name': 'factorization', 'variable': 'None', 'title': 'Factors',
       'input': 'factorint(3840)', 'pre_output': '', 'parameters': []}]),
    ('totient(42)',
     [{'title': 'SymPy', 'input': 'totient(42)', 'output': {'type': 'Tex', 'tex': '12'},
       'num_variables': 0, 'variables': [], 'variable': 'None'},
      {'name': 'totient', 'variable': 'None', 'title': 'Step', 'input': 'totient(42)', 'pre_output': '',
       'parameters': []}]),
    ('totient(x)',
     [{'title': 'SymPy', 'input': 'totient(x)', 'output': {'type': 'Tex', 'tex': '\\phi\\left(x\\right)'},
       'num_variables': 1, 'variables': ['x'], 'variable': 'x'}]),
    ('rsolve(y(n+2)-y(n+1)-y(n), y(n))',
     [{'title': 'SymPy',
       'input': "rsolve(Function('y')(n+2)-Function('y')(n+1)-Function('y')(n),Function('y')(n))",
       'output': {'type': 'Tex',
                  'tex': '\\mathrm{Solve~the~recurrence~}- y{\\left(n \\right)} - y{\\left(n + 1 \\right)} + '
                         'y{\\left(n + 2 \\right)} = 0'}},
      {'title': 'Result',
       'input': "rsolve(Function('y')(n+2)-Function('y')(n+1)-Function('y')(n),Function('y')(n))",
       'output': {'type': 'Tex',
                  'tex': 'C_{0} \\left(\\frac{1}{2} - \\frac{\\sqrt{5}}{2}\\right)^{n} + C_{1} \\left(\\frac{1}{2} + '
                         '\\frac{\\sqrt{5}}{2}\\right)^{n}'}},
      {'title': 'Simplification',
       'input': '(C0*(1 - sqrt(5))**n + C1*(1 + sqrt(5))**n)/2**n',
       'output': {'type': 'Tex',
                  'tex': '2^{- n} \\left(C_{0} \\left(1 - \\sqrt{5}\\right)^{n} + C_{1} \\left(1 + '
                         '\\sqrt{5}\\right)^{n}\\right)'}},
      None]),
    ('diophantine(x**2 - 4*x*y + 8*y**2 - 3*x + 7*y - 5)',
     [{'title': 'SymPy', 'input': 'diophantine(x**2-4*x*y+8*y**2-3*x+7*y-5)',
       'output': {'type': 'Tex',
                  'tex': '\\begin{align}&\\mathrm{Solve~the~diophantine~equation~}x^{2} - 4 x y - 3 x + 8 y^{2} + 7 y '
                         '- 5 = 0\\\\&\\mathrm{where~}(x, y)\\mathrm{~are~integers}\\end{align}'}},
      {'title': 'Result', 'input': 'diophantine(x**2-4*x*y+8*y**2-3*x+7*y-5)',
       'output': {'type': 'Table', 'titles': ('x', 'y'),
                  'rows': [[{'type': 'Tex', 'tex': '5'}, {'type': 'Tex', 'tex': '1'}],
                           [{'type': 'Tex', 'tex': '2'}, {'type': 'Tex', 'tex': '1'}]]}}]),
    ('plot(sin(x) + cos(2*x))',
     [{'input': 'plot(sin(x)+cos(2*x))', 'num_variables': 1,
       'output': {'tex': '\\mathrm{Plot~}\\sin{\\left(x \\right)} + \\cos{\\left(2 x \\right)}', 'type': 'Tex'},
       'title': 'SymPy', 'variable': 'x', 'variables': ['x']},
      {'name': 'plot', 'input': ['sin(x) + cos(2*x)'], 'parameters': ['xmin', 'xmax', 'tmin', 'tmax', 'pmin', 'pmax'],
       'pre_output': '', 'title': 'Plot', 'variable': 'x'}]),
    ('plot(r=1-sin(theta))',
     [{'input': 'plot(r=1-sin(theta))', 'num_variables': 1,
       'output': {'tex': '\\mathrm{Plot~}\\left\\{ \\mathtt{\\text{r}} : 1 - \\sin{\\left(\\theta \\right)}\\right\\}',
                  'type': 'Tex'},
       'title': 'SymPy', 'variable': 'x', 'variables': ['x']},
      {'name': 'plot', 'input': ['r = 1 - sin(theta)'], 'parameters': ['xmin', 'xmax', 'tmin', 'tmax', 'pmin', 'pmax'],
       'pre_output': '', 'title': 'Plot', 'variable': 'x'}]),
    ('π',
     [{'title': 'SymPy', 'input': 'π', 'output': {'type': 'Tex', 'tex': '\\pi'}},
      {'name': 'float_approximation', 'variable': 'None', 'title': 'Floating-point approximation',
       'input': '(pi).evalf()', 'pre_output': '', 'parameters': ['digits']}]),
]


@pytest.mark.parametrize('expression, expected', cases)
def test(expression: str, expected: dict):
    actual = eval_input(expression)['result']
    assert len(actual) == len(expected)
    for a, e in zip(actual, expected):
        assert e is None or a == e
