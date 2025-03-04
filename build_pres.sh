docker run -u $(id -u):$(id -g) --rm -it -v $(pwd):/source -w /source aergus/latex latexmk -pdf -f presentation.tex
docker run -u $(id -u):$(id -g) --rm -it -v $(pwd):/source -w /source aergus/latex latexmk -pdf -f presentation_notes.tex
