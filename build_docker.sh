#/bin/bash -ex
VERSION=$(cat VERSION)
echo "VERSION: $VERSION"
docker build -t cmq2525/mdbook-pdf-summary:$VERSION --build-arg VERSION=$VERSION .