docker run --rm -it -v \
$(pwd):/source \
-w /source aergus/latex \
latexmk -pdf presentation.tex
