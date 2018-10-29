#!/bin/bash
echo "BUILDING TUTORIA"
cd tutoria && make rebuild_empty
python manage.py runserver
