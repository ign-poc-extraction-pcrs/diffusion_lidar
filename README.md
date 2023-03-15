# Interface de diffusion de donnée lidar

Avant de push coté backend verifier black, pylint, et tests unitaires si tu en a fais des nouveaux

pour verifier pylint à la racine du projet
```
pylint --rcfile=backend/.pylintrc --disable=fixme backend --recursive=y
```

pour verifier le formatage avec black
```
black --diff --check backend
```
Si erreur, appliquer le reformatage avec black
```
black <file>
```

test unitaire à la racine du projet
```
pytest backend/api/tests
```

run projet 
```
docker-compose up
```