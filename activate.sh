eval $(poetry env activate)
if [ -f ".env" ]; then
  if [ -n "$BASH_VERSION" ]; then
    set -o allexport
    source .env
    set +o allexport
  elif [ -n "$ZSH_VERSION" ]; then
    setopt allexport
    source .env
    unsetopt allexport
  else
    set -a
    . .env
    set +a
  fi
  echo "Loaded environment variables from .env"
fi
make setup-config
