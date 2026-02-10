docker run -u $(id -u):$(id -g) --rm -it -v $(pwd):/source -w /source aergus/latex latexmk -pdf -f presentation.tex
rm *.fls *.out *.bcf *.bbl *.aux *.blg *.fdb_latexmk *.log *.run.xml
docker run -u $(id -u):$(id -g) --rm -it -v $(pwd):/source -w /source aergus/latex latexmk -pdf -f presentation_notes.tex
