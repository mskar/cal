# isosevcal


# General PDFs from html
`find 2022 -name '*.html' | sed -e 's/\(.*\).html/\1.html \1.pdf/' | xargs -n2 bash -c 'pandoc $0 -o $1'`
