#!/usr/bin/env bash

## configs other than k3s case should be handled when implemented.
if [ -e /etc/rancher/k3s/k3s.yaml ] ; then
    sudo install -C -m 700 -o $USER -g $USER /etc/rancher/k3s/k3s.yaml "$HOME/.kube/config"
else
    echo "WARNING: could not find kubeconfig in /etc/rancher/k3s/k3s.yaml. Installing another vendor ??"
fi
