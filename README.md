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

```
python gen 100 Factor
```

