# Instruction

#### URL to func

> 0.0.0.0:8080/function/ahrefsget
>
> 0.0.0.0:8080/function/ahrefspost?token={TOKEN}&domain={DOMAIN}

#### Settings Database
> The docker-compose file has username, password, db name and port settings. The same settings are the same in the **handlers/env.yml** file, they refer to the connection of functions to the database. They may be replaced if the database is deployed in the cloud.

#### Locally 
> **Docker and faas-cli** must be installed.
> Being at the root of the project, execute the command **make**.
> Launch the docker container with database and run 2 functions