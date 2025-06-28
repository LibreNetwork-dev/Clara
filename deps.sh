#!/bin/bash
set -e

install_debian() {
  sudo apt update
  sudo apt install -y mpv wl-clipboard xclip make gcc libreadline-dev
}

install_fedora() {
  sudo dnf install -y mpv wl-clipboard xclip make gcc readline-devel
}

install_arch() {
  sudo pacman -Sy --noconfirm mpv wl-clipboard xclip base-devel
}

install_alpine() {
  sudo apk add mpv wl-clipboard xclip make gcc readline-dev musl-dev
}

install_opensuse() {
  sudo zypper install -y mpv wl-clipboard xclip make gcc readline-devel
}

if [ -f /etc/os-release ]; then
  . /etc/os-release
  case "$ID" in
    debian|ubuntu|linuxmint)
      install_debian
      ;;
    fedora)
      install_fedora
      ;;
    arch|manjaro)
      install_arch
      ;;
    alpine)
      install_alpine
      ;;
    opensuse*|suse)
      install_opensuse
      ;;
    *)
      echo "Unsupported or unknown distro: $ID"
      echo "please install deps manually"
      exit 1
      ;;
  esac
  pip install --upgrade pip
  pip install sentence-transformers torch datasets transformers[torch]
else
  echo "cant detect distro (/etc/os-release not found)"
  exit 1
fi

echo "deps done."
