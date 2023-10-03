Для сборки:
```
docker build . -t sender
```

Для запуска:
```
docker run --rm --name=sender -d -v /var/log/super_mega_critical.csv:/var/log/data.csv sender
```
