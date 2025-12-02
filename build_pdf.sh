## synopsis

#rm *.fls *.out *.bcf *.bbl *.aux *.pdf *.blg *.fdb_latexmk *.log *.run.xml
#docker run -u $(id -u):$(id -g) --rm -it -v $(pwd):/source -w /source raabf/texstudio-versions latexmk -bibtex -pdf synopsis.tex
#docker run -u $(id -u):$(id -g) --rm -it -v $(pwd):/source -w /source raabf/texstudio-versions latexmk -bibtex -pdf synopsis.tex
#cp --force synopsis.pdf syn_$(date +%d)$(date +%b).pdf


## dissertation
#
#rm *.fls *.out *.bcf *.bbl *.aux *.blg *.fdb_latexmk *.log *.run.xml
docker run -u $(id -u):$(id -g) --rm -it -v $(pwd):/source -w /source raabf/texstudio-versions latexmk -bibtex -pdf dissertation.tex
docker run -u $(id -u):$(id -g) --rm -it -v $(pwd):/source -w /source raabf/texstudio-versions latexmk -bibtex -pdf dissertation.tex
cp --force dissertation.pdf diss_$(date +%d)$(date +%b).pdf

#docker run -u $(id -u):$(id -g) --rm -it -v $(pwd):/source -w /source raabf/texstudio-versions latexmk -bibtex -pdf presentation.tex
#cp --force presentation.pdf pres_$(date +%d)$(date +%b).pdf
