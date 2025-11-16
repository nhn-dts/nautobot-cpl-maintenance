NEW_VERSION=$1
sed -i "s/version = \".*\"/version = \"$NEW_VERSION\"/" ./pyproject.toml
