#!/bin/bash
# Issues
# * https://github.com/devcontainers/features/issues/634#issuecomment-1684691322
# * https://github.com/nektos/act/issues/1658
# * https://github.com/moby/moby/issues/44263
# * https://github.com/docker/for-linux/issues/535
# * https://github.com/docker/for-linux/issues/476
# * https://github.com/devcontainers/features/issues/634
# * https://github.com/orgs/community/discussions/63776
# * https://github.com/devcontainers/features/issues/285
echo "Waiting for Docker to start"

#Features: https://github.com/devcontainers/features

# https://tldp.org/LDP/abs/html/fto.html
# Wait for Docker to start up
while [ ! -S /var/run/docker.sock ]; do
  echo -n "."
  /usr/local/share/docker-init.sh
  sleep 1
done

echo "Docker is running!"