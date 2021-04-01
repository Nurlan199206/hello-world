[![Build Status](https://travis-ci.org/Nurlan199206/hello-world.svg?branch=master)](https://travis-ci.org/Nurlan199206/hello-world)


# hello-world


argocd app create test1 \
--repo https://github.com/Nurlan199206/test1.git \
--path manifests \
--dest-server https://kubernetes.default.svc \
--dest-namespace default
