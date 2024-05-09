FROM hollowman6/mdbook-pdf
ARG VERSION
# Above is copy from mdbook-pdf
RUN pip3 install mdbook_pdf_summary==${VERSION}

ENTRYPOINT mdbook-pdf-summary