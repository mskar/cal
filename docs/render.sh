#! /bin/sh

jupytext schedules.py --output "schedules.ipynb" --execute --set-kernel python3

quarto convert "$1"

quarto render "$1" --cache-refresh --profile javascript --metadata engine:jupyter --output "${1%.*}_javascript.ipynb"

quarto render "$1" --cache-refresh --profile julia --metadata engine:jupyter --output "${1%.*}_julia.ipynb"

quarto render "$1" --cache-refresh --profile python --metadata engine:jupyter --output "${1%.*}_python.ipynb"

quarto render "$1" --cache-refresh --profile r --metadata engine:jupyter --output "${1%.*}_r.ipynb"

# jupytext "${1%.*}_quarto_javascript.ipynb" --to js --output "${1%.*}.js" --set-kernel javascript

# jupytext "${1%.*}_quarto_python.ipynb" --to py --output "${1%.*}.py" --set-kernel python3

# jupytext "${1%.*}_quarto_r.ipynb" --to R --output "${1%.*}.R" --set-kernel ir

# jupytext "${1%.*}_quarto_julia.ipynb" --to jl --output "${1%.*}.jl" --set-kernel julia-1.9

# jupytext "${1%.*}.py" --output "${1%.*}_python.ipynb" --execute --set-kernel python3

# jupytext "${1%.*}.R" --output "${1%.*}_r.ipynb" --execute --set-kernel ir

# jupytext "${1%.*}.jl" --output "${1%.*}_julia.ipynb" --execute --set-kernel julia-1.9

# jupytext "${1%.*}.js" --output "${1%.*}_javascript.ipynb" --execute --set-kernel javascript

# Replace code chunks with embed short codes
cat "${1%.*}.qmd"  | gsed '/^```{python}\|^```{r}\|^```{julia}\|^```{javascript}/,/^```$/ { # set a range and say what should happen in that range below
    /^```{.*}$\|#| tags:/!d; # delete all but the first line and tags line of all code chunks
    N;s/\n//g; # join pairs of lines in all code blocks
    s/^```{\(.*\)}#| tags: \[\(.*\)\]/{{< embed '"${1%.*}"'_\1\.ipynb#\2 echo=true >}}/g; # replace code chunk and comment syntax with shortcode syntax
    /{{< embed .*\.ipynb#.* .* >}}/!d # delete anything that is not an embed shortcode with a tag
}'> "${1%.*}"_embed.qmd

# Here is the above command in a single line without inline comments
# replace code chunks with embed short codes by setting a range, deleting all but two lines, joining the lines, substituting, and deleting anything that does not match the shortcode pattern
# cat "${1%.*}.qmd"  | gsed '/^```{/,/^```$/ { /^```{.*}$\|#| tags:/!d; N;s/\n//g; s/^```{\(.*\)}#| tags: \[\(.*\)\]/{{< embed _\1\.ipynb#\2 >}}/g; /{{< embed .*\.ipynb#.* >}}/!d }' | sed "s/{{< embed \(.*\)\.ipynb#\(.*\) >}}/{{< embed ${1%.*}\1\.ipynb#\2 echo=true >}}/g" > "${1%.*}_embed.qmd"

# Ranges example: This deletes all code chunks
# cat mulang.qmd | sed '/^```{/,/^```$/d'\n

# This inserts a tabset in front of every level-four (####) JavaScript header in the embed qmd
cat "${1%.*}"_embed.qmd | gsed '/#### JavaScript/i ::: {.panel-tabset group="language"}\n'> "${1%.*}"_tabset.qmd

# recreate html output file with embedded notebooks
quarto render "${1%.*}_tabset.qmd" --cache-refresh --profile knitr --metadata engine:knitr
