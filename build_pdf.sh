docker run -u $(id -u):$(id -g) --rm -it -v $(pwd):/source -w /source aergus/latex latexmk -bibtex -pdf dissertation.tex
docker run -u $(id -u):$(id -g) --rm -it -v $(pwd):/source -w /source aergus/latex latexmk -bibtex -pdf synopsis.tex
docker run -u $(id -u):$(id -g) --rm -it -v $(pwd):/source -w /source aergus/latex latexmk -pdf presentation.tex
