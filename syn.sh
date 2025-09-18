rm *.fls *.out *.bcf *.bbl *.aux *.pdf *.blg *.fdb_latexmk *.log *.run.xml
docker run -u $(id -u):$(id -g) --rm -it -v $(pwd):/source -w /source raabf/texstudio-versions latexmk -bibtex -pdf synopsis.tex
docker run -u $(id -u):$(id -g) --rm -it -v $(pwd):/source -w /source raabf/texstudio-versions latexmk -bibtex -pdf synopsis.tex
