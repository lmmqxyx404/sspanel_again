# sspanel_again
learn sspanel

# python project
## poetry
use poetry to manage the project
```pip install poetry```
Then use relative file to start the project.
Pay attention that the poetry could require higher python version

```poetry install```
### poetry details
1. `poetry env use python`
2. `poetry config --list`
3. `poetry config virtualenvs.in-project true`
4. `poetry shell`

## then install uwsgi

# the vital element of the project
## use root privilidge to map the port.

## relative command
### first of all
stop all container.
### second
use the root to execute the following command
```sudo podman-compose up -d ```

## todo
### delete relative image and containers.

### replace the frontend.
