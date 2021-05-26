# Password Generator

## Overview

Have always wanted to create a local password-manager and/or generator via Docker and a local database.

The idea is to bring up the container when a password is to be generated then saved to a db, or making a request for a password.

On my Linux environment where I host Docker, I create a folder to attach as a volume to a docker container.

For example, with this project I am attaching a volume named 'ddata/pwdb' to a mongodb container's path of '/data/db', ddata is my short name for dockerdata.  This path name can be your preference for simplicity you may call it dockerdata or dockervolumes, etc.