docker run --rm -it -v \
$(pwd):/source \
-w /source aergus/latex \
latexmk -bibtex -pdf presentation.tex
