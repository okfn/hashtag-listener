#!/usr/bin/env python
from app import app
db.create_all()
app.run(debug=True)
