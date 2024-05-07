docker run --rm -it -v $(pwd):/source -w /source aergus/latex latexmk -bibtex -pdf dissertation.tex
docker run --rm -it -v $(pwd):/source -w /source aergus/latex latexmk -bibtex -pdf synopsis.tex
