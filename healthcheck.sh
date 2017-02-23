#!/bin/bash

STATUS=$(curl http://localhost:8000/status/)
if (($STATUS > 0)); then
  exit 1
else
  exit 0
fi
