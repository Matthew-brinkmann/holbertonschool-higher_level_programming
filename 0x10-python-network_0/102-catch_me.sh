#!/bin/bash
# Full story of how i achieved this is in advanced_task_2.md
curl -sLX PUT -d "user_id=98" -H "Origin:HolbertonSchool" 0.0.0.0:5000/catch_me
