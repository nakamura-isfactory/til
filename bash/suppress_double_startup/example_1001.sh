#!/usr/bin/bash
#二重起動チェック
CMDLINE=$(cat /proc/$$/cmdline | xargs --null)
if [[ $$ -ne $(pgrep -oxf "${CMDLINE}") ]]; then
  echo "既に起動しています!" >&2
  exit 9
fi
echo [$$] before sleep
sleep 5
echo [$$] after sleep

