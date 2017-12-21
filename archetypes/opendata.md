---
title: "{{ replace .TranslationBaseName "-" " " | title }}"
date: {{ .Date }}
outputs:
- html
- dcxml
- dcresolve
---
