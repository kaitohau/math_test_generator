# Math Test Generator
Automatically generate math problems and output pdf papers(exam and solution).

数学の問題を自動生成し、PDFにて問題と回答を出力します。



# Requirements

- Python 3 (recomend conda)
- Sympy (recomend conda)
- LaTeX

# How to Install  

- Install [Anaconda](https://www.anaconda.com/distribution/)
- Install LaTex
  - MacOS: [MacTex](https://texwiki.texjp.org/?MacTeX#mirror)
- clone this repo

# How to Run

```
git clone git@github.com:kaitohau/math_test_generator.git
cd gen
python gen

```

- options
  - Number of problems
    - 50 (default)
  - Test type
    - Quadratic (default)
    - Factor
    - plus-minus

```
python gen 100 Factor
```

# How to Add Test Type

- Add generator in [math_test_generator](https://github.com/kaitohau/math_test_generator)/[gen](https://github.com/kaitohau/math_test_generator/tree/master/gen)/**generator.py**
  - write rules for each test type: ie. if you don't need rules just copy and rename.
- Add math class in [math_test_generator](https://github.com/kaitohau/math_test_generator)/[gen](https://github.com/kaitohau/math_test_generator/tree/master/gen)/**math.py**
- Import added module on  **__init__.py** and **gen.py**